import json
from datetime import date

import plotly.graph_objects as go
import streamlit as st

from utils.data_manager import (
    compliance_to_json,
    get_article_stats,
    get_pillar_stats,
    save_compliance,
)
from utils.dora_articles import PILLARS


# ── Gauge chart ──────────────────────────────────────────────────────────────

def make_gauge(value: float, title: str, color: str) -> go.Figure:
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            title={"text": title, "font": {"size": 13}},
            number={"suffix": "%", "font": {"size": 22}, "valueformat": ".1f"},
            gauge={
                "axis": {"range": [0, 100], "tickwidth": 1},
                "bar": {"color": color, "thickness": 0.3},
                "bgcolor": "white",
                "borderwidth": 1,
                "bordercolor": "#ccc",
                "steps": [
                    {"range": [0, 40], "color": "#FFEBEE"},
                    {"range": [40, 80], "color": "#FFF8E1"},
                    {"range": [80, 100], "color": "#E8F5E9"},
                ],
                "threshold": {
                    "line": {"color": "#2E7D32", "width": 3},
                    "thickness": 0.75,
                    "value": 80,
                },
            },
        )
    )
    fig.update_layout(height=210, margin=dict(t=50, b=10, l=20, r=20), paper_bgcolor="rgba(0,0,0,0)")
    return fig


# ── Status badge helper ───────────────────────────────────────────────────────

def status_badge(pct: float, is_na: bool = False) -> str:
    if is_na:
        return "⚪ Not Applicable"
    if pct == 100:
        return "🟢 Compliant"
    if pct >= 80:
        return "🟡 Near-compliant"
    if pct > 0:
        return "🟠 In Progress"
    return "🔴 Not Started"


# ── Sidebar export / import ───────────────────────────────────────────────────

def render_sidebar(compliance: dict) -> dict:
    """Renders sidebar controls and returns (possibly updated) compliance dict."""
    with st.sidebar:
        st.header("Settings")

        company = st.text_input(
            "Organisation name",
            value=compliance["metadata"].get("company_name", ""),
            key="sb_company",
        )
        assessor = st.text_input(
            "Assessor",
            value=compliance["metadata"].get("assessor", ""),
            key="sb_assessor",
        )
        if company != compliance["metadata"].get("company_name", ""):
            compliance["metadata"]["company_name"] = company
        if assessor != compliance["metadata"].get("assessor", ""):
            compliance["metadata"]["assessor"] = assessor

        st.divider()
        st.subheader("Export / Import")

        st.download_button(
            label="⬇️  Export compliance.json",
            data=compliance_to_json(compliance),
            file_name="compliance.json",
            mime="application/json",
            use_container_width=True,
        )

        uploaded = st.file_uploader("⬆️  Import compliance.json", type="json", key="importer")
        if uploaded is not None:
            try:
                imported = json.load(uploaded)
                st.session_state.compliance = imported
                compliance = imported
                st.success("Imported successfully.")
            except Exception as e:
                st.error(f"Invalid file: {e}")

        st.divider()
        st.caption(
            "**Workflow:** Edit → *Save to File* (local) or export JSON, "
            "commit to GitHub, Streamlit auto-redeploys."
        )
        last_saved = compliance["metadata"].get("last_saved", "—")
        st.caption(f"Last saved: **{last_saved}**")

    return compliance


# ── Per-pillar page renderer ──────────────────────────────────────────────────

def render_pillar_page(pillar_id: str) -> None:
    pillar = next((p for p in PILLARS if p["id"] == pillar_id), None)
    if pillar is None:
        st.error(f"Unknown pillar: {pillar_id}")
        return

    if "compliance" not in st.session_state:
        from utils.data_manager import load_compliance
        st.session_state.compliance = load_compliance()

    compliance = st.session_state.compliance
    compliance = render_sidebar(compliance)
    st.session_state.compliance = compliance

    stats = get_pillar_stats(compliance, pillar)

    # Header
    st.title(f"{pillar['icon']} Chapter {pillar['chapter']} — {pillar['title']}")
    st.caption(f"Articles {pillar['articles_range']}  ·  DORA Regulation (EU) 2022/2554")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Pillar Compliance", f"{stats['pillar_pct']:.1f}%")
    col2.metric("Controls Met", f"{stats['total_checked']} / {stats['total_controls']}")
    col3.metric("N/A Articles", str(stats["na_count"]))
    col4.metric("Status", status_badge(stats["pillar_pct"]))

    st.progress(stats["pillar_pct"] / 100)
    st.divider()

    # Per-article forms
    for article in pillar["articles"]:
        art_data = compliance["articles"].get(
            article["id"],
            {"controls": {c["id"]: False for c in article["controls"]}, "owner": "", "due_date": "", "notes": "", "not_applicable": False},
        )
        is_na = art_data.get("not_applicable", False)
        checked, total, pct, _ = get_article_stats(compliance, article["id"])

        if is_na:
            expander_label = f"**Art. {article['id']}  ·  {article['title']}**  —  ⚪ Not Applicable"
        else:
            badge = status_badge(pct)
            expander_label = f"**Art. {article['id']}  ·  {article['title']}**  —  {badge}  ({pct:.0f}%)"

        with st.expander(expander_label, expanded=(not is_na and pct == 0)):
            if not is_na:
                st.progress(pct / 100)
                st.markdown(f"**{checked} of {total} sub-requirements met**")

            with st.form(key=f"form_{article['id']}"):
                new_na = st.toggle(
                    "Mark as Not Applicable",
                    value=is_na,
                    help="N/A articles are excluded from all compliance calculations.",
                )

                if new_na:
                    st.info("This article is marked as Not Applicable and will be excluded from compliance calculations. You can still record a rationale in the notes field below.")
                    new_controls = {c["id"]: False for c in article["controls"]}
                else:
                    st.markdown("##### Sub-requirements")
                    new_controls = {}
                    for ctrl in article["controls"]:
                        current = art_data["controls"].get(ctrl["id"], False)
                        new_controls[ctrl["id"]] = st.checkbox(ctrl["text"], value=current)

                st.markdown("##### Ownership & tracking")
                c1, c2 = st.columns(2)
                new_owner = c1.text_input("Owner", value=art_data.get("owner", ""))
                new_due = c2.text_input("Due date (YYYY-MM-DD)", value=art_data.get("due_date", ""))
                new_notes = st.text_area(
                    "Notes / evidence" if not new_na else "Rationale for N/A",
                    value=art_data.get("notes", ""),
                    height=80,
                )

                submitted = st.form_submit_button("💾  Save article", use_container_width=True)
                if submitted:
                    compliance["articles"][article["id"]] = {
                        "controls": new_controls,
                        "owner": new_owner,
                        "due_date": new_due,
                        "notes": new_notes,
                        "not_applicable": new_na,
                        "last_updated": str(date.today()),
                    }
                    st.session_state.compliance = compliance
                    try:
                        save_compliance(compliance)
                        st.success(f"Article {article['id']} saved.")
                    except Exception:
                        st.warning("Could not write to file (Streamlit Cloud). Use Export JSON to save your data.")
                    st.rerun()

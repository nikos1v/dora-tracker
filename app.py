import json

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from utils.data_manager import (
    compliance_to_json,
    get_article_stats,
    get_overall_stats,
    get_pillar_stats,
    load_compliance,
    save_compliance,
)
from utils.dora_articles import PILLARS
from utils.ui_components import make_gauge, render_sidebar, status_badge

st.set_page_config(
    page_title="DORA Compliance Tracker",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Load data ─────────────────────────────────────────────────────────────────
if "compliance" not in st.session_state:
    st.session_state.compliance = load_compliance()

compliance = st.session_state.compliance
compliance = render_sidebar(compliance)
st.session_state.compliance = compliance

# ── Header ────────────────────────────────────────────────────────────────────
col_h1, col_h2 = st.columns([3, 1])
with col_h1:
    company = compliance["metadata"].get("company_name", "")
    title_suffix = f" — {company}" if company else ""
    st.title(f"🛡️ DORA Compliance Tracker{title_suffix}")
    st.caption("EU Regulation 2022/2554 · Digital Operational Resilience Act · Articles 5–46")
with col_h2:
    st.markdown("")
    assessor = compliance["metadata"].get("assessor", "—")
    assessed = compliance["metadata"].get("assessment_date", "—")
    st.markdown(f"**Assessor:** {assessor}  \n**As of:** {assessed}")

st.divider()

# ── Overall KPIs ──────────────────────────────────────────────────────────────
overall = get_overall_stats(compliance)
pct = overall["overall_pct"]

k1, k2, k3, k4, k5 = st.columns(5)
k1.metric("Overall Compliance", f"{pct:.1f}%")
k2.metric("Controls Met", f"{overall['total_checked']}")
k3.metric("Applicable Controls", f"{overall['total_controls']}")
k4.metric("Remaining", f"{overall['total_controls'] - overall['total_checked']}")
k5.metric("N/A Articles", str(overall["na_count"]))

st.progress(pct / 100)
st.markdown("")

# ── Pillar gauges ─────────────────────────────────────────────────────────────
st.subheader("Compliance by Pillar")
gauge_cols = st.columns(5)
for i, pillar in enumerate(PILLARS):
    pstats = get_pillar_stats(compliance, pillar)
    with gauge_cols[i]:
        fig = make_gauge(
            pstats["pillar_pct"],
            f"{pillar['icon']} Ch.{pillar['chapter']}\n{pillar['title']}",
            pillar["color"],
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption(
            f"{pstats['total_checked']}/{pstats['total_controls']} controls  ·  "
            f"Arts. {pillar['articles_range']}"
        )

st.divider()

# ── Article-level summary table ───────────────────────────────────────────────
st.subheader("Article Summary")

rows = []
for pillar in PILLARS:
    pstats = get_pillar_stats(compliance, pillar)
    for art in pstats["articles"]:
        art_data = compliance["articles"].get(art["article_id"], {})
        rows.append(
            {
                "Pillar": pillar["title"],
                "Article": art["article_id"],
                "Title": art["title"],
                "Met": art["checked"],
                "Total": art["total"],
                "Compliance %": round(art["pct"], 1),
                "Status": status_badge(art["pct"], art["is_na"]),
                "Owner": art_data.get("owner", "—") or "—",
                "Due Date": art_data.get("due_date", "—") or "—",
            }
        )

df = pd.DataFrame(rows)

# Filter controls
filter_col1, filter_col2 = st.columns([2, 2])
with filter_col1:
    pillar_filter = st.multiselect(
        "Filter by pillar",
        options=[p["title"] for p in PILLARS],
        default=[],
        placeholder="All pillars",
    )
with filter_col2:
    status_filter = st.multiselect(
        "Filter by status",
        options=["🔴 Not Started", "🟠 In Progress", "🟡 Near-compliant", "🟢 Compliant", "⚪ Not Applicable"],
        default=[],
        placeholder="All statuses",
    )

filtered_df = df.copy()
if pillar_filter:
    filtered_df = filtered_df[filtered_df["Pillar"].isin(pillar_filter)]
if status_filter:
    filtered_df = filtered_df[filtered_df["Status"].isin(status_filter)]

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Compliance %": st.column_config.ProgressColumn(
            "Compliance %",
            min_value=0,
            max_value=100,
            format="%.1f%%",
        ),
    },
)

st.divider()

# ── Gap analysis: top non-compliant items ─────────────────────────────────────
st.subheader("Gap Analysis — Non-compliant Articles")

gaps = df[(df["Compliance %"] < 100) & (df["Status"] != "⚪ Not Applicable")].sort_values("Compliance %").head(15)
if gaps.empty:
    st.success("All articles are fully compliant. 🎉")
else:
    fig_bar = go.Figure()
    fig_bar.add_trace(
        go.Bar(
            x=gaps["Compliance %"],
            y=gaps.apply(lambda r: f"Art. {r['Article']} · {r['Title'][:45]}", axis=1),
            orientation="h",
            marker_color=[
                "#D32F2F" if v < 40 else "#F57C00" if v < 80 else "#FBC02D"
                for v in gaps["Compliance %"]
            ],
            text=[f"{v:.0f}%" for v in gaps["Compliance %"]],
            textposition="outside",
        )
    )
    fig_bar.update_layout(
        xaxis=dict(range=[0, 110], title="Compliance %"),
        yaxis=dict(autorange="reversed"),
        height=max(300, len(gaps) * 32),
        margin=dict(l=20, r=40, t=20, b=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
    )
    st.plotly_chart(fig_bar, use_container_width=True)

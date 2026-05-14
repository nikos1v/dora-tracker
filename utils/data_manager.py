import json
import os
from datetime import date

from utils.dora_articles import PILLARS

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "compliance.json")


def load_compliance():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Migration: add not_applicable field to older saved files
        for art_data in data.get("articles", {}).values():
            if "not_applicable" not in art_data:
                art_data["not_applicable"] = False
        return data
    return get_default_compliance()


def save_compliance(data):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    data["metadata"]["last_saved"] = str(date.today())
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, default=str)


def get_default_compliance():
    compliance = {
        "metadata": {
            "company_name": "",
            "assessment_date": str(date.today()),
            "assessor": "",
            "version": "1.0",
            "last_saved": "",
        },
        "articles": {},
    }
    for pillar in PILLARS:
        for article in pillar["articles"]:
            compliance["articles"][article["id"]] = {
                "controls": {c["id"]: False for c in article["controls"]},
                "owner": "",
                "due_date": "",
                "notes": "",
                "last_updated": "",
                "not_applicable": False,
            }
    return compliance


def get_article_stats(compliance, article_id):
    """Returns (checked, total, pct, is_na) for one article."""
    art_data = compliance["articles"].get(article_id)
    if art_data is None:
        return 0, 0, 0.0, False
    if art_data.get("not_applicable", False):
        return 0, 0, 0.0, True
    controls = art_data["controls"]
    total = len(controls)
    checked = sum(1 for v in controls.values() if v)
    pct = (checked / total * 100) if total > 0 else 0.0
    return checked, total, pct, False


def get_pillar_stats(compliance, pillar):
    """Returns stats dict for a whole pillar. N/A articles are excluded from pct calculations."""
    article_stats = []
    for article in pillar["articles"]:
        checked, total, pct, is_na = get_article_stats(compliance, article["id"])
        article_stats.append(
            {
                "article_id": article["id"],
                "title": article["title"],
                "checked": checked,
                "total": total,
                "pct": pct,
                "is_na": is_na,
            }
        )
    applicable = [s for s in article_stats if not s["is_na"]]
    total_controls = sum(s["total"] for s in applicable)
    total_checked = sum(s["checked"] for s in applicable)
    na_count = sum(1 for s in article_stats if s["is_na"])
    pillar_pct = (total_checked / total_controls * 100) if total_controls > 0 else 0.0
    return {
        "pillar_pct": pillar_pct,
        "total_controls": total_controls,
        "total_checked": total_checked,
        "na_count": na_count,
        "articles": article_stats,
    }


def get_overall_stats(compliance):
    """Returns aggregate stats across all pillars. N/A articles are excluded."""
    total_controls = 0
    total_checked = 0
    na_count = 0
    for pillar in PILLARS:
        stats = get_pillar_stats(compliance, pillar)
        total_controls += stats["total_controls"]
        total_checked += stats["total_checked"]
        na_count += stats["na_count"]
    overall_pct = (total_checked / total_controls * 100) if total_controls > 0 else 0.0
    return {
        "overall_pct": overall_pct,
        "total_controls": total_controls,
        "total_checked": total_checked,
        "na_count": na_count,
    }


def compliance_to_json(compliance) -> str:
    return json.dumps(compliance, indent=2, default=str)

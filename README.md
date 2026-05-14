# DORA Compliance Tracker

A Streamlit dashboard for tracking compliance against the Digital Operational Resilience Act (EU Regulation 2022/2554), covering all Articles 5–46.

## Features

- **5 pillars** matching DORA Chapters II–VI with individual gauge charts
- **Article-level checklists** — each article broken into specific sub-requirements
- **Owner, due date and notes** tracking per article
- **Gap analysis** bar chart of non-compliant articles
- **Export / Import** compliance data as JSON
- Filterable article summary table

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploying to Streamlit Community Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io), connect your repo, set `app.py` as the main file
3. Deploy

## Data workflow

Compliance data lives in `data/compliance.json`.

**Editing flow:**
1. Open the app, edit sub-requirement checkboxes on each pillar page
2. Click **Save article** to persist locally (or use **Export compliance.json** to download)
3. Commit `data/compliance.json` to GitHub
4. Streamlit auto-redeploys with updated data

> **Note:** Streamlit Community Cloud does not persist file writes between sessions.  
> Always use **Export JSON** → commit to GitHub as the canonical save path.

## Structure

```
dora-tracker/
├── app.py                     # Dashboard home
├── pages/
│   ├── 1_ICT_Risk_Management.py
│   ├── 2_Incident_Management.py
│   ├── 3_Resilience_Testing.py
│   ├── 4_Third_Party_Risk.py
│   └── 5_Information_Sharing.py
├── utils/
│   ├── dora_articles.py       # All DORA article / sub-control definitions
│   ├── data_manager.py        # Load / save / stats helpers
│   └── ui_components.py       # Shared Streamlit components
├── data/
│   └── compliance.json        # Your compliance state (commit this)
└── requirements.txt
```

# SHL Assessment Recommender

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Start FastAPI backend:
```
uvicorn app.main:app --reload
```

3. Run Streamlit UI:
```
streamlit run streamlit_ui/streamlit_app.py
```

Try POSTing to `/recommend` with:
```json
{ "query": "Looking for a QA test", "duration_limit": 60 }
```

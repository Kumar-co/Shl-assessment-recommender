import streamlit as st
from app.model import recommend

st.title("SHL Assessment Recommender")
query = st.text_area("Enter job description or query:")
duration = st.slider("Max Duration (mins)", 10, 120, 60)

if st.button("Recommend"):
    results = recommend(query, duration)
    if results:
        st.write("Top Recommendations:")
        st.table(results)
    else:
        st.write("No matching assessments found.")

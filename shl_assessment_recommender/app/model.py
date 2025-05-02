import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("app/shl_catalog.csv")
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['keywords'])

def recommend(query, duration_limit=90):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, tfidf_matrix).flatten()
    df['score'] = scores
    df_filtered = df[df['duration'] <= duration_limit]
    return df_filtered.nlargest(10, 'score')[[
        'assessment_name', 'url', 'remote_support',
        'adaptive_support', 'duration', 'test_type'
    ]].to_dict(orient='records')

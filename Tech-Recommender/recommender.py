import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sys
import os

def load_dataset(filepath):
    """Step 1: Ingestion - Load and validate the dataset"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"❌ Dataset '{filepath}' not found. Place it in the same directory.")
    return pd.read_csv(filepath)

def build_vectorizer(df):
    """Step 2: Processing - TF-IDF Feature Extraction"""
    # 'skills' column contains comma-separated skill strings
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['skills'])
    return vectorizer, tfidf_matrix

def get_recommendations(user_skills, df, vectorizer, tfidf_matrix, top_n=3):
    """Steps 3 & 4: Scoring, Sorting, and Filtering"""
    # 🛡️ Cold Start Bypass: Enforce minimum data density
    if len(user_skills) < 3:
        return "⚠️ Cold Start Alert: Please provide at least 3 skills for accurate matching."
    
    # Transform user input into the same TF-IDF vector space
    user_vector = vectorizer.transform([" ".join(user_skills)])
    
    # Step 3: Scoring - Cosine Similarity
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix).flatten()
    
    # Attach scores and prepare for sorting
    df['match_score'] = similarity_scores
    
    # Step 4: Sorting & Filtering
    sorted_df = df.sort_values(by='match_score', ascending=False).reset_index(drop=True)
    return sorted_df[['job_role', 'skills', 'match_score']].head(top_n)

def main():
    print("🚀 DecodeLabs Project 3: AI Tech Stack Recommender")
    print("=" * 50)
    
    try:
        # 1️⃣ Ingestion
        df = load_dataset('raw_skills.csv')
        vectorizer, tfidf_matrix = build_vectorizer(df)
        
        # 📝 Onboarding Survey (User Cold Start Bypass)
        print("\n📝 Onboarding Survey")
        user_input = input("👉 Enter at least 3 skills separated by commas (e.g., Python, Cloud, Automation): ")
        user_skills = [skill.strip() for skill in user_input.split(',') if skill.strip()]
        
        # 2️⃣ Scoring → 3️⃣ Sorting → 4️⃣ Filtering
        recommendations = get_recommendations(user_skills, df.copy(), vectorizer, tfidf_matrix, top_n=3)
        
        if isinstance(recommendations, str):
            print(recommendations)
        else:
            print("\n🎯 Top 3 Recommended Career Paths:")
            print("-" * 50)
            for _, row in recommendations.iterrows():
                print(f"🔹 {row['job_role']} (Match: {row['match_score']:.2%})")
                print(f"   Required Skills: {row['skills']}\n")
                
    except Exception as e:
        print(f"❌ Execution Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

# 🚀 DecodeLabs Project 3: AI Tech Stack Recommender

## 📌 Project Overview
This project is a **Content-Based Recommendation Engine** designed to act as a "Digital Matchmaker" between a user's raw technical skills and optimal career paths. By leveraging mathematical similarity logic, it solves the modern digital problem of **Choice Overload**, delivering precise, data-driven career recommendations instead of random suggestions.

## 🎯 Objective
To bridge the gap between user profiles and item attributes using pure algorithmic logic, implementing the **Input-Process-Output (IPO)** model for active prediction and pattern alignment.

## 🏗️ The 4-Step IPO Pipeline
This system follows a strict architectural pipeline to transform raw user data into a refined Top-N list:
1. **Ingestion:** Captures explicit user inputs (minimum 3 skills) via an onboarding survey.
2. **Scoring:** Applies **TF-IDF Vectorization** to convert skills into weighted numerical vectors, then calculates **Cosine Similarity** to measure angular alignment between the user profile and job roles.
3. **Sorting:** Ranks all potential matches in descending order based on similarity scores.
4. **Filtering:** Truncates the dataset to a **Top-3 List** to prevent information overload and deliver actionable results.

## 🧠 Core AI Concepts Applied
- **Content-Based Filtering:** Maps user preferences directly to intrinsic job attributes, independent of other users' behavior.
- **TF-IDF Weighting:** Penalizes generic/high-frequency terms while amplifying specific, descriptive skills, ensuring accurate feature extraction.
- **Cosine Similarity:** Measures the mathematical angle between vectors, making it invariant to vector magnitude and highly accurate for text-based matching.
- **Cold Start Bypass:** Implements a mandatory onboarding survey (≥3 skills) to bootstrap a baseline vector, eliminating the User Cold Start problem.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Data Manipulation:** `pandas`
- **Machine Learning:** `scikit-learn` (`TfidfVectorizer`, `cosine_similarity`)
- **Dataset:** `raw_skills.csv` (Job roles mapped to required technical skills)

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/decodelabs-project3-tech-recommender.git
   cd decodelabs-project3-tech-recommender

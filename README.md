# AI Resume Analyzer & Skill Gap Recommender

## Overview
An AI-powered application that analyzes resumes against job descriptions using NLP and machine learning techniques. The system computes a match score, identifies missing skills, and provides personalized learning recommendations.

## Features
- Resume parsing from PDF files
- NLP-based skill extraction using spaCy
- Resume–Job Description matching using TF-IDF and cosine similarity
- Skill gap identification
- Personalized learning recommendations
- Interactive UI built with Streamlit

## Tech Stack
- Python
- Streamlit
- spaCy
- scikit-learn
- PDFPlumber

## How It Works
1. Resume and job description text are cleaned and preprocessed
2. Skills are extracted using NLP techniques
3. TF-IDF vectorization converts text into numerical form
4. Cosine similarity calculates relevance score
5. Missing skills are identified and learning recommendations are generated


## Use cases
1. Students can check resume relevance before applying for jobs
2. Candidates identifying missing skills for desired job role.
3. Recruiters performing quick resume screening.

## Project Structure
- app.py – Streamlit UI and app logic
- resume_parser.py – PDF resume text extraction
- text_cleaner.py – Text preprocessing
- skill_extractor.py – NLP-based skill extraction
- matcher.py – TF-IDF and cosine similarity matching
- recommender.py – Skill learning recommendations

    Live Demo: https://kaniishk005-ai-resume-analyzer-app-xfen7o.streamlit.app/


## How to Run
```bash
pip install -r requirements.txt
streamlit run app.py

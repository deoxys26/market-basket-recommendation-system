# Retail Market Basket Recommendation System

A full-stack retail recommendation system built using Apriori Association Rule Mining.

This project analyzes retail transaction data and recommends products frequently purchased together.

---

## Features

- Market Basket Analysis
- Product Recommendation Engine
- FastAPI Backend
- Streamlit Frontend
- Real-time Recommendations
- Association Rule Mining
- Retail Transaction Analytics

---

## Tech Stack

- Python
- pandas
- Streamlit
- FastAPI
- apyori
- openpyxl

---

## Project Architecture

Frontend (Streamlit)
↓
Backend API (FastAPI)
↓
Apriori Recommendation Engine
↓
Retail Dataset

---

## Dataset

Online Retail transactional dataset containing invoice-level retail purchases.

---

## How to Run

### Install Dependencies

pip install -r requirements.txt

### Run Backend

uvicorn backend.main:app --reload

### Run Frontend

streamlit run frontend/app.py

---

## Example Recommendation

Input:
WHITE METAL LANTERN

Output:
- CREAM CUPID HEARTS COAT HANGER
- KNITTED UNION FLAG HOT WATER BOTTLE

---

## Future Improvements

- Interactive analytics dashboard
- Product popularity charts
- Lift & confidence visualizations
- Cloud deployment
- Hybrid recommendation system

---

## Screenshots

<img width="1916" height="854" alt="image" src="https://github.com/user-attachments/assets/7128f089-cb4b-47b8-908c-4e845ce019f0" />


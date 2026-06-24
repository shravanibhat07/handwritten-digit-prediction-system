# ✍️ Handwritten Digit Prediction System
### Random Forest + Django Web Application

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Django](https://img.shields.io/badge/Django-Framework-green?style=flat&logo=django)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=flat&logo=scikit-learn)
![Domain](https://img.shields.io/badge/Domain-Computer%20Vision-blue?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-success?style=flat)

---

## 🧠 Problem Statement

Handwritten digit recognition is a fundamental computer vision problem with applications in postal services, bank cheque processing, and form digitization. This project builds an end-to-end ML pipeline that classifies handwritten digits (0–9) from pixel data and serves predictions in real time via a Django web interface.

> 💡 Built during my **Python & Machine Learning Internship** at Karunadu Technologies Pvt. Ltd. (Feb–May 2026)

---

## 🎯 What This Project Does

Pixel values from a handwritten digit image are processed by a trained Random Forest classifier, which predicts the digit (0–9) in real time. The entire pipeline — from data ingestion to browser-based prediction — is deployed using Django.

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.x |
| ML Algorithm | Random Forest Classifier |
| Web Framework | Django |
| Data Processing | Pandas, NumPy |
| Image Processing | Pixel value extraction |
| Model Serialization | Pickle (.pkl) |
| Frontend | HTML, CSS |
| Notebook | Jupyter Notebook |

---

## 🚀 How It Works

```
Handwritten Digit Image
        ↓
Pixel Value Extraction
        ↓
Data Preprocessing & Normalization
        ↓
Random Forest Classifier
        ↓
Digit Prediction (0–9)
        ↓
Django Web Interface Output
```

---

## 🗂️ Project Structure

```
handwritten-digit-prediction-system/
│
├── model training notebook    # Jupyter notebook for training
├── saved model (.pkl)         # Serialized Random Forest model
├── views.py                   # Django prediction logic
├── urls.py                    # URL routing
├── templates/                 # HTML pages
└── manage.py                  # Django entry point
```

---

## ⚙️ Setup & Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/shravanibhat07/handwritten-digit-prediction-system.git
cd handwritten-digit-prediction-system

# 2. Install dependencies
pip install django scikit-learn pandas numpy

# 3. Run the Django server
python manage.py runserver

# 4. Open in browser
http://127.0.0.1:8000/
```

---

## 🔬 ML Pipeline

1. **Data Collection** — Handwritten digit dataset (pixel values)
2. **Preprocessing** — Pixel normalization, reshaping
3. **Model Training** — Random Forest Classifier
4. **Evaluation** — Accuracy on test set
5. **Deployment** — Model serialized with Pickle, served via Django
6. **Real-time Prediction** — Browser-based digit classification

---

## 💡 Key Learnings

- Processing **image data as pixel arrays** for ML
- Building **end-to-end ML pipelines** from data to deployment
- **Django integration** with ML models for real-time predictions
- **Random Forest** for multi-class classification (10 classes: 0–9)
- Internship-level **production-ready** ML deployment

---

## 🌱 Future Improvements

- [ ] CNN (Convolutional Neural Network) for higher accuracy
- [ ] Canvas input — draw digits directly in browser
- [ ] Support for letters and symbols
- [ ] REST API endpoint for third-party integration
- [ ] Mobile app with real-time camera input

---

## 👩‍💻 About the Developer

**Shravani Bhat**
B.E. in Electronics & Communication Engineering | CGPA: 8.82/10
Alva's Institute of Engineering and Technology, Udupi

Completed as part of **Python & ML Internship** at Karunadu Technologies Pvt. Ltd.

- 📧 shravanibhat07@gmail.com
- 🔗 [LinkedIn](https://linkedin.com/in/shravanibhat07)
- 💻 [GitHub](https://github.com/shravanibhat07)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

⭐ **If you found this project useful, please give it a star!**

# 🏥 Multiple Disease Predictor (HACKARENA-HIT)

An AI-powered diagnostic and wellness advisory system that predicts **Heart and Kidney diseases** using custom-trained Machine Learning models. Built as a part of the **HackArena HIT**, this project combines robust predictive pipelines with highly interactive health and wellness recommendations.

---

## ✨ Features

- **🩺 Dual Diagnostic Engine**:
  - **Heart Disease Predictor**: Evaluates 13 key physiological factors (Age, ECG, Cholesterol, Resting Blood Pressure, etc.) to predict cardiovascular risks.
  - **Kidney Disease Predictor**: Uses clinical markers to identify potential chronic kidney diseases (CKD).
- **🧘 Interactive Wellness Advisory (Heart Health)**:
  *If a high risk is detected, the app automatically serves actionable guidance:*
  - **Yoga Guides**: Direct video demonstrations for restorative poses (*Tadasana*, *Vrikshasana*, and *Shavasana*).
  - **Dietary Planners**: Clear classifications of heart-friendly foods (greens, whole grains) and foods to avoid (high-sodium, trans-fats).
  - **Physical Activity Suggestions**: Low-impact exercises to improve heart health.
- **📍 Nearby Help Finder**: Integrates an instant click-to-search locator linking users to nearby cardiologists and hospitals on Google Maps.
- **🎨 Interactive Sidebar Navigation**: Modern medical UI dashboard built using `streamlit_option_menu`.

---

## 🛠️ Technology Stack

- **Machine Learning**: Scikit-Learn, Pandas, NumPy, Jupyter Notebooks (Model Training & Evaluation)
- **Serialization**: Pickle (`.pkl`) for saving and reloading pre-trained models
- **Web App Interface**: Streamlit, Streamlit Option Menu
- **Interactive Media**: Embedded YouTube Video APIs & Google Maps API

---

## 📂 Project Architecture

```text
HACKARENA-HIT/
├── DETECTOR APP.py          # Main Streamlit web application
├── heart final.ipynb        # Jupyter Notebook: Heart disease model training
├── kidney final.ipynb      # Jupyter Notebook: Kidney disease model training
├── heart.csv                # Dataset: Heart health records
├── kidney_disease.csv       # Dataset: Chronic Kidney Disease metrics
├── saved_models/            # Pre-trained models (serialized)
│   ├── heart (2).pkl        # Heart disease classification model
│   └── kindey.pkl           # Kidney disease classification model
└── README.md                # Project documentation

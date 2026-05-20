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

Read URL: https://github.com/arpbiswas04-coder/HACKARENA-HIT
Viewed content.md:1-800
Ran command: `Select-String -Path "C:\Users\ARPAN\.gemini\antigravity\brain\cff5b4cd-7e86-4107-89a9-d77376cf607a\.system_generated\steps\116\content.md" -Pattern "HACKARENA-HIT/(tree|blob)" | Select-Object -First 20 Line`
Ran command: `$content = Get-Content -Raw -Path "C:\Users\ARPAN\.gemini\antigravity\brain\cff5b4cd-7e86-4107-89a9-d77376cf607a\.system_generated\steps\116\content.md"
[regex]::Matches($content, 'href="/arpbiswas04-coder/HACKARENA-HIT/(blob|tree)/[^"]+"') | ForEach-Object { $_.Value } | Select-Object -Unique
`
Read URL: https://raw.githubusercontent.com/arpbiswas04-coder/HACKARENA-HIT/main/DETECTOR%20APP.py
Viewed content.md:1-119
Viewed content.md:100-119

I went through your repository for **HACKARENA-HIT**. It is a fantastic Machine Learning project! 

Here is a summary of what I found in your codebase:
* **The Core**: It is a **Multiple Disease Prediction Web Application** built using **Streamlit**.
* **Supported Diseases**:
  * **Heart Disease Predictor**: Takes 13 vital parameters (Age, Blood Pressure, Cholesterol, ECG, etc.), loads your trained `heart (2).pkl` model, and outputs a prediction.
    * *Stunning Features included:* In case of positive predictions, you've integrated **Health & Wellness suggestions** (yoga videos like Tadasana/Vrikshasana, exercises), **Dietary guidance** (foods to eat/avoid), and a **hospital locator via Google Maps**.
  * **Kidney Disease Predictor**: Uses your `kindey.pkl` trained model to diagnose kidney health based on clinical metrics.
* **Jupyter Notebooks**: `heart final.ipynb` and `kidney final.ipynb` containing your complete EDA, data analysis, model training, and evaluation scripts.
* **Datasets**: Real clinical datasets (`heart.csv` and `kidney_disease.csv`) used to train your models.

---

Here is a premium, visual, and highly structured **`README.md`** template tailored perfectly for **HACKARENA-HIT**. It is styled to look professional for hackathons, recruiters, and portfolios.

### Copy the Markdown code below for your README.md:

```markdown
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
```

## ⚙️ How It Works (Machine Learning Pipelines)

### 1. Data Analysis & Model Training
* The `heart final.ipynb` and `kidney final.ipynb` notebooks contain full exploratory data analysis (EDA), handling of missing values, and data scaling.
* Classification models were trained using historical medical records to ensure precise diagnostic scoring.
* Models were exported into highly optimized `.pkl` binaries using `pickle` for low-latency scoring.

### 2. Predictor Application
* Streamlit accepts real-time input fields from the user.
* Input arrays are normalized and cast to `float` values.
* The pre-trained classifiers process the data array and output active risk assessments in seconds.

---

## 🚀 Quick Start & Installation

### Prerequisites
- Python 3.9 or higher.

### 1. Clone the Repository
```bash
git clone https://github.com/arpbiswas04-coder/HACKARENA-HIT.git
cd HACKARENA-HIT
```

### 2. Create and Activate Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install streamlit streamlit-option-menu scikit-learn pandas numpy
```

### 4. Run the Application
```bash
streamlit run "DETECTOR APP.py"
```
The application will open automatically in your default browser at `http://localhost:8501`.

---

## 📜 License
This project is open-source and created for the HackArena HIT hackathon.
```

# 💧 Water Quality Prediction System using Machine Learning

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge&logo=streamlit)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A Machine Learning powered web application that predicts **water pollutant levels** for a monitoring station based on the **Year** and **Station ID**. The project uses historical water quality data to forecast important water quality parameters and provides an easy-to-use Streamlit interface.

---

# 📖 Project Overview

Water pollution is one of the biggest environmental challenges worldwide. Continuous monitoring of water quality helps identify contamination and supports better environmental management.

This project uses historical water quality records to train a Machine Learning model capable of predicting future pollutant concentrations.

The application allows users to:

- Select a year
- Enter a monitoring station ID
- Predict multiple water quality parameters instantly

---

# 🚀 Features

- 📊 Predicts multiple water quality parameters
- 🤖 Machine Learning based prediction
- 🌐 Interactive Streamlit web application
- ⚡ Fast real-time prediction
- 📈 Historical data driven model
- 🖥️ Simple and user-friendly interface

---

# 🧪 Predicted Water Parameters

The model predicts:

| Parameter | Description |
|------------|-------------|
| O₂ | Dissolved Oxygen |
| NO₃ | Nitrate |
| NO₂ | Nitrite |
| SO₄ | Sulphate |
| PO₄ | Phosphate |
| Cl | Chloride |

---

# 🏗 Project Structure

```
Water-Quality-Prediction/
│
├── app.py                     # Streamlit Application
├── WaterQualityPred.ipynb     # Model Training Notebook
├── pollution_model.pkl        # Trained ML Model
├── model_columns.pkl          # Encoded Feature Columns
├── PB_All_2000_2021.csv       # Dataset
├── Parameters_WQM_RMS.pdf
└── README.md
```

---

# ⚙️ Technologies Used

- Python
- Streamlit
- Scikit-Learn
- Pandas
- NumPy
- Joblib
- Pickle

---

# 📊 Dataset

The project is trained using historical water quality monitoring data.

Dataset includes:

- Monitoring Station ID
- Year
- Dissolved Oxygen (O₂)
- Nitrate (NO₃)
- Nitrite (NO₂)
- Sulphate (SO₄)
- Phosphate (PO₄)
- Chloride (Cl)

---

# 🧠 Machine Learning Model

The application uses a trained **Multi-Output Regression Model** capable of predicting multiple pollutants simultaneously.

### Workflow

```
Historical Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Model Training
        │
        ▼
Model Serialization (.pkl)
        │
        ▼
Streamlit Web Application
        │
        ▼
Prediction Results
```

---

# 💻 Installation

Clone the repository

```bash
git clone https://github.com/rayhenprakkash/Water-Quality-Prediction.git
```

Move into the project folder

```bash
cd Water-Quality-Prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# 📸 Application Preview

```
## 📸 Sample Output

<p align="center">
  <img src="sample%20output/output.png" alt="Sample Output" width="900">
</p>

---

# 📈 Future Improvements

- Water Quality Index (WQI) Prediction
- Water Quality Classification (Safe/Unsafe)
- Interactive Graphs
- GIS Map Integration
- Real-Time Sensor Integration
- Cloud Deployment
- User Authentication
- Prediction History Dashboard

---

# 🎯 Applications

- Environmental Monitoring
- Smart Cities
- Government Water Boards
- Pollution Analysis
- Academic Research
- Water Resource Management

---

# 👨‍💻 Author

**Rayhen Prakkash**

Computer Engineering (Cyber Security)

Machine Learning | Python | java | Data Science

GitHub: https://github.com/rayhenprakkash

---

# 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

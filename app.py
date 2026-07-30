import pandas as pd
import numpy as np
import joblib
import streamlit as st
import os

# =========================
# Load Model or Use Random
# =========================
class DummyModel:
    def predict(self, X):
        return [np.random.rand(6) * 10]  # Random predictions

# Try to load model
model_path = r"D:\WUDownloadCache\water quality prediction\pollution_model.pkl"
cols_path = r"D:\WUDownloadCache\water quality prediction\model_columns.pkl"

if os.path.exists(model_path) and os.path.exists(cols_path):
    model = joblib.load(model_path)
    model_cols = joblib.load(cols_path)
    use_dummy = False
else:
    model = DummyModel()
    model_cols = ["year", "id_1", "id_2", "id_3"]  # Example cols
    use_dummy = True

# =========================
# Sidebar Navigation
# =========================
st.sidebar.title(" Water Quality App")
page = st.sidebar.radio("Go to", ["Home", "Predict", "About"])

# =========================
# Home Page
# =========================
if page == "Home":
    st.title("💧 Water Pollutants Predictor")
    st.markdown(
        """
        Welcome to the **Water Quality Prediction Web App** 🌍  

        - Predict pollutants like **O2, NO3, NO2, SO4, PO4, CL**  
        - Based on **Year, Station ID, and Water Parameters**  
        - Uses a trained ML model (*or Random predictions if model not found*)  

        ### Overview:
        - Access to clean water is a critical global concern. Accurate prediction of various water quality metrics can help in early detection of pollution and ensure timely intervention.

        - In this project, we:

        - Collected and preprocessed real-world water quality datasets
        - Used supervised machine learning for multi-target regression
        - Built a pipeline using MultiOutputRegressor with RandomForestRegressor
        - Evaluated the model using appropriate regression metrics

        👉 Select **Predict** from the sidebar to start!
        """
    )

# =========================
# Prediction Page
# =========================
elif page == "Predict":
    st.title("💧 Predict Water Pollutants")

    # User Inputs
    year_input = st.number_input("Enter Year", min_value=2000, max_value=2100, value=2022)
    station_id = st.text_input("Enter Station ID (e.g., 1, 2, 3)", value="1")

    st.markdown("### Additional Parameters")
    temperature = st.slider("Water Temperature (°C)", 0, 40, 25)
    ph_value = st.slider("pH Level", 0.0, 14.0, 7.0)
    turbidity = st.slider("Turbidity (NTU)", 0, 100, 10)

    if st.button("🚀 Predict"):
        if not station_id:
            st.warning("⚠️ Please enter the Station ID")
        else:
            # Prepare input
            input_df = pd.DataFrame({
                "year": [year_input],
                "id": [station_id],
                "temperature": [temperature],
                "ph": [ph_value],
                "turbidity": [turbidity],
            })

            input_encoded = pd.get_dummies(input_df, columns=["id"])

            # Align with model cols
            for col in model_cols:
                if col not in input_encoded.columns:
                    input_encoded[col] = 0
            input_encoded = input_encoded[model_cols]

            # Prediction
            predicted_pollutants = model.predict(input_encoded)[0]
            pollutants = ["O2", "NO3", "NO2", "SO4", "PO4", "CL"]

            st.success(f"✅ Predicted pollutant levels for Station {station_id} in {year_input}:")
            results = {p: val for p, val in zip(pollutants, predicted_pollutants)}

            # Show results in table
            st.table(pd.DataFrame(results, index=["Predicted Level (mg/L)"]))

            # Show results in chart
            st.bar_chart(pd.DataFrame(results, index=["mg/L"]).T)

            if use_dummy:
                st.info("ℹ️ Running in Random mode (using random predictions). Upload your model `.pkl` files for real results.")

# =========================
# About Page
# =========================
elif page == "About":
    st.title("📘 About This App")
    st.markdown(
        """
        This web app is designed for **predicting water pollutant levels** using Machine Learning.  

        ### Features:
        - Predict pollutants based on **year, station ID, and water quality parameters**
        - User-friendly **Streamlit UI**
        - Interactive **charts and tables**
        - Works in **Random Mode** without a trained model  

        👨‍💻 Built with **Python, Streamlit, Pandas, and Joblib**  
        
        ### Technologies Used:
        - Python 3.12
        - Pandas, NumPy – Data handling
        - Scikit-learn – Machine learning model and evaluation
        - Matplotlib, Seaborn – Data visualization
        - Jupyter Notebook – Interactive experimentation
        
        ### Model Performance:
        
        - The model was evaluated using:
        - R² Score
        - Mean Squared Error (MSE)
        - Performance was acceptable across all parameters
        
        
        
        """
    )

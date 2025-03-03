import streamlit as st
import pickle
import numpy as np

# Load the trained model
model = pickle.load(open("smartphone_price_model.pkl", "rb"))

# Streamlit UI
st.title("Smartphone Price Prediction")

# User Inputs
brand = st.selectbox("Select Brand", ["Apple", "Samsung", "OnePlus", "Xiaomi", "Other"])
ram = st.slider("RAM (GB)", 2, 16, 8)
storage = st.slider("Storage (GB)", 32, 512, 128)
battery = st.slider("Battery (mAh)", 2000, 6000, 4000)
camera = st.slider("Camera (MP)", 8, 108, 48)

# Convert Brand to Numerical Value
brand_dict = {"Apple": 1, "Samsung": 2, "OnePlus": 3, "Xiaomi": 4, "Other": 5}
brand_num = brand_dict[brand]

# Make Prediction
if st.button("Predict Price"):
    input_features = np.array([[brand_num, ram, storage, battery, camera]])
    price_prediction = model.predict(input_features)[0]
    st.success(f"Estimated Price: ${price_prediction:.2f}")


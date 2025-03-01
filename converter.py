import streamlit as st
import time

def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {
            "Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000,
            "Miles": 0.000621371, "Yards": 1.09361, "Feet": 3.28084, "Inches": 39.3701
        },
        "Weight": {
            "Kilograms": 1, "Grams": 1000, "Milligrams": 1000000, "Pounds": 2.20462, "Ounces": 35.274
        },
        "Temperature": None,  # Handled separately
        "Time": {
            "Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400
        }
    }
    
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        return value  # If same unit
    
    return (value / conversion_factors[category][from_unit]) * conversion_factors[category][to_unit]

# Streamlit UI
st.set_page_config(page_title="🚀 Smart Unit Converter", layout="centered")
st.markdown("<h1 style='text-align: center; color: #00c9ff;'>🌍 Smart Unit Converter</h1>", unsafe_allow_html=True)
st.write("Convert different units in real-time with ease!")

# Sidebar Category Selection
category = st.sidebar.selectbox("Select a Category", ["Length", "Weight", "Temperature", "Time"])

# Dynamic unit selection based on category
units = {
    "Length": ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"],
    "Weight": ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Time": ["Seconds", "Minutes", "Hours", "Days"]
}

value = st.number_input("Enter Value", min_value=0.0, step=0.1)
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From Unit", units[category])
with col2:
    to_unit = st.selectbox("To Unit", units[category])

if st.button("Convert 🔄"):
    with st.spinner("Converting..."):
        time.sleep(1)  # Fake loading effect
        result = convert_units(value, from_unit, to_unit, category)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

st.markdown("<div style='text-align:center; margin-top:50px; color:grey;'>Made by Safa Aamir 🚀</div>", unsafe_allow_html=True)

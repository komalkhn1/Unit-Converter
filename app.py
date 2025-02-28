import streamlit as st

def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {
            "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371,
            "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
        },
        "Weight": {
            "Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274
        },
        "Temperature": None  # Temperature requires a different formula
    }
    
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # Same unit
    
    factor_from = conversion_factors[category][from_unit]
    factor_to = conversion_factors[category][to_unit]
    return value * (factor_to / factor_from)

st.set_page_config(page_title="Unit Converter", layout="centered")
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .stTitle {
            color: #4CAF50;
        }
        .stButton>button {
            background-color: #008CBA;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📏 Unit Converter</h1>", unsafe_allow_html=True)


categories = ["Length", "Weight", "Temperature"]
category = st.selectbox("Select a category", categories)

if category == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"]
elif category == "Weight":
    units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"]
else:
    units = ["Celsius", "Fahrenheit", "Kelvin"]

from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")

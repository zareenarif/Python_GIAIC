import streamlit as st  # pip install streamlit

# Function to convert units
def Convert_units(values, from_unit, to_unit):
    conversion_formula = {
        "meters": {"kilometers": 0.001, "centimeters": 100, "feet": 3.28084},
        "kilometers": {"meters": 1000, "miles": 0.621371},
        "miles": {"kilometers": 1.60934, "meters": 1609.34},
        "feet": {"meters": 0.3048, "centimeters": 30.48},
        "centimeters": {"meters": 0.01, "feet": 0.0328084},
    }
    if from_unit == to_unit:
        return values
    return values * conversion_formula.get(from_unit, {}).get(to_unit, {})

# Set Page Layout
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")

# Main Title
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🔄 Simple Unit Converter</h1>", unsafe_allow_html=True)

# Sidebar UI
st.sidebar.markdown("## Select Conversion:")
from_unit = st.sidebar.selectbox("Convert From:", ["meters", "kilometers", "miles", "centimeters", "feet"])
to_unit = st.sidebar.selectbox("Convert To:", ["meters", "kilometers", "miles", "centimeters", "feet"])
values = st.sidebar.number_input("Enter Value:", min_value=0.0, format="%.2f")

# Centered Layout for Button & Output
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Convert ✅", help="Click to Convert"):
        result = Convert_units(values, from_unit, to_unit)
        st.success(f"✅ **{values} {from_unit}** = **{result:.4f} {to_unit}**")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)

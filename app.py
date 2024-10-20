import streamlit as st
import math

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Setting up the page design
st.set_page_config(page_title="Temperature Converter", page_icon="🌡️", layout="centered")

# Styling the page with custom CSS for animated button and attractive interface
st.markdown(
    """
    <style>
    body {
        background-color: #f0f4f7;
    }
    .header {
        font-size: 50px;
        text-align: center;
        font-weight: bold;
        color: #FF5733;
    }
    .normal-msg {
        font-size: 30px;
        text-align: center;
        color: #28a745;
        font-weight: bold;
    }
    .convert-btn {
        display: inline-block;
        padding: 15px 30px;
        background-color: #FF5733;
        border-radius: 12px;
        color: white;
        font-size: 18px;
        font-weight: bold;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .convert-btn:hover {
        background-color: #ff3d00;
        transform: scale(1.1);
    }
    </style>
    """, unsafe_allow_html=True
)

# Header for the app
st.markdown('<div class="header">🌡️ Temperature Converter 🌡️</div>', unsafe_allow_html=True)

# Input for temperature value
temperature_value = st.number_input("Enter the temperature value:", step=0.1)

# Option to select the conversion type
conversion_type = st.radio("Select conversion type:", ('Celsius to Fahrenheit', 'Fahrenheit to Celsius'))

# Threshold for comparing float values to avoid precision issues
def is_approximately_equal(val1, val2, threshold=0.01):
    return math.isclose(val1, val2, abs_tol=threshold)

# Perform conversion based on the selection
if st.button('🌡️ Convert Temperature 🌡️'):
    if conversion_type == 'Celsius to Fahrenheit':
        converted_temp = celsius_to_fahrenheit(temperature_value)
        st.write(f"{temperature_value}°C is equal to {converted_temp:.2f}°F")
        # Check if the result is approximately 98.6°F (normal body temperature)
        if is_approximately_equal(converted_temp, 98.6):
            st.markdown('<div class="normal-msg">This is the normal human body temperature!</div>', unsafe_allow_html=True)
    else:
        converted_temp = fahrenheit_to_celsius(temperature_value)
        st.write(f"{temperature_value}°F is equal to {converted_temp:.2f}°C")
        # Check if the result is approximately 37°C (normal body temperature)
        if is_approximately_equal(converted_temp, 37):
            st.markdown('<div class="normal-msg">This is the normal human body temperature!</div>', unsafe_allow_html=True)

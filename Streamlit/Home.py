
import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express 
from PIL import Image
import plotly.figure_factory as ff

# Centered title using HTML and Markdown
st.markdown("<h1 style='text-align: center;'>Forecasting Streetcar Delays</h1>", unsafe_allow_html=True)
st.write("\n")
st.write("\n")

# Set the title of the web app
#st.markdown("<h1 style='text-align: center; color: grey;'>Hello Everyone!</h1>", unsafe_allow_html=True)

#Picture
image = Image.open('/Users/jessicaseo/Documents/Weather_Influenced_TTC_Streetcar_Delay_Prediction/Streamlit/homepage.jpg')

#col1, col2, col3, col4 = st.columns(4)
#with col2:

st.image(image)


# Description Section
st.header(" • Project Objective")
st.write('''Many people rely on public transportation as their only source of travel. 
When public transit experiences unexpected delays or cancellations, it disrupts many passengers' schedules and raises safety concerns. 
With the city expecting the population to grow, how are they preparing to accommodate more passengers when current issues remain unresolved?
This project analyzes Toronto's streetcar delays and their causes to identify delay patterns. 
The goal is to assist commuters in predicting delay severity based on time, route, and weather.''')


#Areas of Impact
st.header(' • Areas of Impact')

#Picture
image = Image.open('Streamlit/General.jpg')

#col1, col2, col3, col4 = st.columns(4)
#with col2:

st.image(image)

# Instructions Section
st.header("• Site Map")

# Sample data
data = {
    "Navigators": ["Home", "About Me", "Discoveries", "Prediction"],
    "Description": ["What is the project?", "Find out the story behind the project", "Explore interesting discoveries from the project", "Join me in predicting streetcar delays"]
}

# Create a DataFrame
table_df = pd.DataFrame(data)

# Display the table
st.table(table_df)

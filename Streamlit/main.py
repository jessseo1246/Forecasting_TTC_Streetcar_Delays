import streamlit as st
import pandas as pd
import joblib


model = joblib.load('best_decision_tree.joblib')
df = pd.read_csv('Streamlit_data.csv')
df2 = pd.read_csv('Capstone_clean_model.csv')

# Set the title of the web app
st.title("Forecasting Streetcar Delays in Toronto")

#Creator
st.write('Created by: Jessica Seo')

st.header("Project Objective")
st.write('''Many people rely on public transportation as their only source of travel. 
When public transit experiences unexpected delays or cancellations, it disrupts many passengers' schedules and raises safety concerns. 
With the city expecting the population to grow, how are they preparing to accommodate more passengers when current issues remain unresolved?
This project analyzes Toronto's streetcar delays and their causes to identify delay patterns. 
The goal is to assist commuters in predicting delay severity based on time, incidents, and weather.''')


#Areas of Impact
st.header('Areas of Impact')
st.write("General Public:")
st.write("Provide transparent information regarding delays and decrease commuters' frustration and answer their core question: 'So how long is this going to take?!'")

st.write("City of Toronto:")
st.write("Regain the reputation of being the best public transit agency in North America, and increase ridership leading to higher fare revenue.")


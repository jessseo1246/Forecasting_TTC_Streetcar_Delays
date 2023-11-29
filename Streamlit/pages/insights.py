import streamlit as st
import pandas as pd
import joblib
import plotly.express as px


model = joblib.load('best_decision_tree.joblib')
df = pd.read_csv('Streamlit_data.csv')
df2 = pd.read_csv('Capstone_clean_model.csv')


fig = px.histogram(df['Hour'], nbins=30, title="Hourly Distribution",
                   labels={"value": "Price"}, color_discrete_sequence=['#DD2E44'])

# Adding more descriptive labels
fig.update_layout(
    xaxis_title="Hour",
    yaxis_title="Number of Delayed",
    title={
        'text': "Hourly Distribution",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    hovermode="x"
)

# Adding hover data
fig.update_traces(hovertemplate='Price: %{x}<br>Count: %{y}')

# Displaying the plot in Streamlit
st.markdown('### Price Distribution Histogram')
st.plotly_chart(fig, use_container_width=True)
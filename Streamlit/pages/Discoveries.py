import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


model = joblib.load('pages/best_decision_tree.joblib')
df = pd.read_csv('pages/Streamlit_data.csv')

# Centered title using HTML and Markdown
st.markdown("<h1 style='text-align: center;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)
st.write("Here are a few interesting discoveries to share from my data analysis.")

################
# Assuming df is your original DataFrame
# Map numerical values to text labels
delay_type_mapping = {0: 'Slight Delay', 1: 'Moderate Delay', 2: 'Severe Delay'}
df['Delay Type'] = df['Min_Delay'].map(delay_type_mapping)

# Calculate counts for each delay type per hour
hourly_counts = df.groupby(['Hour', 'Delay Type']).size().unstack(fill_value=0)
hourly_counts.columns = [f'{col} Count' for col in hourly_counts.columns]
df = df.merge(hourly_counts, on='Hour', how='left')

# Create histogram using text labels for color
fig2 = px.histogram(df, x='Hour', nbins=50,
                    labels={"Delay Type": "Count"}, color='Delay Type',
                    color_discrete_sequence=['#FE9F5D', '#B3D2D1', '#FFD700'],
                    category_orders={"Delay Type": df['Delay Type'].value_counts(ascending=True).index})

# Adding more descriptive labels
fig2.update_layout(
    xaxis_title="Hour",
    yaxis_title="Delayed Frequency",
    title={
        'text': "Which time of the day has the most delay?",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    hovermode="closest"
)

# Update hover data
fig2.update_traces(hovertemplate='Hour: %{x}<br>Slight Delay: %{customdata[0]}<br>Moderate Delay: %{customdata[1]}<br>Severe Delay: %{customdata[2]}',
                   customdata=np.stack([df['Slight Delay Count'], df['Moderate Delay Count'], df['Severe Delay Count']], axis=-1))

# Display the plot in Streamlit
st.plotly_chart(fig2, use_container_width=True)

################
#Delay severity by Weather
test1 = px.scatter(df, x =df.Temperature, y = df.Precipitation, color = df.Min_Delay)

#Adding more descriptive labels
test1.update_layout(
    xaxis_title="Temperature °C",
    yaxis_title="Precipitation mm",
    title={
        'text': "How does the delay severity vary based on weather conditions?",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    hovermode="x"
)

# Adding hover data
test1.update_traces(hovertemplate='Temperature: %{x}<br>Precipitation: %{y}')

# Displaying the plot in Streamlit
st.plotly_chart(test1, use_container_width=True)



#######
# Map numerical values to text labels
delay_type_mapping = {0: 'Slight Delay', 1: 'Moderate Delay', 2: 'Severe Delay'}
df['Delay Type'] = df['Min_Delay'].map(delay_type_mapping)

# Get the top 5 incidents based on value counts
top_incidents = df['Incident'].value_counts().index.tolist()

# Create histogram using text labels for color
graph4 = px.histogram(df, y='Incident', nbins=50,
                      labels={"Delay Type": "Count"}, color='Delay Type',
                      color_discrete_sequence=['#FF7077', '#FFB067', '#ACEEF3'],
                      category_orders={"Delay Type": df['Delay Type'].value_counts(ascending=True).index,
                                       "Incident": top_incidents})

# Adding more descriptive labels
graph4.update_layout(
    xaxis_title="Frequency",
    yaxis_title="Incidents",
    title={
        'text': "Which incident is likely to cause the most delay?",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    hovermode="closest"
)

# Creating separate DataFrames for each delay type
df_slight = df[df['Delay Type'] == 'Slight Delay']
df_moderate = df[df['Delay Type'] == 'Moderate Delay']
df_severe = df[df['Delay Type'] == 'Severe Delay']

# Update hover data
graph4.update_traces(
    hovertemplate='Frequency: %{y}<br>Slight Delay: %{customdata[0]}<br>Moderate Delay: %{customdata[1]}<br>Severe Delay: %{customdata[2]}',
    customdata=np.stack([df['Slight Delay Count'], df['Moderate Delay Count'], df['Severe Delay Count']], axis=-1))

# Displaying the plot in Streamlit
st.plotly_chart(graph4, use_container_width=True)


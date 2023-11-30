import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go


model = joblib.load('best_decision_tree.joblib')
df = pd.read_csv('Streamlit_data.csv')
df2 = pd.read_csv('Capstone_clean_model.csv')

# Centered title using HTML and Markdown
st.markdown("<h1 style='text-align: center;'>Exploratory Data Analysis</h1>", unsafe_allow_html=True)
st.write("Here are a few interesting discoveries to share from my data analysis.")



# Map numerical values to text labels
delay_type_mapping = {0: 'Slight Delay', 1: 'Moderate Delay', 2: 'Severe Delay'}
df['Delay Type'] = df['Min_Delay'].map(delay_type_mapping)

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
# Creating separate DataFrames for each delay type
df_slight = df[df['Delay Type'] == 'Slight Delay']
df_moderate = df[df['Delay Type'] == 'Moderate Delay']
df_severe = df[df['Delay Type'] == 'Severe Delay']

# Adding hover data
fig2.update_traces(hovertemplate='Hour: %{x}<br>Slight Delay: %{y}<br>Moderate Delay: %{y}<br>Severe Delay: %{y}')

# Displaying the plot in Streamlit
st.plotly_chart(fig2, use_container_width=True)





#Delay Frequency by Hour
delay_type_mapping = {0: 'Slight Delay', 1: 'Moderate Delay', 2: 'Severe Delay'}
df['Delay Type'] = df['Min_Delay'].map(delay_type_mapping)

# Create count plot using Plotly Express
fig = px.histogram(df, x='Hour', color='Delay Type', barmode='group',
                   labels={'Hour': 'Hour', 'Delay Type': 'Delay Type'},
                   category_orders={'Delay Type': sorted(df['Delay Type'].unique())},
                   color_discrete_sequence=['#FE9F5D', '#B3D2D1', '#FFD700'])

#Adding more descriptive labels
fig.update_layout(
    xaxis_title="Hour",
    yaxis_title="Delay Frequncy",
    title={
        'text': "Which time of the day has the most delay?",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    hovermode="x"
)

# Update layout for better visualization
fig.update_layout(title_text='Which time of the day has the most delay?', barmode='group')

# Displaying the plot in Streamlit
st.plotly_chart(fig, use_container_width=True)




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





graph3 = px.bar(df['Incident'].value_counts().head(10),
             orientation='h',
             labels={'value': 'Frequency', 'index': 'Incidents'},
             color_discrete_sequence=['#DD2E44'])

# Adding more descriptive labels
graph3.update_layout(
    xaxis_title="Frequency",
    yaxis_title="Incidents",
    title={
        'text': "Which incident is likely to occur the most delay?",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    hovermode="x"
)

# Adding hover data
#graph3.update_traces(hovertemplate='Price: %{x}<br>Count: %{y}')

# Displaying the plot in Streamlit
st.plotly_chart(graph3, use_container_width=True)
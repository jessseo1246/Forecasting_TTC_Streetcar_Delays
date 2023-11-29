import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go


model = joblib.load('best_decision_tree.joblib')
df = pd.read_csv('Streamlit_data.csv')
df2 = pd.read_csv('Capstone_clean_model.csv')



if st.sidebar.expander('Show Filters'):
    #dropdown sections (weather, month, hour, line)
    selected_weather = st.sidebar.selectbox('Select Weather', df['Weather'].unique())

    unique_months =df['Month'].unique()
    sorted_months =sorted(unique_months)

    selected_months =st.sidebar.selectbox('Select Month', sorted_months)

    unique_hour =df['Hour'].unique()
    sorted_hours =sorted(unique_hour)

    selected_hours =st.sidebar.selectbox('Select Hour', sorted_hours)

    sorted_lines = df['Line'].value_counts().index.tolist()
    selected_line = st.sidebar.selectbox('Select Line', sorted_lines)





# functon to make prediction
@st.cache
def predict_probability(features):
        # Process the features as needed
        
        # Example: Convert the input dictionary into a DataFrame
        input_data = pd.DataFrame([features])

        # Predict probabilities using the loaded model
        probabilities = pd.DataFrame(model.predict_proba(input_data), columns=model.classes_)
        return probabilities


if st.sidebar.button('Predict'):
 
    # Display results of the NLP task
    st.header("Prediction")
    

    cloudy = 1 if selected_weather == 'Cloudy' else 0
    rain = 1 if selected_weather == 'Rain' else 0
    HeavySnow = 1 if selected_weather == 'Heavy Snow' else 0
    ModerateRain = 1 if selected_weather == 'Moderate Rain' else 0
    Fog = 1 if selected_weather == 'Fog' else 0
    FreezingRain = 1 if selected_weather == 'Freezing Rain' else 0
    Haze= 1 if selected_weather == 'Haze' else 0
    HeavyRain = 1 if selected_weather == 'Heavy Rain' else 0
    Thunderstorms = 1 if selected_weather == 'Thunderstorms' else 0
    Snow = 1 if selected_weather == 'Snow' else 0
    ModerateSnow = 1 if selected_weather == 'Moderate Snow' else 0
    # Combine selected features with input values
    # Original feature names list
    feature_names_list = [
        'Temperature', 'Precipitation', 'Summer_PT', 'Winter_PT', 'Day', 'Line', 'Year', 'Month', 'Date', 'Hour', 'Minute',
        'Weather_Cloudy', 'Weather_Fog', 'Weather_Freezing Rain', 'Weather_Haze', 'Weather_Heavy Rain', 'Weather_Heavy Snow',
        'Weather_Moderate Rain', 'Weather_Moderate Snow', 'Weather_Rain', 'Weather_Snow', 'Weather_Thunderstorms',
        'Incident_Collision - TTC Involved', 'Incident_Diversion', 'Incident_Emergency Services', 'Incident_General Delay',
        'Incident_Held By', 'Incident_Investigation', 'Incident_Late', 'Incident_Late Entering Service',
        'Incident_Late Leaving Garage', 'Incident_Management', 'Incident_Mechanical', 'Incident_Operations',
        'Incident_Overhead', 'Incident_Rail/Switches', 'Incident_Security', 'Incident_Utilized Off Route'
    ]

    # Provided dictionary to be sorted
    provided_dict = {
        'Line': selected_line,
        'Hour': selected_hours,
        'Incident_Operations': 0,
        'Year': 2023,
        'Incident_Diversion': 0,
        'Incident_Held By': 0,
        'Month': selected_months,
        'Incident_General Delay': 1,
        'Day': 1,
        'Temperature': 10,
        'Date': 1,
        'Minute': 30,
        'Incident_Emergency Services': 0,
        'Incident_Security': 0,
        'Weather_Cloudy': cloudy,
        'Weather_Rain': rain,
        'Precipitation': 0.0,
        'Weather_Heavy Snow': HeavySnow,
        'Incident_Late': 0,
        'Summer_PT': 0,
        'Incident_Rail/Switches': 0,
        'Incident_Overhead': 0,
        'Winter_PT': 0,
        'Incident_Mechanical': 0,
        'Incident_Management': 0,
        'Incident_Late Leaving Garage': 0,
        'Incident_Late Entering Service': 0,
        'Incident_Investigation': 0,
        'Weather_Moderate Rain': ModerateRain,
        'Weather_Fog': Fog,
        'Weather_Freezing Rain': FreezingRain,
        'Weather_Haze': Haze,
        'Weather_Heavy Rain': HeavyRain,
        'Incident_Collision - TTC Involved': 0,
        'Weather_Thunderstorms': Thunderstorms,
        'Weather_Snow': Snow,
        'Weather_Moderate Snow': ModerateSnow,
        'Incident_Utilized Off Route': 0
    }

    # Create a new dictionary with the same keys but in the order specified by feature_names_list
    sorted_dict = {feature: provided_dict[feature] for feature in feature_names_list}


    # Predict probabilities
    probabilities = predict_probability(sorted_dict)
        
   # Get the category names and probabilities
    category_names = probabilities.columns.tolist()  # Get column names as category names
    prob_values = probabilities.iloc[0].values  # Extract the values from the first row

    # Divide the layout into a 2x2 grid
    col1, col2 = st.columns(2)

                # Display probabilities in a 2x2 grid of gauge charts
    for i, (category, prob_value) in enumerate(zip(category_names, prob_values * 100)):
        if i < 2:
            col = col1
        else:
            col = col2
            
        with col:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=prob_value,
                title={'text': f"% Probability of {category}"},
                gauge={'axis': {'range': [0, 100]}, 'bar': {'color': '#4a7ba6'}},
            ))
            st.plotly_chart(fig, use_container_width=True)
    
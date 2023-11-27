<div align="center">
  <h1> Exploring TTC Streetcar Delays and Forecasting Delays </h1>
</div>

### 🚂 Project Objectives 

Many people rely on public transportation as their only source of travel. When public transit experiences unexpected delays or cancellations, it disrupts many passengers' schedules and raises safety concerns. With the city expecting the population to grow, how are they preparing to accommodate more passengers when current issues remain unresolved?

This project analyzes Toronto's streetcar delays and their causes to identify delay patterns. The goal is to assist commuters in predicting delay severity based on time, incidents, and weather.

### 📈 Areas of Impact 

**General Public**:   
Provide transparent information regarding delays and decrease commuters' frustration and answer their core question: *'So how long is this going to take?!*  
**City of Toronto**:  
Regain the reputation of being the [best public transit agency](https://www.ttc.ca/news/2017/June/TTC-named-North-Americas-best-transit-agency-for-2017#:~:text=The%20TTC%20has%20been%20named,of%20the%20people%20of%20Toronto) in North America, and increase ridership leading to higher fare revenue.  

### 🏄🏼‍♂️ Project Workflow:

1. Data loading, scraping, and merging 
2. Data Preprocessing and EDA
3. Baseline modelling
4. Advanced modelling
5. Saving cleaned dataset and machine learning models

### 🔍 Project Structure  
**Data**: Datasets used for analysis/modeling and links to references.    
**Notebooks**: Detailed project analysis.   
**Models**: Models created in notebooks.   
**Docs**: Additional documents such as presentation slides and streamlit.

### ⚙️ Data Resources 
The datasets used in this project are collected from the [City of Toronto's Open Data](https://open.toronto.ca/dataset/ttc-streetcar-delay-data/) and [Environment Canada](https://climate.weather.gc.ca/climate_data/hourly_data_e.html?hlyRange=2009-12-10%7C2023-10-03&dlyRange=2010-02-02%7C2023-10-02&mlyRange=%7C&StationID=48549&Prov=ON&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=2022&EndYear=2023&selRowPerPage=25&Line=179&lstProvince=ON&timeframe=1&time=LST&time=LST&Year=2021&Month=1&Day=13#). Weather data is scraped from multiple URL links with the necessary permissions. After gathering these two separate datasets, they are merged to commence the analysis. 

**Data Dictionary**  

| Column | Description |
| --- | --- |
| Datetime | Date and time of when weather data and streetcar delay was recorded between Jan 01, 2021 to Sept 30, 2023 |
| Temperature | Atmostpheric temperature in degrees Celsius per hour |
| Precipitation | Precipitation amount stored in mm per hour |
| Summer_PT | Percieved temperature in Summer to indicate hot temperature per hour |
| Winter_PT | Percieved temperature in Winter to indicate cold temperature per hour |
| Wind_Speed | Wind Speed km per hour |
| Visibility | Visibility of weather atmosphere in km per hour |
| Weather | Observations of atmospheric phenomenon |
| Time | When the delay causing incident occurred |
| Day | The name of the day |
| Min Delay | The actual delay minutes |
| Min Gap | The total scheduled time in minutes between the streetcar in front and the following streetcar | 
| Route | The number of streetcar route | 
| Line | Streetcar number | 
| Veicle | Vehicle number | 
| Location | The location of the delay | 
| Incident | The description of the delay causing incident | 

### Contributer
Jessica 


<div align="center">
  <h1> Exploring the Influence of Weather on TTC Streetcar Delays and Forecasting Delays </h1>
</div>

### 🚂Project Objectives:


Many people rely on public transportation as their only source of travel. When public transit experiences unexpected delays or cancellations, it disrupts many passengers' schedules and raises safety concerns. With the city expecting the population to grow, how are they preparing to accommodate more passengers when current issues remain unresolved?

This project analyzes Toronto's streetcar delays and their causes, as well as the influence of weather conditions, to identify delay patterns. The goal is to provide commuters with accurate information about upcoming streetcar delays.

### 🚂Data Resources:

The datasets used in this project are collected from the City of Toronto's Open Data platform and Environment Canada. Weather data is scraped from multiple URL links with the necessary permissions. After gathering these two separate datasets, they are merged to commence the analysis. The resulting dataset consists of 42,265 rows and 15 columns.

[Datasets](https://drive.google.com/drive/folders/1ldtAjMVd1zzPN4EjZbrB1EyqPUVLt3ue?usp=sharing): 
- TTC dataset: 2021 Jan.01 - 2023. Sept.30
- Weather dataset: 2021 Jan.01 - 2023 Sept.30


### 🚂Data Dictionary¶:

- _Datetime: Date and time of when weather data and streetcar delay was recorded between January, 01, 2021 to September 30, 2023._

- _Temperature: Atmostpheric temperature in degrees Celsius._
- _Precipitation : Precipitation amount stored in mm._
- _Summer_PT : Percieved temperature in Summer to indicate hot temperature._
- _Winter_PT : Percieved temperature in Winter to indicate cold temperature._
- _Wind_Speed : Wind Speed km per hour._
- _Visibility : Visibility of weather atmosphere in km._
- _Weather : Observations of atmospheric phenomenon._

- _Time: When the delay causing incident occurred._
- _Day: The name of the day._
- _Min Delay : The actual delay minutes._
- _Min Gap : The total scheduled time in minutes between the streetcar in front and the following streetcar._

- _Route : The number of streetcar route._
- _Line : Streetcar number._
- _Location : The location of the delay._
- _Incident : The description of the delay causing incident._

### 🚂Project Organization:

1. Data preparation, preprocessing, and EDA.
2. Data spliting and modelling.
3. Advanced modelling.

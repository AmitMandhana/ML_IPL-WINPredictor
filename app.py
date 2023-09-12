import os
import pickle
import streamlit as st
import pandas as pd


# Get the current working directory
current_dir = os.getcwd()

# Set the path to the pickle file (assuming it's in the same directory)
pickle_file_path = r'C:\Users\BISHNU KANTA\PycharmProjects\FIRSTAPP\pipe.pkl'


# Load the pickled model
with open(pickle_file_path, 'rb') as model_file:
    loaded_pipe = pickle.load(model_file)

# Teams and cities
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 'Kolkata Knight Riders',
         'Kings XI Punjab', 'Chennai Super Kings', 'Rajasthan Royals', 'Delhi Capitals']
cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Kolkata', 'Chandigarh', 'Chennai', 'Jaipur', 'Delhi']

# User inputs
st.sidebar.header('Input Parameters')
batting_team = st.sidebar.selectbox('Select the batting team', sorted(teams))
bowling_team = st.sidebar.selectbox('Select the bowling team', sorted(teams))
selected_city = st.sidebar.selectbox('Select host city', sorted(cities))
target = st.sidebar.number_input('Target')

score = st.sidebar.number_input('Score')
overs = st.sidebar.number_input('Overs completed')
wickets = st.sidebar.number_input('Wickets out')

# Calculate match parameters
runs_left = target - score
balls_left = 120 - (overs * 6)
wickets_left = 10 - wickets
# Calculate match parameters
if overs != 0:
    crr = score / overs
else:
    crr = 0

rrr = (runs_left * 6) / balls_left


input_data = pd.DataFrame({'batting_team': [batting_team],
                           'bowling_team': [bowling_team],
                           'city': [selected_city],
                           'runs_left': [runs_left],
                           'balls_left': [balls_left],
                           'wickets_left': [wickets_left],
                           'total_runs_x': [target],
                           'crr': [crr],
                           'rrr': [rrr]})

# Make prediction
result = pipe.predict_proba(input_data)
win_probability = round(result[0][1] * 100, 2)
lose_probability = round(result[0][0] * 100, 2)

# Display results
st.header(f"{batting_team} - {win_probability}%")
st.header(f"{bowling_team} - {lose_probability}%")

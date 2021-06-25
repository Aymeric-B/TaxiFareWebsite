import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Here you can predict your taxi fare in New York City
''')




d = st.date_input(
    "When do you want to take a cab?",
    datetime.date.today())

pickup_long = st.number_input('pickup longitude')
pickup_lat = st.number_input('pickup latitude')
dropoff_long = st.number_input('dropoff longitude')
dropoff_lat = st.number_input('dropoff latitude')

n_passengers = st.selectbox('Number of passengers', list(range(1,11)))




url = 'https://first-gcloud-image-ie3w56pnxa-ew.a.run.app/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')




# the pipeline expects an object, not a datetime
formatted_pickup_datetime = d.strftime("%Y-%m-%d %H:%M:%S")

params = {
    "pickup_datetime" : str(formatted_pickup_datetime),
    "pickup_longitude" : str(pickup_long),
    "pickup_latitude" : str(pickup_lat),
    "dropoff_longitude" : str(dropoff_long),
    "dropoff_latitude" : str(dropoff_lat),
    "passenger_count" : str(n_passengers)
}



if st.button('Give me the price'):
    response = requests.get(url, params=params).json()
    price = '{:,.2f}'.format(response['prediction'])
    st.write(f"Expected price : {price} $")
else :
    st.write("Waiting for your question")


st.write("Yahouuuu new")
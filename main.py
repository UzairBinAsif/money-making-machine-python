import streamlit as st
import random
import time
import requests

st.title('Money Making Machine')

def generate_money():
    return random.randint(1, 1000)

st.subheader('Instant Cash Generator')

if st.button('Generate Money'):
    st.write('Counting your money...')
    time.sleep(random.randint(1,5))
    amount = generate_money()
    st.success(f'You made ${amount}')

def fetch_side_hustles():
    try:
        res = requests.get('http://127.0.0.1:8000/side_hustles?apiKey=181278')
        if res.status_code == 200:
            hustles = res.json()
            return hustles['side_hustle']
        else:
            return 'Freelancing'
    except:
        return 'Something Went Wrong!'

st.subheader('Side Hustle Ideas')

if st.button('Generate Hustle'):
    idea = fetch_side_hustles()
    st.info(idea) #st.warning, st.success

def fetch_money_quotes():
    try:
        res = requests.get('http://127.0.0.1:8000/money_quotes?apiKey=181278')
        if res.status_code == 200:
            quotes = res.json()
            return quotes['money_quote']
        else:
            return ('Money is the root of all evil!')
    except:
        return 'Something Went Wrong!'
st.subheader('Money Making Motivation')
if st.button('Generate Quote'):
    quote = fetch_money_quotes()
    st.info(quote)
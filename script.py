import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
API_KEY = os.environ.get('API_KEY')

BASE_URL = 'https://api.ouraring.com/v2/usercollection/'

HEADERS = {
    'Authorization': f'Bearer {API_KEY}'
}

def get_sleep_data(start_date=None, end_date=None):
    url = BASE_URL + 'daily_sleep'
    params = {}
    if start_date:
        params['start_date'] = start_date
    if end_date:
        params['end_date'] = end_date

    response = requests.request('GET',url, headers=HEADERS, params=params)
    return json.loads(response.text)

def get_activity_data(start_date=None, end_date=None):
    url = BASE_URL + 'daily_activity'
    params = {}
    if start_date:
        params['start_date'] = start_date
    if end_date:
        params['end_date'] = end_date

    response = requests.request('GET', url, headers=HEADERS, params=params)
    return json.loads(response.text)

# Example usage:
print("-----------------------------------------------------------------------------------")
print("----------------------------------DATASET SLEEP------------------------------------")
print("-----------------------------------------------------------------------------------")
sleep_data = get_sleep_data('2023-09-24', '2023-09-29')
print(sleep_data)

print("-----------------------------------------------------------------------------------")
print("---------------------------------DATASET ACTIVITY----------------------------------")
print("-----------------------------------------------------------------------------------")

activity_data = get_activity_data('2023-09-24', '2023-09-29')
print(activity_data)

print("-----------------------------------------------------------------------------------")
print("--------------------------------DATES GRABBED SLEEP--------------------------------")
print("-----------------------------------------------------------------------------------")

for item in sleep_data['data']:
    print(item['timestamp'])

print("-----------------------------------------------------------------------------------")
print("-------------------------------DATES GRABBED ACTIVITY------------------------------")
print("-----------------------------------------------------------------------------------")

for item in activity_data['data']:
    print(item['timestamp'])
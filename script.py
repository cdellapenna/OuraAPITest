import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get('API_KEY')

BASE_URL = 'https://api.ouraring.com/v1/'

HEADERS = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def get_sleep_data(start_date=None, end_date=None):
    url = BASE_URL + 'sleep'
    params = {}
    if start_date:
        params['start'] = start_date
    if end_date:
        params['end'] = end_date

    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

def get_activity_data(start_date=None, end_date=None):
    url = BASE_URL + 'activity'
    params = {}
    if start_date:
        params['start'] = start_date
    if end_date:
        params['end'] = end_date

    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

# Example usage:
sleep_data = get_sleep_data('2023-09-01', '2023-09-28')
print(sleep_data)

print("------------------------------------------------------------------------")

activity_data = get_activity_data('2023-09-01', '2023-09-28')
print(activity_data)
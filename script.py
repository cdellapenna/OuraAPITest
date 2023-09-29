import requests
import os
from dotenv import load_dotenv

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
    return response.text

def get_activity_data(start_date=None, end_date=None):
    url = BASE_URL + 'daily_activity'
    params = {}
    if start_date:
        params['start_date'] = start_date
    if end_date:
        params['end_date'] = end_date

    response = requests.request('GET', url, headers=HEADERS, params=params)
    return response.text

# Example usage:
sleep_data = get_sleep_data('2023-09-25', '2023-09-29')
print(sleep_data)

print("-----------------------------------------------------------------------------------")
print("-------------------------------SPACER FOR VISUAL AID-------------------------------")
print("-------------------------------SPACER FOR VISUAL AID-------------------------------")
print("-----------------------------------------------------------------------------------")

activity_data = get_activity_data('2023-09-25', '2023-09-29')
print(activity_data)
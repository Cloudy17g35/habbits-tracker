import requests
from datetime import datetime
from src.endpoints import  graphs_endpoint
from src.authentication import get_headers
date_format = 'yyyyMMdd'
current_date = datetime.now().strftime('%Y%m%d')

def post_pixel():
    graph_id = input('Please provide graph id:> ')
    endpoint = f'{graphs_endpoint}/{graph_id}'
    # quantity and date is required
    pixel_params = {
        # date in yyyyMMdd format
        'date': input('Please provide date in yyyyMMdd format (leave Null to keep current date):> ') or current_date,
        'quantity': input('Please provide quantity registered on date you provided:> ')
    }
    headers = get_headers()
    response = requests.post(endpoint,json=pixel_params, headers=headers)
    if not response.ok:
        print('Something went wrong!')
    print(response.text)


def get_pixel():
    graph_id = input('Please provide graph id:> ')
    date = input('Please provide date in yyyyMMdd format (leave Null to keep current date):> ') or current_date
    endpoint = f'{graphs_endpoint}/{graph_id}/{date}'
    headers = get_headers()
    response = requests.get(endpoint, headers=headers)
    if not response.ok:
        print('Something went wrong!')
    print(response.text)


def update_pixel():
    graph_id = input('Please provide graph id for:> ')
    date = input('Please provide date in yyyyMMdd format (leave Null to keep current date):> ') or current_date
    endpoint = f'{graphs_endpoint}/{graph_id}/{date}'
    pixel_params = {
        'quantity': input('Please provide new quantity:> ')
    }
    headers = get_headers()
    response = requests.put(endpoint, headers=headers, json=pixel_params)
    if not response.ok:
        print('Something went wrong!')
    print(response.text)


def delete_pixel():
    graph_id = input('Please provide graph id:> ')
    date = input('Please provide date in yyyyMMdd format (leave Null to keep current date):> ') or current_date
    endpoint = f'{graphs_endpoint}/{graph_id}/{date}'
    headers = get_headers()
    response = requests.delete(endpoint, headers=headers)
    if not response.ok:
        print('Something went wrong!')
    print(response.text)
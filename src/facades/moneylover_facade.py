import requests
import re
from dotenv import load_dotenv
import os

class Moneylover:

    def __init__(self) -> None:
        load_dotenv()
        
        self.email = os.getenv('EMAIL')
        self.password = os.getenv('PASSWORD')
        self.base_url = os.getenv('BASE_URL')

    def validate_error(self, response_json):
        if 'error' in response_json and response_json['error'] != 0:
            raise ValueError(
                f"Error {response_json['error']}: {response_json['msg']}")
        return False

    def get_token(self):
        # Step 1: Get the login URL
        login_url_response = requests.post(self.base_url + '/user/login-url')
        login_url_response_json = login_url_response.json()

        # Extract request_token and client from login URL
        request_token = login_url_response_json['data']['request_token']
        login_url = login_url_response_json['data']['login_url']
        client_match = re.search(r'client=(.+?)&', login_url)

        if not client_match:
            raise ValueError("Client not found in login URL")

        client = client_match.group(1)

        # Step 2: Request the token
        headers = {
            'authorization': f'Bearer {request_token}',
            'client': client
        }
        body = {
            'email': self.email,
            'password': self.password
        }
        token_response = requests.post(
            'https://oauth.moneylover.me/token', headers=headers, json=body)
        token_response_json = token_response.json()

        if 'access_token' not in token_response_json:
            raise ValueError("Access token not found in response")

        return token_response_json['access_token']

    def get_wallets(self):

        # Headers including the authorization token
        headers = {
            'authorization': f'AuthJWT ' + str(self.get_token())
        }
        # Make the request to get wallets
        response = requests.post(
            self.base_url + '/wallet/list', headers=headers)

        # Parse the JSON response
        wallets_response_json = response.json()

        self.validate_error(wallets_response_json)

        # if 'error' in wallets_response_json and wallets_response_json['error'] != 0:
        #     raise ValueError(
        #         f"Error {wallets_response_json['error']}: {wallets_response_json['msg']}")

        return wallets_response_json['data']

    def get_transactions(self, start_date, end_date):
        headers = {
            'authorization': f'AuthJWT ' + str(self.get_token())
        }

        body = {
            'startDate': start_date,
            'endDate': end_date,
            'walletId': 'all'
        }

        response = requests.post(
            self.base_url + '/transaction/list', headers=headers, json=body)

        transactions_response_json = response.json()

        self.validate_error(transactions_response_json)

        return transactions_response_json['data']['transactions']
    # The endpoint only works per wallet id. The 'all' parameter does not work
    def get_categories(self, wallet_id):
        headers = {
            'authorization': f'AuthJWT ' + str(self.get_token()),
            'content-type': 'application/x-www-form-urlencoded'
        }

        body = {
            'walletId': wallet_id
        }

        response = requests.post(
            self.base_url + '/category/list', headers=headers, data=body)

        categories_response_json = response.json()

        self.validate_error(categories_response_json)

        return categories_response_json['data']

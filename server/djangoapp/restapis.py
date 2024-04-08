import os
import requests
from requests.exceptions import RequestException
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Define backend and sentiment analyzer URLs
backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url', default="http://localhost:5050/"
)

# Define the get_request function
def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params += f"{key}={value}&"

    request_url = f"{backend_url}{endpoint}?{params}"
    print(f"GET from {request_url}")

    try:
        response = requests.get(request_url)
        return response.json()
    except RequestException as e:
        print(f"Network exception occurred: {e}")

# Define the analyze_review_sentiments function
def analyze_review_sentiments(text):
    request_url = f"{sentiment_analyzer_url}/analyze/{text}"
    try:
        response = requests.get(request_url)
        return response.json()
    except RequestException as e:
        print(f"Unexpected error: {e}")

# Define the post_review function
def post_review(data_dict):
    request_url = f"{backend_url}/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except RequestException as e:
        print(f"Network exception occurred: {e}")

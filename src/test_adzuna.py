import os
import requests
from dotenv import load_dotenv

load_dotenv()
id = os.getenv('ADZUNA_APP_ID')
key = os.getenv('ADZUNA_APP_KEY')
url = "https://api.adzuna.com/v1/api/jobs/in/search/1"
parameters = {'app_id': id, 'app_key' :key, 'what' : 'data scientist', 'results_per_page' : 5}
response = requests.get(url, params = parameters)
print(response.status_code)
print(response.json())
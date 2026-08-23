import os
import requests
from dotenv import load_dotenv

load_dotenv()
id = os.getenv('ADZUNA_APP_ID')
key = os.getenv('ADZUNA_APP_KEY')
url = "https://api.adzuna.com/v1/api/jobs/in/search/1"
parameters = {'app_id': id, 'app_key' :key, 'what' : 'data scientist', 'results_per_page' : 10}
response = requests.get(url, params = parameters)

data= response.json()
'''print(response.status_code)
print(response.json())

print(type(data))
print(data.keys())
print(len(data['results']))
print(data['results'][0].keys())

print(type(data['results'][0]['company']))
print(data['results'][0]['company'])
print(type(data['results'][0]['location']))
print((data['results'][0]['location']))

print(data["results"][0]["category"])
print(data["results"][0]["contract_type"])
print(data["results"][0]["contract_time"])
print(data["results"][0]["salary_is_predicted"])'''

jobs = data['results']
'''for job in jobs:
    print(job['id'])

jobs = data["results"]

ids = []

for job in jobs:
    ids.append(job["id"])

print("Total jobs:", len(jobs))
print("Unique IDs:", len(set(ids)))
print("Duplicate IDs:",len(jobs) - len(set(ids)))'''


'''count = 0
for job in jobs:
    if job["title"]:
        count += 1

print(count)'''



fields = [
    "id",
    "title",
    "company",
    "location",
    "category",
    "contract_type",
    "contract_time",
    "latitude",
    "longitude",
    "description",
]

'''for field in fields:
    count = 0

    for job in jobs:
        if field in job:
            count += 1
    percent = float((count/len(jobs)) * 100)

    print(field, count, percent,'%')'''



'''count = 0
for job in jobs:
    a = job.get('latitude')
    if a is None:
        count += 1

print(count)'''

# above was just learning

'''for field in fields:
    present_count = 0
    missing_count = 0

    for job in jobs:
        value = job.get(field)

        if value is None:
            missing_count += 1
        else:
            present_count += 1

    percent = (present_count / len(jobs)) * 100

    print(
        field,
        "present:", present_count,
        "missing:", missing_count,
        "completeness:", percent
    )


contract_type = []
contract_time = []

for job in jobs:
    type_value = job.get('contract_type')
    time_value = job.get('contract_time')

    if type_value is not None:
        contract_type.append(type_value)

    if time_value is not None:
        contract_time.append(time_value)

print(f'contract_type: unique count- {len(set(contract_type))} value- {set(contract_type)}')
print(f'contract_time: unique count- {len(set(contract_time))} value- {set(contract_time)}')



for job in jobs:
    company = job.get("company")
    category = job.get("category")
    location = job.get("location")

    if company is not None:
        print(company)

    if location is not None:
            print(location)

    if category is not None:
            print(category)'''
    


    
for job in jobs:
    print(job.get("salary_min"))
    print(job.get("salary_max"))
    print(job.get("salary_is_predicted"))
    print("---")
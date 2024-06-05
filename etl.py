import pandas as pd
import sqlalchemy
import requests


response = requests.get('https://api.restful-api.dev/objects')

if response.status_code == 200:
    print("API request successful")
else:
    print("API request failed")

print(response.headers.get("Content-Type"))

data = response.json()
    
df = pd.DataFrame(data)
    

df.to_csv('output.csv', index=False)

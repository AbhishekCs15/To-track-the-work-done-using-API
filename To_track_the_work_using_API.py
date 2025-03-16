import requests
from datetime import datetime

url = "https://pixe.la/v1/users"
USER_NAME = "your_own"
TOKEN = "your_own"
# headers is created for secure user connection(authentication)
headers = {
    "X-USER-TOKEN": TOKEN,
}


# TO CREATE ACCOUNT IN PIXEL(API PROVIDER)
params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# post = requests.post(url=url,json=params)
# print(post.text)


# TO CREATE GRAPH
end_point = f"{url}/{USER_NAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Coding",
    "unit": "Hour",
    "type": "float",
    "color": "momiji",
    # "timezone": "5:30",
}
# response = requests.post(url=end_point, json=graph_config, headers=headers) #headers is for secure connection
# print(response.text)


# TO ADD VALUE TO GRAPH
first_update = f"{end_point}/graph1"
today = datetime.now()
data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input(f"How many hours did you code/read Today({today.strftime("%Y-%m-%d")}):")
}
response = requests.post(url=first_update, headers=headers, json=data)
print(response.text)


# TO UPDATE VALUE IN GRAPH USING put METHOD
updated_data = {
    "quantity": "1"
}
# response = requests.put(url=f"{first_update}/20250123", headers=headers, json=updated_data)
# print(response.text)


# TO DELETE VALUE FROM GRAPH USING delete METHOD
# response = requests.delete(url=f"{first_update}/20250123", headers=headers)
# print(response.text)

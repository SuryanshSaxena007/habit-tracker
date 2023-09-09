import requests
from datetime import datetime
USER = "suryansh"
TOKEN = "lkiuyjt5rewq"
pixela_endpoint = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"


user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixel_endpoint, json=user_params)
# print(response.text)



graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_create_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_config = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many kilometers did you ride today ?\n")
}

response = requests.post(url=pixel_create_endpoint, json=pixel_config, headers=headers)
print(response.text)

# pixel_update_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#
# p_update_config = {
#     "quantity": "5.4"
# }

# response = requests.put(url=pixel_update_endpoint, json=p_update_config, headers=headers)
# print(response.text)


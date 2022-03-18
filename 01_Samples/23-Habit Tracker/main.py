import requests
import datetime

PIXELA_EP = "https://pixe.la/v1/users"
TOKEN = "wishesqazwsxedc@99"
USERNAME = "skandan"
GRAPH_ID = "graph1"

GRAPH_EP = f"{PIXELA_EP}/{USERNAME}/graphs"
DATA_EP = f"{GRAPH_EP}/{GRAPH_ID}"

parameters = {
     "token": TOKEN,
     "username": USERNAME,
     "agreeTermsOfService": "yes",
     "notMinor": "yes",
}
# response = requests.post(url=PIXELA_EP, json=parameters)
# # response.raise_for_status()
# print(response.text)
graph_params ={
     "id": "graph1",
     "name": "Lines Of Code",
     "unit": "LOC",
     "type": "int",
     "color": "shibafu",
}
headers ={
     "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=GRAPH_EP, json=graph_params, headers=headers)
# response.raise_for_status()
# print(response.text)
# data = {
#      "date": datetime.datetime.now().strftime("%Y%m%d"),
#      "quantity": "200",
# }
#
# response = requests.post(url=DATA_EP, headers=headers, json=data)
# print(response.text)

# data = {
#      "quantity": "500",
# }
# mod_date = datetime.datetime.now().strftime("%Y%m%d")
# GRAPH_PUT_EP = f"{DATA_EP}/{mod_date}"
# response = requests.put(url=GRAPH_PUT_EP, headers=headers, json=data)
# print(response.text)

mod_date = datetime.datetime(year=2022, month=3, day=17)
mod_date = mod_date.strftime("%Y%m%d")
GRAPH_DELETE_EP = f"{DATA_EP}/{mod_date}"
response = requests.delete(url=GRAPH_DELETE_EP, headers=headers)
print(response.text)
import requests

BASE = "http://127.0.0.1:5000/"
# response = requests.put(BASE + "videos/2", {"name": "bahubali2 movie", "views":100000, "likes": 250})
# response = requests.get(BASE + "videos/6")

data = [{"name": "bahubali2 movie", "views":100000, "likes": 250}, {"name": "pushpa", "views": 50000, "likes": 30}]
for i in range(len(data)):
    response = requests.put(BASE + "videos/" + str(i), data[i])
    print(response.json())
response = requests.delete(BASE + "videos/0")
print(response)
response = requests.get(BASE + "videos/1")
print(response.json())

import requests

response = requests.post('http://10.2.0.2:5000/api/getMostReleventRooms')
print(response.status_code)

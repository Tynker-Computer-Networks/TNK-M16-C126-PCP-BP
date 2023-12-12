import requests

# Create a loop on variable i from 1 to 5000

# Check following URL for different id's from 1-5000
URL = f"http://ec2-3-108-196-161.ap-south-1.compute.amazonaws.com/api/get-customer?id=1"
r = requests.get(url=URL)
if r.status_code == 200:
    print(URL)
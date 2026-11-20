import httpx
import random

base_url = "https://dummyjson.com/"


#trying to get it to return the number of products which mention "apple"
content = "products/search?title=Apple"  # API request

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

print(content)

import httpx
import random
import matplotlib.pyplot as plt

base_url = "https://dummyjson.com/"


#trying to get it to return the number of products which mention "apple"
content = "recipe/meal-type/snack"  # API request

url = base_url + content  # API request

response = httpx.get(url)   # API call

print(response.status_code)   # HTTP response

content = response.json()   # JSON data

"""below is code used to test the questions, i have commented it out so it doesn't return
errors when i change the the API request"""

#putting the number of responses from the json data into a list
#numberOfResponses = content['total']

#print(numberOfResponses)

#getting the difficulties of the recipes and putting them into a list
#difficulties = [recipe['difficulty'] for recipe in content['recipes']]

#print(difficulties)

#testing the code given in the question
for i in range(0,100):
    temp = random.choice([k for k in range(3,21,2)])
    print(temp)

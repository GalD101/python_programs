import requests
from bs4 import BeautifulSoup

url = "http://avivitagamdali.co.il/"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

images = soup.find_all

print(soup.prettify())
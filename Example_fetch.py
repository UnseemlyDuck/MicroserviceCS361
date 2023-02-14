import requests

url = 'http://localhost:8080/images/blick.jpg'
response = requests.get(url)

# If the response code is 200 (ok), the code retrieves the image data with the response body using the 'content' attribute and stores it.
if response.status_code == 200:
    image_data = response.content
    # do something with the image data, such as save it to a file
else:
    # handle the error

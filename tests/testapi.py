import requests


# Make sure to start the express server with the following command! :)
# nodemon app.js
def test_root_endpoint():
    endpoint = "http://localhost:9876/"
    data = requests.get(endpoint)
    print(data.text)

def test_random_endpoint():
    endpoint = "http://localhost:9876/api/random"
    data = requests.get(endpoint)
    print(data.text)

def main():
    test_root_endpoint()
    test_random_endpoint()


main()

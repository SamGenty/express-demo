import requests
import time

# Make sure to start the express server with the following command! :)
# nodemon app.js
def test_root_endpoint():
    endpoint = "http://localhost:9876/"
    data = requests.get(endpoint)
    print(data.text)

def test_random_endpoint():
    endpoint = "http://localhost:9876/api/random"
    x = 5000
    start = time.time()
    for i in range(x):
        data = requests.get(endpoint)
    end = time.time()
    print("Total time : ")  + str(end-start)
    print((end - start) / (x*1.0))

def main():
    test_root_endpoint()
    test_random_endpoint()


main()

import requests

# Base URL for testing
BASE_URL = "https://httpbin.org"

def get_request():
    response = requests.get(f"{BASE_URL}/get")
    data = response.json()
    if 'origin' in data:
        del data['origin']  # Remove client IP for privacy
    print("GET response:")
    print(data)
    print("\n" + "-"*50 + "\n")

def post_request():
    payload = {
        "name": "username",
        "password": "your-password"
    }
    response = requests.post(f"{BASE_URL}/post", data=payload)
    data = response.json()
    if 'origin' in data:
        del data['origin']
    print("POST response:")
    print(data)
    print("\n" + "-"*50 + "\n")

def put_request():
    payload = {
        "name": "username",
        "password": "new-password"
    }
    response = requests.put(f"{BASE_URL}/put", json=payload)  # send JSON data
    data = response.json()
    if 'origin' in data:
        del data['origin']
    print("PUT response:")
    print(data)
    print("\n" + "-"*50 + "\n")

def patch_request():
    payload = {
        "password": "patched-password"
    }
    response = requests.patch(f"{BASE_URL}/patch", json=payload)  # partial update
    data = response.json()
    if 'origin' in data:
        del data['origin']
    print("PATCH response:")
    print(data)
    print("\n" + "-"*50 + "\n")

def delete_request():
    response = requests.delete(f"{BASE_URL}/delete")
    data = response.json()
    if 'origin' in data:
        del data['origin']
    print("DELETE response:")
    print(data)
    print("\n" + "-"*50 + "\n")

def main():
    get_request()
    post_request()
    put_request()
    patch_request()
    delete_request()

if __name__ == "__main__":
    main()

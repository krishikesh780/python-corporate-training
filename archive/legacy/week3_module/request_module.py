# ----------------------------------------------
# 📘 Real-world Examples using requests module
# ✅ All functions are callable & testable
# ----------------------------------------------

import requests

# ✅ 1. Get dummy posts from JSONPlaceholder API
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    posts = response.json()
    # print("📰 Total Posts Fetched:", (posts))

    print("📢 Latest Dummy Posts:")
    for post in posts[:5]: # Display first 5 posts: 0, 1, 2, 3, 4
        print(f"- {post['body']}")


# ✅ 3. Get your public IP address
def get_public_ip():
    response = requests.get("https://api.ipify.org?format=json")
    ip = response.json()['ip']
    print(f"🌐 Your IP Address: {ip}")


# ✅ 4. Get current weather for any city
def get_weather(city="UP"):
    url = f"https://wttr.in/{city}?format=3"  # Short weather format
    response = requests.get(url)
    print(f"⛅ Weather in {city}: {response.text}")


# ✅ 5. Download a random image
def download_image():
    image_url = "https://picsum.photos/200"
    response = requests.get(image_url)

    with open("random_image.jpg", "wb") as f:
        f.write(response.content)

    print("📷 Image downloaded as 'random_image.jpg'")


# ✅ 6. Post sample data to test API (dummy POST)
def post_data():
    url = "https://httpbin.org/post"
    data = {'name': 'Rishikesh', 'role': 'Trainer'}
    response = requests.post(url, data=data)
    print("📝 POST Response:")
    print(response.json())

# get_posts()
# get_public_ip()
# get_weather()
download_image()    
# post_data()
# ✅ Run selected methods here
# if __name__ == "__main__":
#     print("Choose an option to run:")
#     print("1. Get Posts")
#     print("2. Get Bitcoin Price")
#     print("3. Get Public IP")
#     print("4. Get Weather")
#     print("5. Download Image")
#     print("6. POST Sample Data")

#     choice = input("Enter option (1-6): ")

#     if choice == "1":
#         get_posts()
#     elif choice == "2":
#         get_bitcoin_price()
#     elif choice == "3":
#         get_public_ip()
#     elif choice == "4":
#         city = input("Enter city name (default: Delhi): ") or "Delhi"
#         get_weather(city)
#     elif choice == "5":
#         download_image()
#     elif choice == "6":
#         post_data()
#     else:
#         print("❌ Invalid option!")

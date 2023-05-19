import requests
import time
import random
import matplotlib.pyplot as plt
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def execute_login_request(self):
        response_times = []
        bytes_sent = 0
        payload = {"firstName": "Allan", "lastName": "Gray"}

        start_time = time.time()
        response = requests.post("https://httpbin.org/post", data=payload)
        end_time = time.time()

        response_times.append(end_time - start_time)
        bytes_sent += len(response.content)

        return response_times, bytes_sent

    def execute_get_requests(self):
        response_times = []
        bytes_sent = 0

        num_requests = random.randint(1, 5)
        for _ in range(num_requests):
            start_time = time.time()
            response = requests.get("https://httpbin.org/get")
            print(response.status_code)
            end_time = time.time()

            response_times.append(end_time - start_time)
            bytes_sent += len(response.content)

        return response_times, bytes_sent
    
    def execute_post_requests(self):
        response_times = []
        bytes_sent = 0
        image_path = "008.jpg"

        num_requests = random.randint(1, 5)
        for _ in range(num_requests):
            start_time = time.time()
            with open(image_path, "rb") as file:
                response = requests.post("https://httpbin.org/post", files={"image": file})
            print(response.status_code)
            end_time = time.time()

            response_times.append(end_time - start_time)
            bytes_sent += len(response.content)

        return response_times, bytes_sent


def perform_load_testing(users):
    login_response_times = []
    get_response_times = []
    post_response_times = []
    all_bytes_sent = []
    login_bytes_sent = []
    get_bytes_sent = []
    post_bytes_sent = []


    with ThreadPoolExecutor() as executor:
        login_futures = [executor.submit(user.execute_login_request) for user in users]
        get_futures = [executor.submit(user.execute_get_requests) for user in users]
        post_futures = [executor.submit(user.execute_post_requests) for user in users]

        for future in concurrent.futures.as_completed(login_futures):
            response_times, bytes_sent = future.result()
            login_response_times.extend(response_times)
            login_bytes_sent.append(bytes_sent)
            all_bytes_sent.append(bytes_sent)

        for future in concurrent.futures.as_completed(get_futures):
            response_times, bytes_sent = future.result()
            get_response_times.extend(response_times)
            get_bytes_sent.append(bytes_sent)
            all_bytes_sent.append(bytes_sent)

        for future in concurrent.futures.as_completed(post_futures):
            response_times, bytes_sent = future.result()
            post_response_times.extend(response_times)
            post_bytes_sent.append(bytes_sent)
            all_bytes_sent.append(bytes_sent)

    return login_response_times, get_response_times, post_response_times, sum(all_bytes_sent), sum(login_bytes_sent), sum(get_bytes_sent), sum(post_bytes_sent)

def main():
    num_users = int(input("Enter the number of users: "))

    users = [User(user_id) for user_id in range(1, num_users + 1)]

    login_response_times, get_response_times, post_response_times, bytes_sent, login_bytes_sent, get_bytes_sent, post_bytes_sent = perform_load_testing(users)

    # Display statistics
    avg_login_response_time = sum(login_response_times) / len(login_response_times)
    avg_get_response_time = sum(get_response_times) / len(get_response_times)
    avg_post_response_time = sum(post_response_times) / len(post_response_times)
    print("Average Login Response Time:", avg_login_response_time)
    print("Average GET Response Time:", avg_get_response_time)
    print("Average POST Response Time:", avg_post_response_time)
    print("Total Bytes Sent:", bytes_sent)

    # Create histograms for response times
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 3, 1)
    plt.hist(login_response_times, bins=15, color='red')
    plt.xlabel('Response Time')
    plt.ylabel('Count')
    plt.title('Distribution of Login Response Times')
    plt.text(0.05, 0.95, f"Number of Users: {num_users}", transform=plt.gca().transAxes, va='top')
    plt.text(0.05, 0.85, f"Avg Login Time: {avg_login_response_time:.4f}", transform=plt.gca().transAxes, va='top')
    plt.text(0.05, 0.75, f"Total Login Bytes Sent: {login_bytes_sent}", transform=plt.gca().transAxes, va='top')

    plt.subplot(1, 3, 2)
    plt.hist(get_response_times, bins=15, color='blue')
    plt.xlabel('Response Time')
    plt.ylabel('Count')
    plt.title('Distribution of GET Response Times')
    plt.text(0.05, 0.95, f"Number of Users: {num_users}", transform=plt.gca().transAxes, va='top')
    plt.text(0.05, 0.85, f"Avg GET Time: {avg_get_response_time:.4f}", transform=plt.gca().transAxes, va='top')
    plt.text(0.05, 0.75, f"Total GET Bytes Sent: {get_bytes_sent}", transform=plt.gca().transAxes, va='top')

    plt.subplot(1, 3, 3)
    plt.hist(post_response_times, bins=15, color='green')
    plt.xlabel('Response Time')
    plt.ylabel('Count')
    plt.title('Distribution of POST Response Times')
    plt.text(0.05, 0.95, f"Number of Users: {num_users}", transform=plt.gca().transAxes, va='top')
    plt.text(0.05, 0.85, f"Avg POST Time: {avg_post_response_time:.4f}", transform=plt.gca().transAxes, va='top')
    plt.text(0.05, 0.75, f"Total POST Bytes Sent: {post_bytes_sent}", transform=plt.gca().transAxes, va='top')

    plt.tight_layout()
    plt.savefig('response_times_plot.png')
    plt.close()

if __name__ == "__main__":
    main()

import requests
import time
import random
import matplotlib.pyplot as plt
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

class User:
    def __init__(self, user_id):
        self.user_id = user_id

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
        payload = {"firstName": "Allan", "lastName": "Gray"}

        num_requests = random.randint(1, 5)
        for _ in range(num_requests):
            start_time = time.time()
            response = requests.post("https://httpbin.org/post", data=payload)
            print(response.status_code)
            end_time = time.time()

            response_times.append(end_time - start_time)
            bytes_sent += len(response.content)

        return response_times, bytes_sent


def perform_load_testing(users):
    get_response_times = []
    post_response_times = []
    all_bytes_sent = []

    with ThreadPoolExecutor() as executor:
        get_futures = [executor.submit(user.execute_get_requests) for user in users]
        post_futures = [executor.submit(user.execute_post_requests) for user in users]

        for future in concurrent.futures.as_completed(get_futures):
            response_times, bytes_sent = future.result()
            get_response_times.extend(response_times)
            all_bytes_sent.append(bytes_sent)

        for future in concurrent.futures.as_completed(post_futures):
            response_times, bytes_sent = future.result()
            post_response_times.extend(response_times)
            all_bytes_sent.append(bytes_sent)

    return get_response_times, post_response_times, sum(all_bytes_sent)

def main():
    num_users = int(input("Enter the number of users: "))

    users = [User(user_id) for user_id in range(1, num_users + 1)]

    get_response_times, post_response_times, bytes_sent = perform_load_testing(users)

    # Display statistics
    avg_get_response_time = sum(get_response_times) / len(get_response_times)
    avg_post_response_time = sum(post_response_times) / len(post_response_times)
    print("Average GET Response Time:", avg_get_response_time)
    print("Average POST Response Time:", avg_post_response_time)
    print("Total Bytes Sent:", bytes_sent)

    # Create histograms for response times
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.hist(get_response_times, bins=15, color='blue')
    plt.xlabel('Response Time')
    plt.ylabel('Count')
    plt.title('Distribution of GET Response Times')

    plt.subplot(1, 2, 2)
    plt.hist(post_response_times, bins=15, color='green')
    plt.xlabel('Response Time')
    plt.ylabel('Count')
    plt.title('Distribution of POST Response Times')

    plt.tight_layout()
    plt.savefig('response_times_plot.png')
    plt.close()

if __name__ == "__main__":
    main()

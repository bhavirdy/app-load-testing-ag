import requests
import time
import random
import matplotlib.pyplot as plt

class User:
    def __init__(self, user_id, url, num_requests):
        self.user_id = user_id
        self.url = url
        self.num_requests = num_requests

    def execute_requests(self):
        response_times = []
        bytes_sent = 0

        for _ in range(self.num_requests):
            start_time = time.time()
            response = requests.get(self.url)
            end_time = time.time()

            response_times.append(end_time - start_time)
            bytes_sent += len(response.content)

        return response_times, bytes_sent

def perform_load_testing(users):
    all_response_times = []
    all_bytes_sent = []

    for user in users:
        response_times, bytes_sent = user.execute_requests()
        all_response_times.extend(response_times)
        all_bytes_sent.append(bytes_sent)

    return all_response_times, sum(all_bytes_sent)

def main():
    url = "https://www.youtube.com/watch?v=qriL9Qe8pJc"
    num_users = int(input("Enter the number of users: "))

    users = []
    for i in range(num_users):
        user_id = i + 1
        num_requests = random.randint(1, 10)
        users.append(User(user_id, url, num_requests))

    response_times, bytes_sent = perform_load_testing(users)

    # Display statistics
    avg_response_time = sum(response_times) / len(response_times)
    print("Average Response Time:", avg_response_time)
    print("Total Bytes Sent:", bytes_sent)

    # Create histogram for response times
    plt.hist(response_times, bins=15)
    plt.xlabel('Response Time')
    plt.ylabel('Count')
    plt.title('Distribution of Response Times')
    plt.savefig('response_times_plot.png')
    plt.close()

if __name__ == "__main__":
    main()

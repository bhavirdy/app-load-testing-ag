import requests
import time
import matplotlib.pyplot as plt

def perform_load_testing(url, num_requests):
    response_times = []
    bytes_sent = 0

    for _ in range(num_requests):
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        response_times.append(end_time - start_time)
        bytes_sent += len(response.content)

    return response_times, bytes_sent

def main():
    # url = input("Enter the URL to test: ")
    url = "https://en.wikipedia.org/wiki/Fortnite_Battle_Royale"
    num_requests = int(input("Enter the number of requests: "))

    response_times, bytes_sent = perform_load_testing(url, num_requests)

    # Display statistics
    avg_response_time = sum(response_times) / num_requests
    print("Average Response Time:", avg_response_time)
    print("Total Bytes Sent:", bytes_sent)

    # Create histogram for response times
    plt.hist(response_times, bins=15)
    plt.xlabel('Response Time')
    plt.ylabel('Count')
    plt.title('Distribution of Response Times')
    plt.tight_layout()
    plt.savefig('response_times_plot.png')
    plt.close()

if __name__ == "__main__":
    main()

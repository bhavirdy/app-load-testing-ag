from locust import HttpUser, task, between, events

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def my_task(self):
        response = self.client.get("/your-endpoint")
        # Process the response if needed

    def on_start(self):
        pass

# Event listener to print statistics
@events.test_stop.add_listener
def print_stats(environment, **kwargs):
    # Total requests
    total_requests = environment.stats.total_requests
    print(f"Total requests: {total_requests}")

    # Total failures
    total_failures = environment.stats.total_failures
    print(f"Total failures: {total_failures}")

    # Total average response time
    total_avg_response_time = environment.stats.total_average_response_time
    print(f"Total average response time: {total_avg_response_time:.2f} ms")

    # Total content length
    total_content_length = environment.stats.total_content_length
    print(f"Total content length: {total_content_length} bytes")

    # Requests per second
    requests_per_second = total_requests / environment.stats.total_run_time
    print(f"Requests per second: {requests_per_second:.2f}")

    # Response time percentiles
    response_time_percentiles = environment.stats.get_response_time_percentile(95)
    print(f"95th percentile response time: {response_time_percentiles:.2f} ms")

# Run the load test
if __name__ == "__main__":
    MyUser().run()

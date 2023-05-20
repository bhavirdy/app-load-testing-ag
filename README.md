# app-load-testing-ag

Allan Gray Coding Challenge: Load Testing Script

This script allows you to perform load testing on a web application by simulating multiple users making HTTP requests. It measures the response times and the amount of data sent for login, GET, and POST requests. Additionally, it generates histograms to visualize the distribution of response times for each type of request.

A login request occurs once per user at the beginning of a user's requests. It passes text for a login form.

POST requests post an jpg image. A random amount of POST requests are generated per user (in a range of 1, 5).

A random amount of GET requests are generated per user (in a range of 1, 5).

The program uses https://httpbin.org/ to execute these requests.

# Prerequisites:

Python 3.x
requests library
matplotlib library
How to Use
Install the required libraries by running the following command:

```pip install requests matplotlib```

Save the script to a Python file (e.g., load_test_users.py).

# Run the script using the command:

```python load_test_users.py```

Enter the number of users to simulate when prompted.

The script will simulate the specified number of users making login, GET, and POST requests concurrently. It will print the average response times for each type of request and the total number of bytes sent.

The script will generate three histograms showing the distribution of response times for login, GET, and POST requests. The histograms will be saved as response_times_plot.png.

# Customization

You can modify the URL and payload in the execute_login_request() and execute_post_requests() methods of the User class to match your specific use case.
The number of GET and POST requests made by each user is randomly generated in the range of 1 to 5. You can adjust this range in the execute_get_requests() and execute_post_requests() methods if needed.
The number of bins in the histograms can be adjusted by modifying the bins parameter in the plt.hist() function calls.

# Notes
The script uses a thread pool executor to concurrently execute the requests from multiple users, improving the performance of the load testing.
The requests library is used to make the HTTP requests.
The matplotlib library is used to create the histograms for visualizing the response times.
Please ensure that you have the necessary permissions and authorization before performing load testing on any web application.

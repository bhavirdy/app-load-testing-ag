import matplotlib.pyplot as plt

# Set up the figure and axis
fig, ax = plt.subplots()

# Initialize empty lists for x and y data
x_data = []
y_data = []

# Create the line plot
line, = ax.plot(x_data, y_data)

# Update the plot with new data
def update_plot(new_x, new_y):
    x_data.append(new_x)
    y_data.append(new_y)
    line.set_data(x_data, y_data)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(0.001)

# Example data update loop
for i in range(10):
    x = i
    y = i * i
    update_plot(x, y)

# Keep the plot window open
plt.show()

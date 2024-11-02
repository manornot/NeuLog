import requests
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import json

# Define the base URL for the NeuLog API
base_url = 'http://localhost:22004/NeuLogAPI'

# Initialize storage for all samples from the experiment
all_data_points = []
times = []

# Function to start an experiment
def start_experiment(sensor_type, sensor_id, rate, samples):
    command = f'StartExperiment:[{sensor_type}],[{sensor_id}],[{rate}],[{samples}]'
    response = requests.get(f'{base_url}?{command}')
    if response.status_code == 200:
        print('Experiment Started:', response.json())
    else:
        print('Error starting experiment:', response.status_code)

# Function to retrieve all samples collected so far in the experiment
def get_all_samples(sensor_type, sensor_id):
    command = f'GetExperimentSamples:[{sensor_type}],[{sensor_id}]'
    response = requests.get(f'{base_url}?{command}')
    if response.status_code == 200:
        data = response.json().get("GetExperimentSamples", [[]])
        if data and data[0]:
            return data[0]  # Return the complete list of samples
    else:
        print('Error retrieving samples:', response.status_code)
    return None

# Function to stop the experiment
def stop_experiment(sensor_type, sensor_id):
    command = f'StopExperiment:[{sensor_type}],[{sensor_id}]'
    response = requests.get(f'{base_url}?{command}')
    if response.status_code == 200:
        print('Experiment Stopped:', response.json())
    else:
        print('Error stopping experiment:', response.status_code)

# Define the plotting function
def update_plot(i):
    # Get all samples collected so far
    all_samples = get_all_samples(sensor_type, sensor_id)
    if all_samples is not None:
        current_time = time.time() - start_time
        times.append(current_time)
        all_data_points.extend(all_samples)  # Store all samples in all_data_points

        # Clear and update the plot with all data points
        ax.clear()
        ax.plot(range(len(all_data_points)), all_data_points, label="Respiration Data")
        ax.set_title("Real-Time Respiration Data")
        ax.set_xlabel("Sample Number")
        ax.set_ylabel("Sensor Value")
        ax.legend(loc="upper left")

# Save all data to a file at the end of the experiment
def save_data():
    with open("all_respiration_data.json", "w") as f:
        json.dump({"all_data_points": all_data_points}, f)
    print("Data saved to all_respiration_data.json")

# Start an experiment with the respiration sensor
sensor_type = 'Respiration'
sensor_id = 1  # Replace with your sensor's ID
rate = 8  # Sampling rate index (e.g., 8 for 10 samples per second)
samples = 10000  # Total number of samples to collect

# Start the experiment
start_experiment(sensor_type, sensor_id, rate, samples)

# Set up plot
fig, ax = plt.subplots()
start_time = time.time()

# Run the real-time plot with Matplotlib animation
try:
    ani = animation.FuncAnimation(fig, update_plot, interval=100)  # Update every second
    plt.show()
except KeyboardInterrupt:
    print("Stopping experiment due to user interruption.")
finally:
    # Stop the experiment and save the data
    stop_experiment(sensor_type, sensor_id)
    save_data()

# Event to handle plot window close and save data
def on_close(event):
    stop_experiment(sensor_type, sensor_id)
    save_data()

fig.canvas.mpl_connect('close_event', on_close)

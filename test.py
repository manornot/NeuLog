from NeuLog import NeuLog

# Initialize the NeuLog instance with default parameters
neulog = NeuLog(config_file=r"C:\Users\orman\Documents\MimicHub\EDI\Sustronics\NeuLog\config\sensors.yaml")

# Specify the parameters for the respiration data experiment
sensor_name = "Respiration"
rate = 8        # Sampling rate, adjust based on required frequency
samples = 1000  # Number of samples to collect

# Initialize the experiment for the respiration sensor
respiration_sensor = [(sensor_name, 1)]  # Assuming the sensor ID is 1
neulog.start_experiment(sensors=respiration_sensor, rate=rate, samples=samples)

# Fetch and print the samples in real-time
try:
    while True:
        samples = neulog.experiment.get_samples()
        if samples:
            print("Respiration Samples:", samples)
        else:
            print("No new data. Waiting...")
except KeyboardInterrupt:
    print("Experiment interrupted by user.")

# Stop the experiment once done
neulog.experiment.stop()
print("Experiment ended.")

class Experiment:
    def __init__(self, api_client, sensors, rate, samples):
        self.api_client = api_client
        self.sensors = sensors
        self.rate = rate
        self.samples = samples
        

    def start(self):
        
        sensor_params = ",".join([f"[{sensor.code}],[{id}]" for sensor,id in self.sensors])
        return self.api_client.send_request("StartExperiment", f"{sensor_params},[{self.rate}],[{self.samples}]")

    def stop(self):
        return self.api_client.send_request("StopExperiment")

    def get_samples(self):
        sensor_params = ",".join([f"[{sensor.code}],[{id}]" for sensor,id in self.sensors])
        return self.api_client.send_request("GetExperimentSamples", sensor_params)

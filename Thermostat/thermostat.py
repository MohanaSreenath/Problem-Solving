class SmartThermostatAgent:
    def __init__(self):
        self.current_temperature = 0

    def sense_temperature(self, temperature):
        self.current_temperature = temperature

    def control_thermostat(self):
        if self.current_temperature < 20:
            print("Turning on heating...")
        elif self.current_temperature > 25:
            print("Turning on cooling...")
        else:
            print("Temperature is comfortable.")
temp=int(input("temprature of the environment "))
agent = SmartThermostatAgent()
agent.sense_temperature(temp)
agent.control_thermostat()

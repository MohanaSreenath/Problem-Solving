class Power:
    def __init__(self):  # Constructor method to initialize the Power class
        self.current = 0  # Initialize the current power status to 0 (False)

    def func(self, power):  # Method to handle power changes
        self.current = power  # Update the current power status with the provided value
        if self.current == False:  # If power is False (0), meaning power is off
            print("Windows are opening")  # Open the windows to let air enter the room
        else:  # If power is True (1), meaning power is on
            print("Windows are closing")  # Close the windows to maintain temperature

Agent = Power()  # Create an instance of the Power class
power = bool(input())  # Accept user input to determine the power status of the room
Agent.func(power)  # Call the func method of the Shanks instance with the provided power status

from opcua import Server
from random import randint
import datetime
import time

# Create server instance
server = Server()

# Set endpoint to localhost for testing purposes
url = "opc.tcp://0.0.0.0:4840"
server.set_endpoint(url)

# Disable security policies for testing (Not recommended for production)
server.set_security_policy([
    "None",  # No security
])

# Register namespace
name = "DWSim_OPC_Server"
addspace = server.register_namespace(name)

# Get objects node
node = server.get_objects_node()

# Add parameters object
Param = node.add_object(addspace, "Parameters")

# Add variables for temperature, pressure, and time
Temp = Param.add_variable(addspace, "Temperature", 0)
Press = Param.add_variable(addspace, "Pressure", 0)
TimeVar = Param.add_variable(addspace, "Time", 0)

# Set variables writable
Temp.set_writable()
Press.set_writable()
TimeVar.set_writable()

# Start the server
server.start()
print("Server started at {}".format(url))

try:
    while True:
        # Generate random temperature and pressure values
        Temperature = randint(10, 50)
        Pressure = randint(200, 999)
        TIME = datetime.datetime.now()

        # Print values
        print(f"Temperature: {Temperature} C, Pressure: {Pressure} Pa, Time: {TIME}")

        # Update values on the server
        Temp.set_value(Temperature)
        Press.set_value(Pressure)
        TimeVar.set_value(TIME)

        # Sleep for 2 seconds
        time.sleep(2)

finally:
    # Ensure the server is properly shut down
    server.stop()
    print("Server stopped.")

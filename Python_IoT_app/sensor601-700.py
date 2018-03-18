import socket
import time
import random
from datetime import datetime

from elasticsearch import Elasticsearch     # import elasticsearch module
es = Elasticsearch()

TCP_IP = '127.0.0.1'        # Define the TCP IP
TCP_PORT = 5011             # Define the TCP Port
BUFFER_SIZE = 500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           # Create an INET streaming socket
s.connect((TCP_IP, TCP_PORT))                                   # Connect to the server on TCP_PORT

# define the Sensor class
class Luminosity:
    id = 601                                      # Initialize sensor id
    value = 1.00                                # Initialize sensor value
    postcode = 2000                             # Initialize sensor postcode
    def description(self):
        desc_str = "The value of sensor %d is %.2f and has a postcode %d." % (self.id, self.value, self.postcode)
        return desc_str

# Initialize sensor class
sensor = Luminosity()

# Define and initialize variables
sensor.value = 0
sensor.id = 601
sensor.postcode = 2000

# Start generating random values for the sensor class
while(1):
# sensors 1-200 are Oxygen sensors
# sensors 200- 400 are Smoke detection sensors
# sensors 400-600 are Parking space sensors
# sensors 600- 800 are Luminosity sensors
# sensors 800-1000 are Garbage sensors
      sensor.value = (random.randint(8,21))         # Generate the values for Smoke in the range from 8 to 21
      t = str(sensor.id).encode()                   # Convert the id to string so it can be sent to the TCP connection
      print (sensor.id)                             # Print the sensor id
      s.send(t)                                     # Send the id on the TCP connection
      s.send(",")                                   # Send a comma to separate id and value
      m = str(sensor.value).encode()                # Convert sensor value to string so it can be sent to TCP connection
      s.send(m)                                     # Send the id on the TCP connection
      s.send(",")                                   # Send a comma to separate value and postcode
      k = str(sensor.postcode).encode()             # Convert sensor postcode to string so it can be sent to TCP connection
      s.send(k)                                     # Send the postcode on the TCP connection
      s.send("\n")                                  # Send a newline character so the next set of values be printed on next line
      sensor.id = sensor.id+1                       # Increment the sensor id by 1
      sensor.postcode = sensor.postcode+1           # Increment the sensor postcode by 1
      time.sleep(1)                                 # Wait for 1 second to generate next value
      # Create a document to be sent to elasticsearch
      doc = {
          'sensorid': sensor.id,
          'value': sensor.value,
          'postcode': sensor.postcode,
          'timestamp': datetime.datetime.now(),
      }
      res = es.index(index="iot", doc_type='smart_building', body=doc)   # Index the document in elasticsearch
      print(res['created'])                                          # Print if indexed successfully
      if(sensor.id==701):                           # Reset the sensor id and postcode when it reaches 100 sensors
            sensor.id = 601                           # Reset sensor id
            sensor.postcode = 2000                  # Reset sensor postcode
s.close()

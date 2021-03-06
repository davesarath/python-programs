
# pip install paho-mqtt
import paho.mqtt.client as mqtt # Import the MQTT library
import time # The time library is useful for delays


# Our "on message" event
def messageFunction (client, userdata, message):
    topic = str(message.topic)
    message = str(message.payload.decode("utf-8"))
    print(topic +" : "+ message)

ourClient = mqtt.Client("makerio_mqtt") # Create a MQTT client object & giva any name
ourClient.username_pw_set("etmhjbta","qCC5wB4eE6f0")
ourClient.connect("tailor.cloudmqtt.com", 13544) # Connect to the test MQTT broker
ourClient.subscribe("switch") # Subscribe to the topic AC_unit
ourClient.on_message = messageFunction # Attach the messageFunction to subscription
ourClient.loop_start() # Start the MQTT client

# # Main program loop
# while(1):
#     ourClient.publish("switch", "on") # Publish message to MQTT broker
#     time.sleep(1) # Sleep for a second
input()

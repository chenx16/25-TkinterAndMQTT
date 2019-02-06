""" A simple example of using MQTT for SENDING messages. """

import mqtt_remote_method_calls as com
import time


def main():
    name1 = input("Enter one name (subscriber): ") # String
    name2 = input("Enter another name (publisher): ")

    mqtt_client = com.MqttClient() # Calls Init
    mqtt_client.connect(name1, name2) # Message call 2 things
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    while True:
        s = input("Enter a message: ")
        mqtt_client.send_message("say_it", [s])


main()

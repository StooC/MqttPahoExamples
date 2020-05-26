# MqttPahoExamples
Simple examples to demo paho.mqtt.client and test a MQTT Broker. Not that environment variables are used to have settings config/passwords in source file, see below for details.

# Dependances
This code has been developed on the Python 3.8.3 and uses [paho-mqtt](https://pypi.org/project/paho-mqtt/) and [dotenv](https://pypi.org/project/python-dotenv/) (this code can be removed and values set directly in code if preferred)

- `pip install paho-mqtt`
- `pip install -U python-dotenv`

# Using .env file
If leaving the code as is you need to define values for the broker, topic, etc. in a .env file (or set OS environment variables) in the same folder as the script files. This could contain key value pairs such as:

- `MQTT_BROKER="192.168.X.X"`
- `MQTT_TOPIC="test/hello"`
- `CLIENT_USER="user"`
- `CLIENT_PWD="password"`

See [dotenv on GitHub](https://github.com/theskumar/python-dotenv) for more details.
from threading import Thread
from time import sleep, time
from paho.mqtt import client as mqtt

from settings import (
  HOST,
  PORT,
  TOPIC_STORE_REQUEST,
  TOPIC_STORE_ADD,
  TOPIC_DISTCENTER_REQUEST,
  TOPIC_DISTCENTER_ADD,
)
import commons.utils as utils


class MqttClient(object):
  """ Represents a MQTT Client connection handler class"""

  def __init__(self, client_id=None, host=HOST, port=PORT, timeout=60):
    """The class initializer"""

    self._mqtt_client = mqtt.Client(client_id)
    self.host = host
    self.port = port
    self.timeout = timeout

    self.subscription_topics = [
      (TOPIC_STORE_REQUEST, 0),
      (TOPIC_STORE_ADD, 0),
      (TOPIC_DISTCENTER_REQUEST, 0),
      (TOPIC_DISTCENTER_ADD, 0),
    ]

    self._mqtt_client.on_message = self.mqtt_on_message
    self._mqtt_client.on_connect = self.mqtt_on_connect

  def publish(self, topic, payload):
    """Publishes a message to a victim"""

    encoded_payload = utils.encode(payload)
    self._mqtt_client.publish(topic=topic, payload=encoded_payload)

  def disconnect(self):
    self._mqtt_client.disconnect()

  def mqtt_on_connect(self, mqtt_client, userdata, flags, result):
    """A callback function that is responsible to being triggered when a connection was established"""

    if result == mqtt.MQTT_ERR_SUCCESS:
      print('Connected to MQTT broker')
    else:
      self.disconnect()
      self._mqtt_client = None
      print('Failed to connect to MQTT broker')

  def mqtt_on_message(self, mqtt_client, obj, msg):
    """Handles when a new message arrives"""

    decoded_msg = utils.decode(msg.payload)

    if msg.topic == TOPIC_STORE_REQUEST:
      print('TOPIC_STORE_REQUEST', decoded_msg)

    elif msg.topic == TOPIC_STORE_ADD:
      print('TOPIC_STORE_ADD', decoded_msg)

    elif msg.topic == TOPIC_DISTCENTER_REQUEST:
      print('TOPIC_DISTCENTER_REQUEST', decoded_msg)

    elif msg.topic == TOPIC_DISTCENTER_ADD:
      print('TOPIC_DISTCENTER_ADD', decoded_msg)


  def stop(self):
    """Stops the mqtt connection loop"""

    self.disconnect()
    self._mqtt_client.loop_stop()

  def run(self):
    """Run the MQTT client"""

    self._mqtt_client.connect(self.host, self.port, self.timeout)
    self._mqtt_client.subscribe(self.subscription_topics)

    Thread(target=self.check_for_timeout).start()

    self._mqtt_client.loop_start()


  def check_for_timeout(self):
    """Checks if we should stop the loop based on `self.listen_timeout`"""

    start_time = time()

    while True:
      if time() > start_time + self.timeout:
        self._mqtt_client.loop_stop()
        break
      sleep(0.5)

    print(f'Scan has finished! @@@@@2')

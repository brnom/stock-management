# import asyncio

from commons.client import MqttClient
from models.store import StoreManager
from models.topic import TopicManager

def start():
  """Handles when a user selects the connect method"""

  # loop = asyncio.get_event_loop()

  print('Starting server.')

  topic_manager = TopicManager()

  print(topic_manager.list_topics())

  try:
    mqtt_client = MqttClient(topic_manager=topic_manager)
    mqtt_client.run()

    store_manager = StoreManager(mqtt_client, topic_manager)

    # mock client requests
    store_names = store_manager.list()
    store_manager.sell(store_names[0], 10)
    store_manager.sell(store_names[0], 60)

    # loop.run_forever()
  except KeyboardInterrupt:
    print('Connection interrupted!')
    mqtt_client.stop()
  # finally:
  #   loop.close()


if __name__ == '__main__':
  """Main driver for this application"""
  start()

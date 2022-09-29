# import asyncio

from commons.client import MqttClient
from models.store import StoreManager

def start():
  """Handles when a user selects the connect method"""

  # loop = asyncio.get_event_loop()

  print('Starting server.')

  try:
    mqtt_client = MqttClient()
    mqtt_client.run()

    store_manager = StoreManager(mqtt_client)

    # mock client requests
    store_names = store_manager.list()
    store_manager.sell(store_names[0], 10)
    store_manager.sell(store_names[0], 60)

    # loop.run_forever()
  except KeyboardInterrupt:
    print('Connection interrupted!', start='\n')
    mqtt_client.stop()
  # finally:
  #   loop.close()


if __name__ == '__main__':
  """Main driver for this application"""
  start()

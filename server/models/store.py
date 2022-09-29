import random

from settings import STORE_MAX_STOCK, TOPIC_STORE_REQUEST
from commons.client import MqttClient
from commons.utils import get_stock_level_color


class Store():
  def __init__(self, name: str, mqtt_client: MqttClient):
    self.name = name
    self.stock = int(STORE_MAX_STOCK * .8)
    self.mqtt_client = mqtt_client
  
  def sell(self, amount: int):
    print(f'{self.name} is selling {amount} products')

    self.stock -= amount

    stock_color = get_stock_level_color(self.stock, STORE_MAX_STOCK)

    print(f'{self.name} has {self.stock} products left ({stock_color})')

    if (stock_color == 'red'):
      print(f'{self.name} will request a new batch of products from the distribution center')

      missing = STORE_MAX_STOCK - self.stock
      payload = {
        'store': self.name,
        'amount': missing
      }

      self.mqtt_client.publish(TOPIC_STORE_REQUEST, payload)

      print(f'{self.name} requested {missing} products from the distribution center')


    return self.stock
  
  def add(self, amount: int):
    self.stock += amount
    return self.stock


class StoreManager():
  def __init__(self, mqtt_client: MqttClient):
    self.stores: dict[(str, Store)] = {}

    # create ramdom stores from 10 to 20
    for i in range(random.randint(10, 20)):
      name = f'store-{str(i)}'
      self.stores[name] = Store(name, mqtt_client)

    # logs
    print(f'Created {self.count()} stores')

  def list(self):
    return list(self.stores.keys())

  def count(self):
    return len(self.stores)
  
  def get_store(self, name: str):
    return self.stores[name]

  def sell(self, name, amount: int):
    store = self.get_store(name)
    return store.sell(amount)
  
  def add(self, name, amount: int):
    store = self.get_store(name)
    return store.add(amount)

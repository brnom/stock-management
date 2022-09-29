import os

HOST = os.environ['MQTT_HOST']
PORT = int(os.environ['MQTT_PORT'])

STORE_MAX_STOCK = 100
""" The maximum stock of a given store """

TOPIC_STORE_REQUEST = 'store/request'
""" Store requests a new batch of products from the distribution center """

TOPIC_STORE_ADD = 'store/add'
""" Distribution center adds a new batch of products to stores stock """

TOPIC_DISTCENTER_REQUEST = 'distcenter/request'
""" Distribution center requests a new batch of products from the fabrics """

TOPIC_DISTCENTER_ADD = 'distcenter/add'
""" Fabrics add a new batch of products to the distribution center stock """

from base64 import b64decode, b64encode
import json


def encode(data):
  """Encodes a message"""
  return b64encode(json.dumps(data).encode())


def decode(data):
  """Decodes a message"""
  return json.loads(b64decode(data).decode())


def get_stock_level_color(stock: int, max_stock: int):
  """Returns the stock level color"""

  percentage = stock / max_stock
  if percentage >= 0.5:
    return 'green'
  elif percentage >= 0.25:
    return 'yellow'
  else:
    return 'red'
  
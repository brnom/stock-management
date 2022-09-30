from settings import (
  TOPIC_STORE_REQUEST,
  TOPIC_STORE_ADD,
  TOPIC_DISTCENTER_REQUEST,
  TOPIC_DISTCENTER_ADD,
)

class Topic():
  def __init__(self, name):
    self.name = name
    self.messages = []
  
  def add_msg(self, message: dict) -> None:
    self.messages.append(message)
  
  def get_next_msg(self) -> dict:
    return self.messages.pop(0)
  
  def count_msgs(self) -> int:
    return len(self.messages)
  

class TopicManager():
  def __init__(self):
    names = [
      TOPIC_STORE_REQUEST,
      TOPIC_STORE_ADD,
      TOPIC_DISTCENTER_REQUEST,
      TOPIC_DISTCENTER_ADD,
    ]

    self.topics: dict[str, Topic] = {}

    for name in names:
      self.topics[name] = Topic(name)
  
  def add_topic(self, name):
    self.topics[name] = Topic(name)
  
  def get_topic(self, name):
    return self.topics[name]
  
  def list_topics(self):
    return list(self.topics.keys())
  
  def publish_msg(self, topic_name: str, message: dict):
    topic = self.get_topic(topic_name)
    topic.add_msg(message)
  
  def get_next_msg(self, topic_name: str) -> dict:
    topic = self.get_topic(topic_name)
    return topic.get_next_msg()
  
  def count(self):
    return len(self.topics)

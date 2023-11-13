import threading
import requests
import json


class RequestHandler(text):
  def __init__(self):
      self.text = text;
      self.thread = threading.Thread(target=self.request)
      self.thread.start()

  def request(self):
    request = self.text.get().split("?")
    url = "http://localhost:8080/CriticalDesignPBE/back/index.php?request={}&{}".format(request[0], request[1])
    response = requests.get(url)
    rq = response.json()
    return (rq)

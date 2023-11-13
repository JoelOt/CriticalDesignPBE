import threading
import requests
import json


class RequestHandler():
  def __init__(self):
      self.thread = threading.Thread(target=self.request)
      self.thread.start()


  #url destinat a text que ha de tornar rq que pot ser una llista on string amb el nom de l'usuari ... 
  def request(self, text):
    url = "http://localhost:8080/CriticalDesignPBE" + text
    response = requests.get(url)
    rq = response.json()
    return (rq)

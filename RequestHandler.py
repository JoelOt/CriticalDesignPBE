import threading
import requests
import json


class RequestHandler():
  def __init__(self):
      self.thread = threading.Thread(target=self.request_str)
      self.thread.start()


  #url destinat a text que ha de tornar rq que pot ser una llista on string amb el nom de l'usuari ... 
  def request_strt(self, text):
    url = "http://localhost:8080/phpProject2/back/" + text
    response = requests.get(url)
    rq = response.json()
    return (rq)

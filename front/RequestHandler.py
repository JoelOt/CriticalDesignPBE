import sys

import gi
import threading 
import requests
import json

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class EntryHandler:
    def __init__(self, entry, callback):
        self.entry = entry
        self.callback = callback
        self.entry.connect("changed", self.on_entry_changed)

    def on_entry_changed(self, entry):
        text = entry.get_text()
        if text:
            handler = RequestHandler(text, self.callback)
            handler.thread.start()



class RequestHandler:
    def __init__(self, text, callback):
        self.text = text
        self.callback = callback
        self.thread = threading.Thread(target=self.request)
        self.thread.start()

  def request(self):
      request_data = self.text.get().split("?")
      url = "http://localhost:8080/CriticalDesignPBE/back/index.php?request={}&{}".format(request_data[0], request_data[1])
      response = requests.get(url)
      result = response.json()
      self.callback(result)



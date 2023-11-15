import sys
import threading
import gi
import json
import requests

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from course_manager import CourseManager
from entry_handler import EntryHandler


class CourseManager(Gtk.Box):
    def __init__(self, entry_handler):
        super().__init__()

        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.set_spacing(150)

        self.create_button()
        self.create_entry(entry_handler)

        self.show_all()

    def create_button(self):
        self.button = Gtk.Button(label = 'Logout')
        self.button.set_size_request(60, 40)
        self.button.set_alignment(1, 0)
        self.pack_start(self.button, False, False, 10)
      
    def create_entry(self):
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Enter your query:")
        self.entry.connect("changed", self.metodeThread)
        self.pack_start(entry, False, False, 0)
    
    #def crear grid i taula:
    
    
    def metodeThread(self, widjet):  #creem un thread per consultar el server de forma concurrent
        text = entry.get_text()
        thread1 = threading.Thread(target= self.consultarServer(text))  #li passem el que esta escrit
        thread1.start()
        
    def consultarServer(self,text):  #fa la consulta GET i rep com a resultat un json 
        request_data = text.split("?")
        tables = request_data[0]
        variables = request_data[1]
        textvar = ""
        if (len(request_data) >= 2){
            textvar = tables + "&" + variables
        } else if (){
            textvar = tables
        }else{
            return
        }
        url = "http://localhost:8080/CriticalDesignPBE/back/index.php?" + textvar
        response = requests.get(url)
        result = response.json()
        
        GObject.idle_add(self.update_ui, result)  #modifica la interficie grafica
        
    def update_ui(self,result):
        #posar les dades maques
        array_of_strings = [json.dumps(entry) for entry in result]
        for entry_str in array_of_strings:
            entry_dict = json.loads(entry_str)
            
        #modifciar taula
        
if __name__ == '__main__':
    
    entry = Gtk.Entry()
    course_manager = CourseManager()

    win = Gtk.Window()
    Gtk.Window.__init__(win, title = 'Course Manager')
    win.set_default_size(800, 500)
    win.connect("destroy", Gtk.main_quit)
    win.add(course_manager)
    win.show_all()
    Gtk.main()


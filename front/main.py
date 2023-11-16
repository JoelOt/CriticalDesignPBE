import sys
import threading
import gi
import json
import requests

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from course_manager import CourseManager
from entry_handler import EntryHandler


class CourseManager(Gtk.Grid):
    def __init__(self):
        super().__init__()

        self.set_size_request(-1, 20)
        self.login()
    
    def create_button(self):
        self.button = Gtk.Button(label = 'Logout')
        self.attach(button,1, 0, 1, 1)
        self.button.connect("clicked", self.login)
        
    def create_entry(self):
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Enter your query:")
        self.entry.connect("changed", metodeThread)
        self.attach(entry,0, 1, 1, 1)


    def login (self):  #crec que ja ens convé que sigui bloquejant
        label = Gtk.Label(label="acerque su tarjeta")
        self.attach(entry,0, 1, 1, 1)
        self.show_all()

        #llegir uid
        
        label.set_text(uid)
        
        url = "http://localhost:8080/CriticalDesignPBE/back/index.php?uid={}".format(uid)
        response = request.get(url)
        if response.status_code == 200:
            result = response.text()
            #ensenyar al lcd en thread auxiliar
        label.destroy()
        self.create_button()
        self.create_entry()
        self.show_all()


    def metodeThread(self, widjet):  #creem un thread per consultar el server de forma concurrent
        text = entry.get_text()
        thread1 = threading.Thread(target= self.consultarServer(text))  #li passem el que esta escrit
        thread1.start()
        
    def consultarServer(self, text):  #fa la consulta GET i rep com a resultat un json 
        request = text.split("?")
        if len(request) < 2:
            request.append('')
        url = "http://localhost:8080/CriticalDesignPBE/back/index.php?request={}&{}".format(request[0], request[1])  #url de l'arxiu index.php on s'envia la request per que el processi
        response = requests.get(url)  #fem una request post a l'url enviant les data
        print("STATUS: {}, url: {}".format(response.status_code, url))
        # verificar si la request és exitosa
        if response.status_code == 200: #200 exitosa, 404 url no trobat, 500 error en el php...
            result = response.text()
            GObject.idle_add(self.update_ui, result)  #modifica la interficie grafica 
        
    def update_ui(self, result):
        matriz = json.loads(result)
        
        grid = Gtk.Grid()
        grid.set_row_homogeneous(True)
        grid.set_column_homogeneous(True)
        
        for i, fila in enumerate(matriz):
            for j, dada in enumerate(fila):
                label = Gtk.Label(label=str(dada))
                grid.attach(label, j, i, 1, 1)
                
        self.attach(grid, 0, 2, 2, 1)


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

import sys
import threading
import gi
import json
import requests

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib


class CourseManager(Gtk.Grid):
    def __init__(self):
        super().__init__()

        self.set_size_request(-1, 20)
        
        self.create_button()
        
        self.create_entry()
      
        self.login()
    
    def create_button(self):
        self.button = Gtk.Button(label = 'Logout')
        self.attach(self.button,1, 0, 1, 1)
        estil = self.button.get_style_context()
        estil.add_class("button_style")
        self.button.connect("clicked", self.login)
        
    def create_entry(self):
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Enter your query:")
        self.entry.connect("activate", self.metodeThread)
        self.attach(self.entry,0, 0, 1, 1)

    def login(self):
        self.nom = None
        self.hide_all()
        self.label = Gtk.Label("acerque la tarjeta")
        self.attach(self.lable,0, 1, 1, 1)
        self.label.show()

        #llegeix uid
        uid = 'D1FDE202'
        self.label.set_text(uid)

        url = "http://localhost:8080/CriticalDesignPBE/back/index.php/uid?uid={}".format(uid)
        response = requests.get(url)
        if response.status_code == 200:
                self.nom = response.text

        #print lcd

        self.label.destroy()
        self.show_all()

    def metodeThread(self, widget):  #creem un thread per consultar el server de forma concurrent
        text = self.entry.get_text()
        thread1 = threading.Thread(target= self.consultarServer(text))  #li passem el que esta escrit
        thread1.start()
      
    def consultarServer(self, text):  #fa la consulta GET i rep com a resultat un json 
        request = text
        self.req = request.split("?")[0]
        url = "http://localhost:8080/CriticalDesignPBE/back/index.php/{}".format(request)
        response = requests.get(url)
        print("STATUS: {}, url: {}".format(response.status_code, url))
        # verificar si la request és exitosa
        if response.status_code == 200: #200 exitosa, 404 url no trobat, 500 error en el php...
            result = response.text
            GLib.idle_add(self.update_ui, result)  #modifica la interficie grafica
        
    def update_ui(self, result):
        try:
            matriz = json.loads(result)
        except json.decoder.JSONDecodeError as e:
            print("Error al decodificar JSON:", e)
            return
        
        for widget in self.get_children():
            if widget is not self.entry and widget is not self.button:
                widget.destroy()

        if self.req == 'marks':
            labels = ['subject', 'name', 'mark', 'id']
        elif self.req == 'timetables':
            labels = ['day', 'hour', 'subject', 'room']
        elif self.req == 'tasks':
            labels = ['date', 'subject', 'name']

        win.__init__()

      
        for row, person in enumerate(matriz):
            for col, key in enumerate(labels):
                if row == 0:
                    label = Gtk.Label(label=key)
                    estil = label.get_style_context()
                    estil.add_class("personalitzar")
                    self.attach(label, col , 3, 1, 1)
                value = person[key]
                label = Gtk.Label(label=value)
                estil = label.get_style_context()
                estil.add_class("personalitzar")
                self.attach(label, col, row + 5 , 1, 1)
                label.set_hexpand(True)

        win.show_all()

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title = 'Course Manager')
        self.set_default_size(800, 500)
        self.connect("destroy", Gtk.main_quit)
        

if __name__ == '__main__':
    
    course_manager = CourseManager()
    css_provider = Gtk.CssProvider()
    css_provider.load_from_path("style.css")
 
    win = MyWindow()
    win.__init__()
    win.add(course_manager)
    screen= Gdk.Screen.get_default()
    style_context = Gtk.StyleContext()
    style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    win.show_all()
    Gtk.main()

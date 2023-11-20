
import sys
import threading
import gi
import json
import requests
from nfc import Rfid

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib


class CourseManager(Gtk.Grid):
    def __init__(self):
        super().__init__()

        self.set_size_request(-1, 20)
        self.userName = None
        self.uid = None
        self.create_button()
        self.create_entry()
        self.login()
    
    def create_button(self):
        self.button = Gtk.Button(label = 'Logout')
        self.attach(self.button,1, 0, 1, 1)
        estil = self.button.get_style_context()
        estil.add_class("button_style")
        self.button.connect("clicked", lambda button: self.login())
        
    def create_entry(self):
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Enter your query:")
        self.entry.connect("activate", lambda entry: self.metodeThread(uid=self.uid))
        
        self.attach(self.entry,0, 0, 1, 1)

    def login(self):
        print("login...")
        self.label = Gtk.Label("acerque la tarjeta")
        self.attach(self.label,0, 1, 1, 1)
        self.label.show()

        reader = Rfid()
        self.uid = reader.read_uid()
        
        #self.label.set_text(self.uid)

        url = "http://10.42.0.1:8080/CriticalDesignPBE/back/index.php/uid"
        headers = {'uid': self.uid}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
                self.userName = response.text
        print(self.userName)
        self.label.destroy()
        self.show_all()
         
    def metodeThread(self, uid):  #creem un thread per consultar el server de forma concurrent
        text = self.entry.get_text()
        thread1 = threading.Thread(target= self.consultarServer(text,uid))  #li passem el que esta escrit i el uid
        thread1.start()
      
    def consultarServer(self, text, uid):  #fa la consulta GET i rep com a resultat un json 
        request = text
        self.req = request.split("?")[0]
        url = "http://10.42.0.1:8080/CriticalDesignPBE/back/index.php/{}".format(request)
        headers = {'uid': uid}  #posem el uid a la capçalera perque sino peta en alguns casos
        response = requests.get(url, headers=headers)  #enviem la request amb capçalera extra
        print("STATUS: {}, url: {}".format(response.status_code, url))
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
            labels = ['subject', 'name', 'mark']
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
    
    win = MyWindow()
    win.__init__()
    win.show_all()
    course_manager = CourseManager()
    css_provider = Gtk.CssProvider()
    css_provider.load_from_path("style.css")
    
    
    win.add(course_manager)
    screen= Gdk.Screen.get_default()
    style_context = Gtk.StyleContext()
    style_context.add_provider_for_screen(screen, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    Gtk.main()

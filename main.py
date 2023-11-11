import sys

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class CourseManager(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title = 'course manager')
        self.set_default_size(800, 500)
        self.connect("destroy", Gtk.main_quit)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=150)

        self.add(self.box)
        self.create_button()
        self.create_entry()

        self.show_all()


    def create_button(self):
        self.button = Gtk.Button(label = 'Logout')
        self.button.set_size_request(60, 40)
        self.button.set_alignment(1, 0)
        self.box.pack_start(self.button, False, False, 10)
        
    def on_entry_changed(self, entry):
        text = entry.get_text()

        
    def create_entry(self):
        self.entry = Gtk.Entry()
        self.entry.set_placeholder_text("Enter your query:")
        self.entry.connect("changed", self.on_entry_changed)
        self.box.pack_start(self.entry, False, False, 0)


win = CourseManager()
Gtk.main()

import sys

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from RequestHandler import EntryHandler



class CourseManager(Gtk.Grid):
    def __init__(self, entry_handler):
        super().__init__()

        self.set_size_request(-1, 20)
        self.create_button()
        self.create_entry(entry_handler)

        self.show_all()

    def create_button(self):
        button = Gtk.Button(label = 'Logout')
        self.attach(button,1, 0, 1, 1)
        
    def create_entry(self, entry_handler):
        entry = Gtk.Entry()
        entry.set_placeholder_text("Enter your query:")
        entry.connect("changed", entry_handler.on_entry_changed)
        self.attach(entry,0, 1, 1, 1)



        self.pack_start(entry, False, False, 0)



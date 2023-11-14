import sys

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
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
        
    

    def create_entry(self, entry_handler):
        entry = Gtk.Entry()
        entry.set_placeholder_text("Enter your query:")
        entry.connect("changed", entry_handler.on_entry_changed)
        self.pack_start(entry, False, False, 0)



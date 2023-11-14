import sys

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from course_manager import CourseManager
from entry_handler import EntryHandler


def handle_request_result(result):
    print(result)



if __name__ == '__main__':
    
    entry = Gtk.Entry()
    entry_handler = EntryHandler(entry, handle_request_result)
    course_manager = CourseManager(entry_handler)

    win = Gtk.Window()
    Gtk.Window.__init__(win, title = 'Course Manager')
    win.set_default_size(800, 500)
    win.connect("destroy", Gtk.main_quit)
    win.add(course_manager)
    win.show_all()
    Gtk.main()


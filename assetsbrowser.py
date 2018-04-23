#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


builder = Gtk.Builder()
builder.add_from_file("AssetsBrowser.glade")

builder.add_objects_from_file("AssetsBrowser.glade", ("mainWindow", "textureWindow"))

mainWindow = builder.get_object("mainWindow")
textureWindow = builder.get_object("textureWindow")
# print(builder.get_objects())


mainWindow.connect("destroy", Gtk.main_quit)
mainWindow.show_all()
textureWindow.show_all()
Gtk.main()



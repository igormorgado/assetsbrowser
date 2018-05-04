#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Handler:
    def onDestroy(self, *args):
        Gtk.main_quit()

    def toggleTextureLock(self, button):
        print("Locked/Unlocked", button)


builder = Gtk.Builder()
builder.add_from_file("AssetsBrowser.glade")
builder.add_objects_from_file("AssetsBrowser.glade", (
    "assets_browser_window",
    "texture_window",
    "about_dialog",
    "main_menu",
    "recent_menu",
    "search_menu",
    "texture_menu"

    ))

mainwin = builder.get_object("assets_browser_window")
textwin = builder.get_object("texture_window")
aboutwin = builder.get_object("about_dialog")

mainwin.show_all()
textwin.show_all()
aboutwin.show_all()

Gtk.main()



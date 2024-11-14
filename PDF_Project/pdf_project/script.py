import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="Hello GTK")
        self.set_default_size(200, 100)
        self.set_border_width(10)
        button = Gtk.Button(label="Click Me")
        button.connect("clicked", self.on_button_clicked)
        self.add(button)

    def on_button_clicked(self, widget):
        print("Hello, World!")

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
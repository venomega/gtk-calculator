import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

numbers = [ ord(i) for i in "0123456789+-*/=()"]

class Main():
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("layout.glade")
        builder.connect_signals(self)
        self.buffer = ""
        self.root = builder.get_object("root_calc")
        self.screen = builder.get_object("screen")
        self.root.show_all()
        Gtk.main()

    def update_screen(self):
        if self.buffer == "":
            self.screen.set_label("0")
        else:
            self.screen.set_label(self.buffer)

    def result(self):
        self.buffer = str(eval(self.buffer))
    #SIGNALS
    def on_event(self,x, keys):
        ascii = keys.get_keyval()[-1]
        release = 9
        status = keys.get_event_type().real
        #on any char in numbers, it will display it
        if ascii in numbers and release == status :
            self.on_button(None, ascii.to_bytes(1,"little").decode())
        #on backspace it will remove last char from buffer
        if ascii == 65288 and release == status:
            self.on_button(None, "<-")
        #on space it will clean the buffer
        if ascii == 32 and release == status:
            self.buffer = ""
            self.update_screen()

    def quit(self, widget):
        Gtk.main_quit()

    def on_button(self, widget, num = ""):
        if num == "":
            value = widget.get_label()
        else:
            value = num
        if value == "=":
            self.result()
        elif value != "<-":
            self.buffer += value
        else:
            self.buffer = self.buffer[:-1]
        self.update_screen()


if __name__ == "__main__":
    exit(o := Main())

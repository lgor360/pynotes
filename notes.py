import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

def openm(w, event, menu):
    if event.button == 3: # Right-click
        menu.popup(None, None, None, None, event.button, event.time)


def setti(w, label):
    dialog = Gtk.Dialog("edit note", None, 0,
                        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                         Gtk.STOCK_OK, Gtk.ResponseType.OK))


    input_box = Gtk.TextView()
    lt = label.get_text()
    tb = input_box.get_buffer()
    tb.set_text(lt)
    dialog.vbox.pack_start(input_box, True, True, 0)


    dialog.set_default_size(200, 70)
    dialog.set_resizable(False)
    dialog.show_all()


    response = dialog.run() # Wait for user response


    if response == Gtk.ResponseType.OK:
        bufferi = input_box.get_buffer()
        si, ei = bufferi.get_bounds()
        user_input = bufferi.get_text(si, ei, True)
        label.set_text(user_input)


    dialog.destroy() # Always destroy the dialog


def main():
    # Create main window
    window = Gtk.Window(title="note")
    window.set_size_request(140, 170)
    window.set_keep_below(True)
    window.set_decorated(False)
    window.set_resizable(False)
    window.set_skip_taskbar_hint(True)


    main_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)


    label = Gtk.Label(label="your note\nright click for settings")
    label.set_line_wrap(True)
    label.set_max_width_chars(25)
    main_box.pack_end(label, True, True, 0)


    bare = Gtk.Menu()

    sett = Gtk.MenuItem(label="edit note")
    sett.connect("activate", lambda w: setti(w, label)) # Use a lambda to pass the label
    bare.append(sett)

    hi = Gtk.MenuItem(label="close")
    hi.connect("activate", Gtk.main_quit)
    bare.append(hi)


    bare.show_all()


    window.add(main_box)
    window.connect("button-press-event", openm, bare)
    window.connect("destroy", Gtk.main_quit)


    window.show_all()
    Gtk.main()


if __name__ == "__main__":
    main()
import os
import tkinter as tk
from tkinter import ttk

import platformdirs
import sv_ttk
import watchdog
import watchdog.observers  # observers is a separate submodule, which isn't imported with watchdog

padding = 30
widget_padding = 5
TITLE = "Ephemeral Screenshots"
SCREENSHOT_FOLDER = os.path.join(platformdirs.user_pictures_dir(), "Screenshots")


def screenshot_taken(_: tk.Event):
    print()


class ScreenshotTaken(watchdog.events.FileSystemEventHandler):
    def on_any_event():
        print("Test!")


if __name__ == "__main__":
    observer = watchdog.observers.Observer()
    observer.schedule(watchdog.events.FileCreatedEvent, SCREENSHOT_FOLDER)
    observer.start()

    root = tk.Tk()
    root.title(TITLE)

    frame = tk.Frame()
    frame.grid(padx=padding, pady=padding)

    lbl_status = ttk.Label(text="No screenshot detected...", master=frame)
    btn_screenie = ttk.Button(text="Take Screenshot", master=frame)
    btn_screenie.bind("<Button-1>", screenshot_taken)

    lbl_status.pack(padx=widget_padding, pady=widget_padding)
    btn_screenie.pack(padx=widget_padding, pady=widget_padding)

    sv_ttk.set_theme("dark")
    root.mainloop()

    observer.stop()
    observer.join()

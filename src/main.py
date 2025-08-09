import os
import threading

from PIL import Image
import platformdirs
import pystray
import send2trash
from watchdog.events import FileCreatedEvent, FileSystemEventHandler
from watchdog.observers import Observer

padding = 30
widget_padding = 5
TITLE = "Ephemeral Screenshots"
SCREENSHOT_FOLDER = os.path.join(platformdirs.user_pictures_dir(), "Screenshots")


def annihilate_file(path: str, **_):
    send2trash.send2trash(path)
    print(f"Annihilated {path}")


class ScreenshotTaken(FileSystemEventHandler):
    def on_created(self, event: FileCreatedEvent):
        print(f"{event.src_path} detected, annihilating in 10 seconds")
        threading.Timer(10, annihilate_file, args=[event.src_path]).start()


if __name__ == "__main__":
    observer = Observer()
    screenshot_handler = ScreenshotTaken()
    observer.schedule(screenshot_handler, SCREENSHOT_FOLDER)
    observer.start()

    with open("icon.png", "rb") as f:
        icon = pystray.Icon(TITLE, Image.open(f))

        icon.menu = pystray.Menu(
            pystray.MenuItem(TITLE, enabled=False, action=lambda: None),
            pystray.MenuItem("Quit", lambda: icon.stop()),
        )
        icon.run()

    observer.stop()
    observer.join()

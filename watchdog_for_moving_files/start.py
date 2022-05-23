# import the modules
import os
import time
from os.path import exists
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def move_files(path_to_watch, path_to_destination):
    dir_list = os.listdir(path_to_watch)
    for fname in dir_list:
        source = path_to_watch + '/' + fname
        target = path_to_destination + '/' + fname
        file_exits = exists(path_to_watch)
        if file_exits == True:
            print(f"moved: {fname}")
            os.rename(source, target)

class movehandler(FileSystemEventHandler):
    def on_modified(self, event):
        dir_list = os.listdir(path_to_watch)
        move_files(path_to_watch, path_to_destination)



path_to_watch = "/run/user/1000/gvfs/smb-share:server=192.168.0.108,share=p2p/complete"
path_to_destination = "/run/user/1000/gvfs/smb-share:server=192.168.0.108,share=public/Nas_Xujintao/Videos"
# path_to_watch = "/home/XuJintao/Downloads/source"
# path_to_destination = "/home/XuJintao/Downloads/destination"

move_files(path_to_watch, path_to_destination)

event_handler = movehandler()

# Initialize Observer
observer = Observer()
observer.schedule(event_handler, path_to_watch, recursive=False)

# Start the observer
observer.start()
try:
    while True:
        # Set the thread sleep time
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
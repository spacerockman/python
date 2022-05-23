# import the modules
import os
import time
from os.path import exists
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
  
class movehandler(FileSystemEventHandler):
    def on_modified(self, event):
        dir_list = os.listdir(path_to_watch)
        for fname in dir_list:
            source = path_to_watch + '/' + fname
            target = path_to_destination + '/' + fname
            file_exits = exists(path_to_watch)
            if file_exits == True:
                os.rename(source, target)

path_to_watch = "/run/user/1000/gvfs/smb-share:server=192.168.0.108,share=p2p/complete"
path_to_destination = "/run/user/1000/gvfs/smb-share:server=192.168.0.108,share=public/Nas_Xujintao/Videos"
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
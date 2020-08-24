import watchdog
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

class ChangeHandler(FileSystemEventHandler):
    # すべてのイベント
    def on_any_event(self, event):
        pass
        #print('[全て]',event)

    # 作成された時のイベント
    def on_created(self, event):
        print('[作成]',event)

    # 変更されたときのイベント
    def on_modified(self, event):
        print('[変更]', event)

    # 削除された時のイベント
    def on_deleted(self, event):
        print('[削除]',event)

    # 移動した時のイベント
    def on_moved(self, event):
        print('[移動]',event)

def watchdog_func(target_dir):
    while 1:
            event_handler = ChangeHandler()
            observer = Observer()
            observer.schedule(event_handler, target_dir, recursive=True)
            observer.start()
            observer.join()

watchdog_func("./")

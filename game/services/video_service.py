import pyray

class VideoService:
    def __init__(self):
        pass
    def open_window(self):
        pyray.init_window(800, 450, "Hello Jake")
        pyray.set_target_fps(60)
    def is_window_open(self):
        return not pyray.window_should_close()
    
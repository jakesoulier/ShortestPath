class Director():
    def __init__(self, video_service):
        self._video_service = video_service
        
    def start_game(self, cast):
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._execute_actions("input", cast)
    def _execute_actions(self, group, cast):
        # actions = 
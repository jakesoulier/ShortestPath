class Cast:
    def __init__(self):
        self._actors = {}
        
    def add_actor(self, group, actor):
        if not group in self._actors.keys():
            self._actors[group] = []
        if not actor in self._actors[group]:
            self._actors[group].append(actor)
    
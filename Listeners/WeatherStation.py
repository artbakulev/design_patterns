import time

from Listeners.abstract import Observe
from Listeners.utils import generate_data


class WeatherStation(Observe):

    def __init__(self, init_data=None):
        self._data = init_data
        self._listeners = []
        self._is_changed = False
        self._is_running = False

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
        self.set_changed()
        self.notify_listeners()

    def notify_listeners(self):
        if not self._is_changed:
            return
        for listener in self._listeners:
            listener.update(self._data)

    def set_changed(self):
        self._is_changed = True

    def add_listener(self, listener):
        self._listeners.append(listener)

    def remove_listener(self, listener):
        self._listeners.remove(listener)

    def run(self):
        self._is_running = True
        while self._is_running:
            time.sleep(1)
            print('Receiving data...')
            self.data = generate_data(mock=True)

    def stop(self):
        self._is_running = False

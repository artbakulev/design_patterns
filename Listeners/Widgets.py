import time

from Listeners.WeatherStation import WeatherStation
from Listeners.abstract import Listener, Widget


class CurrentTemperatureWidget(Listener, Widget):
    def __init__(self, init_temperature=None):
        self._temperature = init_temperature

    def display(self):
        print(f'Current temperature is {self._temperature}C')

    def update(self, data):
        self._temperature = data.get('temperature', self._temperature)
        self.display()


class CurrentHumidityWidget(Listener, Widget):
    def __init__(self, init_humidity=None):
        self._humidity = init_humidity

    def display(self):
        print(f'Current humidity is {self._humidity}%')

    def update(self, data):
        self._humidity = data.get('humidity', self._humidity)
        self.display()


class CurrentWindSpeedWidget(Widget):
    def __init__(self, station: WeatherStation):
        self.station = station
        self._wind_speed = station.data.get('wind_speed', None) if \
            station.data is not None else None
        self._displays_number = 0
        self._is_running = False

    def display(self):
        print(f'{self._displays_number}. '
              f'Current wind speed is {self._wind_speed} mps')

    def run(self):
        self._is_running = True
        while self._is_running:
            time.sleep(1)
            self._wind_speed = self.station.data.get('wind_speed', None) if \
                self.station.data is not None else None
            self.display()
            self._displays_number += 1

    def stop(self):
        self._is_running = False

from Listeners.WeatherStation import WeatherStation
from Listeners.Widgets import CurrentTemperatureWidget, CurrentHumidityWidget, \
    CurrentWindSpeedWidget
import threading


if __name__ == '__main__':
    weather_station = WeatherStation()

    temperature_widget = CurrentTemperatureWidget()
    humidity_widget = CurrentHumidityWidget()

    weather_station.add_listener(temperature_widget)
    weather_station.add_listener(humidity_widget)

    wind_speed_widget = CurrentWindSpeedWidget(weather_station)
    wind_speed_widget_thread = threading.Thread(target=wind_speed_widget.run)
    wind_speed_widget_thread.start()

    weather_station.run()

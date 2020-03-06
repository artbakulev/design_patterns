import random


def generate_data(temperature=None, humidity=None, wind_speed=None,
                  mock=False):
    if mock:
        return _generate_data_dict(random.randint(-30, 30),
                                   random.randint(0, 100),
                                   random.randint(0, 30))
    return _generate_data_dict(temperature, humidity, wind_speed)


def _generate_data_dict(temperature, humidity, wind_speed):
    return {
        'temperature': temperature,
        'humidity': humidity,
        'wind_speed': wind_speed,
    }

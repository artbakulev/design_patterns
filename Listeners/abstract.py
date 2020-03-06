from abc import abstractmethod


class Widget:
    @abstractmethod
    def display(self):
        """отображает информацию"""


class Observe:
    @abstractmethod
    def notify_listeners(self):
        """оповещает подписчиков"""

    @abstractmethod
    def set_changed(self):
        """устанавливает флаг при необходимости оповещения"""

    @abstractmethod
    def add_listener(self, listener):
        """регистрирует слушателя"""

    @abstractmethod
    def remove_listener(self, listener):
        """отписывает слушателя"""


class Listener:
    @abstractmethod
    def update(self, data):
        """метод, вызываемый для оповещения"""

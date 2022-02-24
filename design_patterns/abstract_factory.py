from __future__ import annotations
from abc import ABC, abstractmethod


"""
Basic class of abstract factory
"""


class GUIFactory(ABC):
    @abstractmethod
    def create_window(self) -> Window:
        pass

    @abstractmethod
    def create_main_menu(self) -> MainMenu:
        pass

    @abstractmethod
    def get_os_version(self) -> str:
        pass


"""
Windows Factory:
- create window for win os
- create main menu for win os
- stores version of os
"""


class WinFactory(GUIFactory):
    def create_window(self) -> WinWindow:
        return WinWindow()

    def create_main_menu(self) -> WinMainMenu:
        return WinMainMenu()

    def get_os_version(self) -> str:
        return "Windows 11"


"""
Mac OS Factory:
- create window for mac os
- create main menu for mac os
- stores version of os
"""


class MacFactory(GUIFactory):
    def create_window(self) -> MacWindow:
        return MacWindow()

    def create_main_menu(self) -> MacMainMenu:
        return MacMainMenu()

    def get_os_version(self) -> str:
        return "MacOS"


"""
Elements of UI:
- Window
- Main menu
"""


class Window(ABC):
    @abstractmethod
    def init_window(self) -> str:
        pass


class MainMenu:
    @abstractmethod
    def init_menu(self) -> str:
        pass


"""
Window | Initialization for every os
"""


class WinWindow(Window):
    def init_window(self) -> str:
        success_output = "Windows | window has been initialized"
        return success_output


class MacWindow(Window):
    def init_window(self) -> str:
        success_output = "MacOS | window has been initialized"
        return success_output


"""
Main menu | Initialization for every os
"""


class WinMainMenu(MainMenu):
    def init_menu(self) -> str:
        success_output = "Windows | main menu has been initialized"
        return success_output


class MacMainMenu(MainMenu):
    def init_menu(self) -> str:
        success_output = "MacOS | main menu has been initialized"
        return success_output


"""
Client class, that's using abstract factory for creating GUI
"""


class Application:
    def __init__(self, factory: GUIFactory):
        self.factory = factory
        self.os_version = self.factory.get_os_version()

    def __str__(self):
        return f"{self.os_version} application"

    def create_gui(self):
        window = self.factory.create_window()
        menu = self.factory.create_main_menu()
        # Print a result
        print(f"\n{self.os_version}:")
        print(window.init_window())
        print(menu.init_menu())


"""
Testing part
"""


if __name__ == '__main__':
    mac_application = Application(MacFactory())
    mac_application.create_gui()

    win_application = Application(WinFactory())
    win_application.create_gui()



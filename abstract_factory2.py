from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Dialog(ABC):
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        print('Renderizamiento boton en Windows')

class WindowsDialog(Dialog):
    def render(self):
        print('Renderizamiento boton en Windows')

class MacOSButton(Button):
    def render(self):
        print('Renderizamiento boton en Mac')

class MacOSDialog(Dialog):
    def render(self):
        print('Renderizamiento boton en Mac')

class UIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass
    @abstractmethod
    def create_dialog(self):
        pass

class WindowsUIFactory(UIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_dialog(self):
        return WindowsDialog()
    

class MacosUIFactory(UIFactory):
    def create_button(self):
        return  MacOSButton()   
    def create_dialog(self):
        return  MacOSDialog()
    
os_type = "windows"

if os_type == "windows":
    factory = WindowsUIFactory()
elif os_type == "macos":
    factory = MacosUIFactory()

button = factory.create_button()
button.render()

dialog = factory.create_button()
button.render()


from abc import abstractmethod,ABC

class TouchScreenLaptop(ABC):

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass
# Hp Class
class HP(TouchScreenLaptop):

    def scroll(self):
        print("Scroll function implemented")

# HpNotebook Class
class HPNoteBook(HP):

    def click(self):
        print("Clicked function implemented")

# Dell Class
class Dell(TouchScreenLaptop):

    def scroll(self):
        print("Scroll function implemented")

# DellNotebook Class
class DellNoteBook(Dell):

    def click(self):
        print("Clicked function implemented")

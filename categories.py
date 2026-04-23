from stickers import Stickers
from pins import Pins
from lanyards import Lanyards
from shirts import (CanWeDoBetterEarthyGreen, CanWeDoBetterTangyOrange, 
                    CanWeDoBetterCrimsonRed, BruteForceDark, BruteForceLight)
from cards import Cards

class Sticker:
    def __init__(self):
        self._data = {i: 0 for i in Stickers}
        self.random_stickers = {i: 0 for i in Stickers}
        
        self._smiski = [Stickers.S1, Stickers.S2, 
                        Stickers.S3, Stickers.S4]
        self._meme = [Stickers.M1, Stickers.M2, Stickers.M3, 
                      Stickers.M4, Stickers.M5]
        self._retro = [Stickers.R1, Stickers.R2, Stickers.R3, 
                       Stickers.R4, Stickers.R5]
        self._pycpp = [Stickers.PC1, Stickers.PC2]
        self._dcherisse = [Stickers.DC1, Stickers.DC2, 
                           Stickers.DC3, Stickers.DC4]
        self._jji = [Stickers.JI1, Stickers.JI2, Stickers.JI3, 
                     Stickers.JI4, Stickers.JI5, Stickers.JI6]
        
    def print_random_stickers(self):
        print("Note that these values are automatically added to main list!\n")
        print("Gacha Stickers")
        for item, quantity in self.random_stickers.items():
            if quantity != 0:
                print(f"{str(item)}: {quantity}")

    def print_data(self):
        print("Smiski")
        for item, quantity in self._data.items():
            if item in self._smiski:
                print(f"{str(item)}: {quantity}")
        print("")

        print("Retro")
        for item, quantity in self._data.items():
            if item in self._retro:
                print(f"{str(item)}: {quantity}")
        print("")

        print("Meme")
        for item, quantity in self._data.items():
            if item in self._meme:
                print(f"{str(item)}: {quantity}")
        print("")

        print("Python vs C++")
        for item, quantity in self._data.items():
            if item in self._pycpp:
                print(f"{str(item)}: {quantity}")
        print("")

        print("DCS-Chan and Cherisse")
        for item, quantity in self._data.items():
            if item in self._dcherisse:
                print(f"{str(item)}: {quantity}")
        print("")

        print("JJ and Inigo")
        for item, quantity in self._data.items():
            if item in self._jji:
                print(f"{str(item)}: {quantity}")

    @property
    def data(self):
        return self._data
    
    @property
    def smiski(self):
        return [(str(item), quantity) for item, quantity 
                in self._data.items() if item in self._smiski]
    
    @property
    def meme(self):
        return [(str(item), quantity) for item, quantity
                in self._data.items() if item in self._meme]
    
    @property
    def retro(self):
        return [(str(item), quantity) for item, quantity
                in self._data.items() if item in self._retro]
    
    @property
    def pycpp(self):
        return [(str(item), quantity) for item, quantity
                in self._data.items() if item in self._pycpp]
    
    @property
    def dcherisse(self):
        [(str(item), quantity) for item, quantity
                in self._data.items() if item in self._dcherisse]
        
    @property
    def jji(self):
        [(str(item), quantity) for item, quantity
                in self._data.items() if item in self._jji]


class Lanyard:
    def __init__(self):
        self._data: dict[Lanyards, int] = {i: 0 for i in Lanyards}

    @property
    def data(self):
        return self._data
    
    def print_data(self):
        print("Lanyard")
        for item, quantity in self._data.items():
            print(f"{str(item)}: {quantity}")


class Keychain:
    def __init__(self):
        self._data = {"Abbey Road": 0, "Cherisse": 0, "Shadow Gate": 0}

    @property
    def data(self):
        return self._data

    def print_data(self):
        print("Keychain")
        for item, quantity in self._data.items():
            print(f"{item}: {quantity}")


class IdCase:
    def __init__(self):
        self._data = {"Levitate": 0, "Windows XP": 0}
        
    @property
    def data(self):
        return self._data
    
    def print_data(self):
        print("ID Case")
        for item, quantity in self._data.items():
            print(f"{str(item)}: {quantity}")


class Pin:
    def __init__(self):
        self._data: dict[str, int] = {i: 0 for i in Pins}
    
    def print_data(self):
        print("Pins")
        for item, quantity in self._data.items():
            print(f"{str(item)}: {quantity}")

    @property
    def data(self):
        return self._data


class ToteBag:
    def __init__(self):
        self.quantity: int = 0
    
    def print_data(self):
        print("Tote Bag")
        print(f"DCS-Chan: {self.quantity}")
    

class Shirt:
    def __init__(self, green: CanWeDoBetterEarthyGreen, 
                 orange: CanWeDoBetterTangyOrange, 
                 red: CanWeDoBetterCrimsonRed,
                 dark: BruteForceDark,
                 light: BruteForceLight):
        self._green = green
        self._orange = orange
        self._red = red
        self._dark = dark
        self._light = light

    @property
    def green(self):
        return self._green.sizes
    
    @property
    def orange(self):
        return self._orange.sizes
    
    @property
    def red(self):
        return self._red.sizes
    
    @property
    def dark(self):
        return self._dark.sizes
    
    @property
    def light(self):
        return self._light.sizes
    
    def print_data(self):
        print("Can We Do Better")

        for size, quantity in self.green.items():
            print(f"Can We Do Better Green ({size}): {quantity}")
        print("")

        for size, quantity in self.orange.items():
            print(f"Can We Do Better Orange ({size}): {quantity}")
        print("")

        for size, quantity in self.red.items():
            print(f"Can We Do Better Red ({size}): {quantity}")
        print("")

        print("Brute Force Club")

        for size, quantity in self.dark.items():
            print(f"Brute Force Dark ({size}): {quantity}")
        print("")

        for size, quantity in self.light.items():
            print(f"Brute Force Light ({size}): {quantity}")
        print("")


class Pack:
    def __init__(self):
        self.data: dict[str, int] = {str(i):0 for i in Cards}

    def print_data(self):
        print("Overload Packs")
        for pack, qty in self.data.items():
            print(f"{pack}: {qty}")
import pandas as pd
import re
from random import choice
from categories import (Sticker, Pin, ToteBag, 
                        Keychain, Lanyard, IdCase, Shirt)
from shirts import (CanWeDoBetterEarthyGreen, CanWeDoBetterTangyOrange, 
                    CanWeDoBetterCrimsonRed, BruteForceDark, BruteForceLight)
from stickers import Stickers
from lanyards import Lanyards
from pins import Pins

class Merch:
    def __init__(self, data: str):
        self._data = data
        self.sticker = Sticker()
        self.pin = Pin()
        self.totebag = ToteBag()
        self.keychain = Keychain()
        self.lanyard = Lanyard()
        self.idcase = IdCase()
        self.green = CanWeDoBetterEarthyGreen()
        self.orange = CanWeDoBetterTangyOrange()
        self.red = CanWeDoBetterCrimsonRed()
        self.dark = BruteForceDark()
        self.light = BruteForceLight()
        self.shirt = Shirt(self.green, self.orange, 
                           self.red, self.dark, self.light)
    
    @property
    def data(self):
        return self._data
    
    def process_data(self):
        purchased: "pd.Series[str]" = self.get_purchased(self.data)

        for item in purchased:
            products: list[str] = item.splitlines()[:-1]

            for product in products:
                # These are for bundles
                if "Buy 6 Get 7" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    stickers = parameters_str.split(", ")[1:]
                    stickers_clean = self.extract_stickers(stickers)

                    for element in stickers_clean:
                        temp = Stickers(element)
                        self.sticker.data[temp] += 1

                    seventh_pull = self.gacha_sticker([i for i in Stickers])
                    # Add random stickers to main dict
                    self.sticker.data[seventh_pull] += 1

                    # Add to the dict for random stickers
                    self.sticker.random_stickers[seventh_pull] += 1

                elif "Back to School Starter Pack" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    items = parameters_str.split(", ")[1:]
                    bts_clean = self.extract_bts(items)
                    
                    temp_lanyard = Lanyards(bts_clean[0])
                    temp_id_case = bts_clean[1]

                    self.lanyard.data[temp_lanyard] += 1
                    self.idcase.data[temp_id_case] += 1

                elif "Fit Check" in product:
                    parameters = product[11:-1]
                    items = parameters.split(", ")[1:]

                    first_shirt = items[1]
                    size_first_shirt = items[0][-1]
                    if "Earthy Green" in first_shirt:
                        self.shirt.green[size_first_shirt] += 1
                    elif "Tangy Orange" in first_shirt:
                        self.shirt.orange[size_first_shirt] += 1
                    elif "Crimson Red" in first_shirt:
                        self.shirt.red[size_first_shirt] += 1
                    
                    second_shirt = items[3]
                    size_second_shirt = items[2][-1]
                    if "Earthy Green" in second_shirt:
                        self.shirt.green[size_second_shirt] += 1
                    elif "Tangy Orange" in second_shirt:
                        self.shirt.orange[size_second_shirt] += 1
                    elif "Crimson Red" in second_shirt:
                        self.shirt.red[size_second_shirt] += 1

                    third_shirt = items[5]
                    size_third_shirt = items[4][-1]
                    if "Dark" in third_shirt:
                        self.shirt.dark[size_third_shirt] += 1
                    else:
                        self.shirt.dark[size_third_shirt] += 1

                elif "Pins" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    items = parameters_str.split(", ")[1:]
                    quantity: int = int(items[0].split(": ")[1])
                    pin: Pins = Pins(items[1].split(": ")[1])
                    self.pin.data[pin] += quantity

                elif "Tote-ally Cool!" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    temp_shirt = parameters_str.split(", ")[2].split("Shirt: ")[1]
                    size = parameters_str.split(", ")[1].split("Size: ")[1]
                    
                    # Shirt counter
                    if "Crimson Red" in temp_shirt:
                        self.shirt.red[size] += 1
                    elif "Tangy Orange" in temp_shirt:
                        self.shirt.orange[size] += 1
                    else:
                        self.shirt.green[size] += 1

                    # Lanyard counter
                    temp_lanyard = Lanyards(parameters_str.split(", ")
                                            [3].split("Lanyard: ")[1])
                    self.lanyard.data[temp_lanyard] += 1

                    # Tote bag counter
                    self.totebag.quantity += 1

                elif "Lanyard" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    items = parameters_str.split(", ")[1:]
                    quantity = int(items[0].split("Quantity: ")[1])
                    design = Lanyards(items[1].split("Design: ")[1])

                    self.lanyard.data[design] += quantity

                elif "ID Case" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    items = parameters_str.split(", ")[1:]
                    quantity = int(items[0].split("Quantity: ")[1])
                    design = items[1].split("Design: ")[1]

                    self.idcase.data[design] += quantity

                elif "Can We Do Better" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    items = parameters_str.split(", ")[1:]
                    size = items[0].split("Size: ")[1]
                    quantity = int(items[1][-1])
                    color = items[2].split(": ")[1]
                    
                    if color == "Crimson Red":
                        self.shirt.red[size] += quantity
                    elif color == "Earthy Green":
                        self.shirt.green[size] += quantity
                    else:
                        self.shirt.orange[size] += quantity

                elif "Brute Force Club" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    items = parameters_str.split(", ")[1:]
                    size = items[0].split("Size: ")[1]
                    quantity = int(items[1][-1])
                    color = items[2].split(": ")[1]
                    
                    if color == "Light Force":
                        self.shirt.light[size] += quantity
                    else:
                        self.shirt.dark[size] += quantity
                
                elif "Keychains" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    items = parameters_str.split(", ")[1:]
                    design = items[0].split("Design: ")[1]
                    quantity = int(items[1].split("Quantity: ")[1])

                    self.keychain.data[design] += quantity

                # These are for the stickers
                elif "Smiski" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    items = parameters_str.split(", ")[1:]
                    quantity: int = int(items[0].split(": ")[1])
                    sticker: Stickers = Stickers(items[1].split(": ")[1])
                    self.sticker.data[sticker] += quantity

                elif "Meme" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    items = parameters_str.split(", ")[1:]
                    quantity: int = int(items[0].split(": ")[1])
                    sticker: Stickers = Stickers(items[1].split(": ")[1])
                    self.sticker.data[sticker] += quantity

                elif "Retro" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    items = parameters_str.split(", ")[1:]
                    quantity: int = int(items[0].split(": ")[1])
                    sticker: Stickers = Stickers(items[1].split(": ")[1])
                    self.sticker.data[sticker] += quantity

                elif "Python vs C++" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    items = parameters_str.split(", ")[1:]
                    quantity: int = int(items[0].split(": ")[1])
                    sticker: Stickers = Stickers(items[1].split(": ")[1])
                    self.sticker.data[sticker] += quantity

                elif "DCS-Chan and Cherisse" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    items = parameters_str.split(", ")[1:]
                    quantity: int = int(items[0].split(": ")[1])
                    sticker: Stickers = Stickers(items[1].split(": ")[1])
                    self.sticker.data[sticker] += quantity

                elif "JJ and Inigo" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    items = parameters_str.split(", ")[1:]
                    quantity: int = int(items[0].split(": ")[1])
                    sticker: Stickers = Stickers(items[1].split(": ")[1])
                    self.sticker.data[sticker] += quantity

                elif "DCS-Chan" in product:
                    parameters = re.search(r'\((.*?)\)', product)
                    parameters_str = parameters.group(1)
                    qty = int(parameters_str.split(", ")[1][-1])
                    self.totebag.quantity += qty

    def get_purchased(self, data: str) -> "pd.Series[str]":
        df = pd.read_excel(data)
        purchased = df["Kindly select the merch you are willing to avail. Product mock ups are for reference only and may slightly vary.: Products"]
        return purchased

    def extract_stickers(self, data: list[str]) -> list[str]:
        temp: list[str] = []
        for i in data:
            temp.append(i[11:])
        return temp

    def extract_bts(self, data: list[str]) -> list[str]:
        temp: list[str] = []
        for item in data:
            if "Lanyard" in item:
                temp.append(item.split("Lanyard: ")[1])
            elif "ID Case" in item:
                temp.append(item.split("ID Case: ")[1])
        return temp

    def gacha_sticker(self, stickers: list[Stickers]) -> Stickers:
        return choice([i for i in Stickers])

    def print_all_data(self):
        self.sticker.print_data()
        print("")
        self.keychain.print_data()
        print("")
        self.pin.print_data()
        print("")
        self.lanyard.print_data()
        print("")
        self.idcase.print_data()
        print("")
        self.totebag.print_data()
        print("")
        self.shirt.print_data()
        print("")
        self.print_random_stickers()

    def print_random_stickers(self):
        self.sticker.print_random_stickers()

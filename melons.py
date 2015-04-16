"""This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = 0   # TODO, calculate the real amount!

        return total

class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        pass

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Summer", "Winter", "Fall"]

    def get_price(self, qty):
        pass

class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        pass

class SantaClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Winter", "Spring"]

    def get_price(self, qty):
        pass

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Winter", "Spring"]

    def get_price(self, qty):
        pass

class HornedMelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        pass

class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]

    def get_price(self, qty):
        pass

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = "Spring, Summer"

    def get_price(self, qty):
        pass
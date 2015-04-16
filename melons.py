"""This file should have our melon-type classes in it."""

BASE_PRICE = 5



class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = BASE_PRICE * qty
        if qty >= 3:
            total *= 0.75

        return total

class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = BASE_PRICE * qty 

        if qty >= 5:
            total *= 0.5

        return total

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Summer", "Winter", "Fall"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (BASE_PRICE + 1) * 1.5

        return total

class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = BASE_PRICE * qty * 1.5

        return total

class SantaClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Winter", "Spring"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = BASE_PRICE * qty * 1.5

        return total

class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Winter", "Spring"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = BASE_PRICE * qty

        return total

class HornedMelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = BASE_PRICE * qty * 1.5

        return total

class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = BASE_PRICE * qty * 1.5 * 2

        return total

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = "Spring, Summer"

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (BASE_PRICE + 1) * qty

        return total
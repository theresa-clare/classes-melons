"""This file should have our melon-type classes in it."""


class Melon(object):
    def get_base_price(self):
        """Set base price of melons"""
        return 5

class WatermelonOrder(Melon):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""

        total = self.get_base_price() * qty
        if qty >= 3:
            total *= 0.75

        return total

class CantaloupeOrder(Melon):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = self.get_base_price() * qty 

        if qty >= 5:
            total *= 0.5

        return total

class CasabaOrder(Melon):
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Summer", "Winter", "Fall"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (self.get_base_price() + 1) * 1.5

        return total

class SharlynOrder(Melon):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = self.get_base_price() * qty * 1.5

        return total

class SantaClausOrder(Melon):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Winter", "Spring"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = self.get_base_price() * qty * 1.5

        return total

class ChristmasOrder(Melon):
    species = "Christmas"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Winter", "Spring"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = self.get_base_price() * qty

        return total

class HornedMelonOrder(Melon):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = self.get_base_price() * qty * 1.5

        return total

class XiguaOrder(Melon):
    species = "Xigua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = self.get_base_price() * qty * 1.5 * 2

        return total

class OgenOrder(Melon):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = "Spring, Summer"

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        total = (self.get_base_price() + 1) * qty

        return total
"""melons.py -- This file should have our melon-type classes in it."""


class WatermelonOrder(object):
    species = "Watermelon"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Fall', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        price = 5

        if self.species == "Casaba" or self.species == "Ogen":
            price = price + 1
        
        if self.imported == True:
            price = price * 1.5
        
        if self.shape == 'square':
            price = 2 * price
        
        if self.species == "Watermelon" and qty > 2:
            price = 0.75 * price

        if self.species == "Cantaloupe" and qty > 4:
            price = 0.5 * price    

        total = qty * price

        return total


class CantaloupeOrder(object):
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Spring', 'Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        price = 5

        if self.species == "Casaba" or self.species == "Ogen":
            price = price + 1
        
        if self.imported == True:
            price = price * 1.5
        
        if self.shape == 'square':
            price = 2 * price
        
        if self.species == "Watermelon" and qty > 2:
            price = 0.75 * price

        if self.species == "Cantaloupe" and qty > 4:
            price = 0.5 * price    

        total = qty * price

        return total

class CasabaOrder(object):
    species = "Casaba"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Spring', 'Summer',"Fall","Winter"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        price = 5

        if self.species == "Casaba" or self.species == "Ogen":
            price = price + 1
        
        if self.imported == True:
            price = price * 1.5
        
        if self.shape == 'square':
            price = 2 * price
        
        if self.species == "Watermelon" and qty > 2:
            price = 0.75 * price

        if self.species == "Cantaloupe" and qty > 4:
            price = 0.5 * price    

        total = qty * price

        return total

class SharlynOrder(object):
    species = "Sharlyn"
    color = "tan"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        price = 5

        if self.species == "Casaba" or self.species == "Ogen":
            price = price + 1
        
        if self.imported == True:
            price = price * 1.5
        
        if self.shape == 'square':
            price = 2 * price
        
        if self.species == "Watermelon" and qty > 2:
            price = 0.75 * price

        if self.species == "Cantaloupe" and qty > 4:
            price = 0.5 * price    

        total = qty * price

        return total


class SantaClausOrder(object):
    species = "Santa Claus"
    color = "green"
    imported = True
    shape = 'natural'
    seasons = ['Winter','Spring']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        price = 5

        if self.species == "Casaba" or self.species == "Ogen":
            price = price + 1
        
        if self.imported == True:
            price = price * 1.5
        
        if self.shape == 'square':
            price = 2 * price
        
        if self.species == "Watermelon" and qty > 2:
            price = 0.75 * price

        if self.species == "Cantaloupe" and qty > 4:
            price = 0.5 * price    

        total = qty * price

        return total


class ChristmasOrder(object):
    species = "Christmas"
    color = "green"
    imported = False
    shape = 'natural'
    seasons = ['Winter']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        price = 5

        if self.species == "Casaba" or self.species == "Ogen":
            price = price + 1
        
        if self.imported == True:
            price = price * 1.5
        
        if self.shape == 'square':
            price = 2 * price
        
        if self.species == "Watermelon" and qty > 2:
            price = 0.75 * price

        if self.species == "Cantaloupe" and qty > 4:
            price = 0.5 * price    

        total = qty * price

        return total


class HornedMelonOrder(object):
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = 'natural'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        price = 5

        if self.species == "Casaba" or self.species == "Ogen":
            price = price + 1
        
        if self.imported == True:
            price = price * 1.5
        
        if self.shape == 'square':
            price = 2 * price
        
        if self.species == "Watermelon" and qty > 2:
            price = 0.75 * price

        if self.species == "Cantaloupe" and qty > 4:
            price = 0.5 * price    

        total = qty * price

        return total


class XiguaOrder(object):
    species = "Xigua"
    color = "black"
    imported = True
    shape = 'square'
    seasons = ['Summer']

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        price = 5

        if self.species == "Casaba" or self.species == "Ogen":
            price = price + 1
        
        if self.imported == True:
            price = price * 1.5
        
        if self.shape == 'square':
            price = 2 * price
        
        if self.species == "Watermelon" and qty > 2:
            price = 0.75 * price

        if self.species == "Cantaloupe" and qty > 4:
            price = 0.5 * price    

        total = qty * price

        return total
        

class OgenOrder(object):
    species = "Ogen"
    color = "tan"
    imported = False
    shape = 'natural'
    seasons = ['Summer',"Spring"]

    def get_price(self, qty):
        """Calculate price, given a number of melons ordered."""
        price = 5

        if self.species == "Casaba" or self.species == "Ogen":
            price = price + 1
        
        if self.imported == True:
            price = price * 1.5
        
        if self.shape == 'square':
            price = 2 * price
        
        if self.species == "Watermelon" and qty > 2:
            price = 0.75 * price

        if self.species == "Cantaloupe" and qty > 4:
            price = 0.5 * price    

        total = qty * price

        return total
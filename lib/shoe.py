#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        if not isinstance(size, int):
            print("size must be an integer")
        else:
            self.size = size
            self.condition = "New"

    def repair(self):
        print("The shoe has been repaired.")
        self.condition = "New"

    def cobble(self):
        print("Your shoe is as good as new!")

# Example usage:
my_shoe = Shoe("Nike", 10)
my_shoe.repair()
my_shoe.cobble()

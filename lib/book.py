#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        if not isinstance(page_count, int):
            raise ValueError("page_count must be an integer")
        else:
            self.page_count = page_count
            self.condition = "New"

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

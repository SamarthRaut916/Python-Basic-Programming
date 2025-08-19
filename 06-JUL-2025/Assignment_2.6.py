# Base class
class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id

    def display_info(self):
        print(f"{self.title} (ID: {self.item_id})")

# Subclasses
class Book(LibraryItem):
    def __init__(self, title, item_id, author):
        super().__init__(title, item_id)
        self.author = author

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}")

class DVD(LibraryItem):
    def __init__(self, title, item_id, duration):
        super().__init__(title, item_id)
        self.duration = duration

    def display_info(self):
        super().display_info()
        print(f"Duration: {self.duration} min")

# Library class
class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def show_items(self):
        for item in self.items:
            item.display_info()
            print("-" * 20)

# Example usage
library = Library()
library.add_item(Book("1984", "B001", "George Orwell"))
library.add_item(DVD("Inception", "D001", 148))
library.show_items()

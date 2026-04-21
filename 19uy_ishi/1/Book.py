import json
class Book:
    cnt = 0
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        Book.cnt += 1

    def __str__(self):
        return f'Kitob: "{self.title}", Muallif: {self.author}, Yil: {self.year}'
    
    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title
        return False
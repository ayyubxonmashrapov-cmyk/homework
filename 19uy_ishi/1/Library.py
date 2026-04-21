from Book import Book
from EBook import EBook
import json

class Library:
    
    def __init__(self, owner):
        self.owner = owner

    def add_book(self, book):
        self.__save(book)

    def __load(book):
        with open("books.json", "r") as fayl:
            return json.load(fayl)
        
    def __save(self, book):
        data = []
        data.extend(self.__load())
        if isinstance(book, Book):
            data.append({"name": book.title, "author": book.author, "year": book.year})
        elif isinstance(book, EBook):
            data.append({"name": book.title, "author": book.author, "year": book.year, "MB": book.mb})
        with open("books.json", "w") as fayl:
            json.dump(data, fayl, indent=4, ensure_ascii=False)
        print(f"Kitob kutubxonaga qo'shildi: {book.title}\n→ Kutubxona faylga saqlandi: {book.title}")
        

    def printf(self):
        data = self.__load()
        for book in data:
            print(book)       
    
    def __contains__(self, book_name):
        data = self.__load()
        for name in data:
            if book_name == name["name"]:
                print("kitob kutubxonoda bor")
                return True
        return False    
    
    def __len__(self):
        data = self.__load()
        return len(data)
    
    
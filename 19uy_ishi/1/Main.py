from Library import Library
from Book import Book
from EBook import EBook

book1 = Book("Sariq devni minib", "X. To'xtaboyev", 1974)
book2 = Book("Dunyo ishlari", "O. Hoshimov", 1982)
ebook1 = EBook("Python Dasturlash", "B. Karimov", 2023, 2.8)
ebook2 = EBook("AI Revolyutsiyasi", "D. Hasanov", 2024, 5.1)
print(f"Kitob yaratildi: {book1.title} ({book1.author}, {book1.year})")
print(f"Kitob yaratildi: {ebook1.title} ({ebook1.author}, {ebook1.year}), hajmi: {ebook1.mb}")
print(f"{Book.cnt} ta kitob muvaffaqiyatli yaratildi.")
print(book1)
print(ebook1)
library = Library("Ayyub")
library.add_book(book1)
library.add_book(ebook1)
library.add_book(book2)
print(library)
print("Sariq devni minib" in library)
print("Dunyo ishlari" in library)
print(f"Kutubxonadagi kitoblar soni: {len(library)} ta")
book1 == Book("Sariq devni minib", "Boshqa Muallif", 2000)
book1 == book2
class Library:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.members = {}
        self.books = {}

    def addbook(self, book, quantity):
        if quantity < 1:
            return False
        if book in self.books:
            self.books[book] += quantity
        else: 
            self.books[book] = quantity
        return True
    
    def lendBook(self, member, book):
        if book not in self.books or self.books[book] == 0:
            return False
        if member in self.members:
            self.members[member].append(book)
            self.books[book] -= 1
        else:
            self.members[member] = []
            self.members[member].append(book)
            self.books[book] -= 1

    def returnBook(self, member, book):
        if member in self.members:
            if book in self.members[member]:
                self.members[member].remove(book)
                self.books[book] += 1


lib = Library(1, "Central Library")

print(lib.addbook("Python", 3))
print(lib.addbook("Java", 2))

print(lib.lendBook("Ali", "Python"))
print(lib.lendBook("Ali", "Python"))
print(lib.lendBook("Vali", "Java"))

print(lib.books)
print(lib.members)

print(lib.returnBook("Ali", "Python"))

print(lib.books)
print(lib.members)

        
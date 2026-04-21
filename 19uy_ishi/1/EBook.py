from Book import Book

class EBook(Book):
    def __init__(self, title, author, year, mb):
        super().__init__(title, author, year)
        self.mb = mb

    def __str__(self):
        return f'Elektron kitob: "{self.title}", Muallif: {self.author}, Yil: {self.year}, Hajmi: {self.mb}MB'


        

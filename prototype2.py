import copy
from abc import ABC, abstractmethod

class Document(ABC):
    def __init__(self, title, content):
        self.title = title
        self.content = content


    @abstractmethod
    def clone(self):
        pass

    def __str__(self):
        return f"Title: {self.title} Content: {self.content}"
    

class Article(Document):
    def __init__(self, title, author, content):
        super().__init__(title, content)
        self.author = author

    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return super().__str__() + f" Author: {self.author}"
    

class SpreadSheet(Document):

    def __init__(self, title,rows, content, columns):
        super().__init__(title, content)

        self.rows = rows
        self.columns = columns

    def clone(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return super().__str__() + f" Rows: {self.rows} Columns: {self.columns}"
    
artitle_prototype = Article("Title", "Author", "Content")
spreadsheet_prototype = SpreadSheet("Spreadsheet" , "Content", 10, 5)

artitle1 = artitle_prototype.clone()
artitle1.title = "Calidad de Software"
artitle2 = artitle_prototype.clone()
artitle2.title = "Inteligencia Artificial"


print(artitle1)
print(artitle2)

spreadsheet1 = spreadsheet_prototype.clone()
spreadsheet1.title = "Pagos"
spreadsheet1.rows = 20
spreadsheet2 = spreadsheet_prototype.clone()
spreadsheet2.title = "Ingresos"
spreadsheet2.rows = 10

print(spreadsheet1)
print(spreadsheet2)
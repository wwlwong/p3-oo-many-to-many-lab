class Author:
    
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        contract_list = []
        for contract in Contract.all:
            if contract.author == self:
                contract_list.append(contract)
        return contract_list

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        royalties_sum = 0
        for contract in self.contracts():
            royalties_sum += contract.royalties
        return royalties_sum



class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        contract_list = []
        for contract in Contract.all:
            if contract.book == self:
                contract_list.append(contract)
        return contract_list

    def authors(self):
        return [contract.author for contract in self.contracts()]

   


class Contract:
    
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, Author):
            self._author = value
        else:
            raise Exception("Author must be an instance of Author class")

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of Book class")
        self._book = value
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string type")
        self._date = value
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer")
        self._royalties = value

    @classmethod
    def contracts_by_date(cls):
        sorted_contracts = []
        for contract in cls.all:
            sorted_contracts.append(contract)
        
        sorted_contracts = sorted(sorted_contracts, key=lambda x: x.date)

        return sorted_contracts
            

        



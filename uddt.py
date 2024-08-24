class Client:
    def __init__(self, name, id, credit, address):
        self.name = name
        self.id = id
        self.credit = credit
        self.address = address
        
    def __str__(self):
        return f"the name is {self.name} \n the id is {self.id} \n the credit limit is {self.credit} \n the address is {self.address}"
    
p1 = Client("Lisa","12345",3000000,"Ottawa, Canada")
p2 = Client("Luis","12346",15000000,"Ontario, Canada")
p3 = Client("Sarah","12347",4500000,"New York, US")

print(p1)
print(p2)
print(p3)
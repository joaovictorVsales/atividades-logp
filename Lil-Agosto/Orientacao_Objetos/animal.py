class Animal:
    def __init__(self,nome:str):
        self.nome = nome
    
    def emitir_som(self):
        return "som generico"
    
class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au!"
    
    def latir(self):
        return "Woof woof!"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
    def miar(self):
        return "Meow meow!"
    
dog = Cachorro("Totó")
cat = Gato("Tom")

print(dog.emitir_som())
print(dog.latir())

print(cat.miar())
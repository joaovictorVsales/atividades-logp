class Veiculo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

    def exibir_detalhes(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}"
    
class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, num_portas: int):
        super().__init__(marca, modelo)  
        self.num_portas = num_portas

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nNúmero de portas: {self.num_portas}"
    
class Moto(Veiculo):
    def __init__(self, marca:str, modelo:str, cilindradas:int):
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\n Numero de cilindros: {self.cilindradas}"

carros = [
    {"marca": "Toyota", "modelo": "Corolla",  "num_portas": 4},
    {"marca": "Honda", "modelo": "Civic",  "num_portas": 4},
    {"marca": "Ford", "modelo": "Mustang",  "num_portas": 2},
    {"marca": "Chevrolet", "modelo": "Onix",  "num_portas": 4},
    {"marca": "Volkswagen", "modelo": "Golf GTI",  "num_portas": 4}
]

motos = [
    {"marca": "Honda", "modelo": "CG 160", "cilindros": 1},
    {"marca": "Yamaha", "modelo": "Fazer 250", "cilindros": 1},
    {"marca": "Kawasaki", "modelo": "Ninja 400", "cilindros": 2},
    {"marca": "BMW", "modelo": "G 310 R", "cilindros": 1},
    {"marca": "Suzuki", "modelo": "GSX-S750", "cilindros": 4}
]

for carro in carros:
    CarDet = Carro(carro['marca'],carro['modelo'],carro['num_portas'])
    print(f"{CarDet.exibir_detalhes()}\n")
for moto in motos:
    MotoDet = Moto(moto['marca'],moto['modelo'],moto['cilindros'])
    print(f"{MotoDet.exibir_detalhes()}\n")
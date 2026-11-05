class Componente:
    def __init__(self, codice: str, nome: str, peso_kg: float) -> None:
        self.codice = codice
        self.nome = nome
        self.peso_kg = peso_kg
        
    def __str__(self) -> str:
        print(f"codice: {self.codice}, nome: {self.nome}, peso: {self.peso_kg} kg")
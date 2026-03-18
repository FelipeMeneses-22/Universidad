class Nadador:
    def nadar(self):
        return f"Nadando"

class Volador:
    def volar(self):
        return f"Volando"

class Pato(Nadador, Volador):
    def sonido(self):
        return f"Cuak"
    
class Paloma(Volador):
    def  ruido(self):
        return f"Bebesita brrrr"


print("___________________________\n")
animal1 = Pato()
print(animal1.nadar())
print(animal1.volar())
print(animal1.sonido())

print("___________________________\n")
animal = Paloma()
print(animal.ruido())
print("___________________________\n")
message = "a vida!"
palavra = "nossa"
fala_completa = (f"{message} {palavra}")
print(message)
print(message.title())
print(message.lower())
print(message.upper())
print(f"{fala_completa} é tudo de bom!")
sentimentos = ("\n\tAmor\n\tAlegria\n\tForça\n\tFé\n\tJustiça\n\tHonestidade\n\tUnião\n\tConfiança\n\tVerdade")
print(f"\tLista de sentimentos:{sentimentos}")
##########
x = 10
y = 3
multiplicar = x * y / 3
print(multiplicar)
#########
def __init__(self, multiplicando, multiplicador):
    self.multiplicando = multiplicando
    self.multiplicador = multiplicador
    self.resultado = self.multiplicando * self.multiplicador
    return self.resultado

    
def main():
    multiplicando_1 = 10
    multiplicador_1 = 3
    multiplicando_2 = 20
    multiplicador_2 = 5
    multiplicando_3 = 15
    multiplicador_3 = 2
    resultado_1 = multiplicando_1 * multiplicador_1
    resultado_2 = multiplicando_2 * multiplicador_2
    resultado_3 = multiplicando_3 * multiplicador_3
    print(f"O valor encontrado é {resultado_1}, {resultado_2}, {resultado_3}")
    
if __name__=="__main__":
    main()
#insert, del, pop, remove, append, len, removeprefix, removesuffix, sort, sorted, reverse, min, max, sum:
fruits = ["banana","apple","orange","watermelon","penaple","melon"]
fruits.insert (0, "blueberry")
print(fruits)

poped_fruit = fruits.pop (0)
print(fruits)
print(poped_fruit)
fruits.append(poped_fruit)
print(fruits)
print(len(fruits))
del fruits [1]
print(fruits)
fruits.remove("banana")
print(fruits)
print(len(fruits))

name = "astrogildo"
print(name.removesuffix("do"))
print(name.removeprefix("astro"))
print(name.title())

numbers = [2, 5, 3, 8, 9, 11, 15, 10]
print(numbers)
print(sorted(numbers, reverse=True))
print(numbers)
numbers.sort()
print(numbers)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(numbers [1:6])
print(numbers [2:])
print(numbers [-1:])

guest_names = ["clara","rafael","debora","maria", "maria clara",""]
for name in guest_names:
    print(f"{name.title()}, voce e protegido(a) e amado(a) por Deus!")
pessoa = "rafael"
print(f"Óla {pessoa}, seja bem vindo! você esta no caminho certo! continuir!")
print(f"Óla {pessoa.upper()}!")
print(f"Óla {pessoa.lower()}!")
print(f"Óla {pessoa.title()}")
print('"A ciência é, portanto, uma perversão de si mesma, a menos que tenha como fim último, melhorar a humanidade."')
famous_person = "Nikola Tesla"
message = '"A ciência é, portanto, uma perversão de si mesma, a menos que tenha como fim último, melhorar a humanidade."'
print(message)
nome = "\tclarinha é fofa.\n\té o amor de pai.\n\té a felicidade de pai!" 
print(nome.title())
nome_2= " Clarinha "
print(nome_2)
print(nome_2.rstrip())
print(nome_2.lstrip())
print(nome_2.strip())
filename = "python_notes.txt"
print(filename.removesuffix("txt"))
print(filename.removeprefix("python"))
#Exercicos números
print(5+3)#adição
print(10-2)#subtração
print(4*2)#multiplicação
print(16/2)#divisão
favorite_number = 7
print(f"Eu escolho o número {favorite_number}, pois é o número que representa o dia citado por DEUS reservado para o descanso.")
#Exercicios list_in_python
names = ["rafael", "debora", "maria", "clara", "caio", "santos", "araujo"]
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
print(names[4].title())
print(names[5].title())
print(names[6].title())
message = f"My name is {names[0].title()}, i am married with {names[1].title()}. We have a daughter, your name is {names[2].title()} and i want to continue living happy with them!"
print(message)
guests_list = ["natalia","maria","debora","audra"]
for i in guests_list:
    print("{} voce foi convidada para festa! Contamos  com a sua presenca!".format(i).title())
print(f"A convidada {guests_list[0].title()}, nao podera comparecer!")
not_coming = guests_list.pop(0)
guests_list.insert(0,"Clara")
print(guests_list)
print(not_coming.title())
for i in guests_list:
    print("{}, voce foi convidada para festa! Contamos com a sua presenca!".format(i).title())
for i in guests_list:
    print("{} encontramos novos lugares, por isso teremos 3 concites a mais.".format(i).title())
guests_list.insert(0,"bruna")
guests_list.insert(2,"roberta")
guests_list.append("vitoria")
print(guests_list)
for i in guests_list:
    print("{} voce esta convidada para a festa! Contamos com a sua presenca".format(i).title())
    print("{} houve uma CHANGE e temos apenas 2 lugares na festa.Sorry".format(i).title())

print(guests_list)
removing_bruna = guests_list.pop(0)
print(guests_list)
removing_roberta = guests_list.pop(1)
print(guests_list)
removing_vitoria = guests_list.pop()
print(guests_list)
removing_audra = guests_list.pop()
print(guests_list)
removing_clara = guests_list.pop(0)
print(guests_list)

guests_canceled = [removing_audra,removing_bruna, removing_clara, removing_vitoria, removing_roberta]
print(guests_canceled)
for i in guests_canceled:
    print("{} seu convite foi cancelado pela falta de lugares disponiveis.".format(i).title())
print(guests_list)
for i in guests_list:
    print("{} voce ainda esta convidada para a festa! Te espero la.".format(i).title())
del guests_list [-1]
print(guests_list)
del guests_list[0]
print(guests_list)
print("A lista esta vazia!")

locais = ["estados unidos","portugal","italia","china","japao","peru"]
print("Lista original:")
print(locais)
print("\nLista ordenana alfabetica:")
print(sorted(locais))
print("\nLista original novamente:")
print(locais)
print("\nOrdem alfabetica reversa:")
print(sorted(locais, reverse=True))
print("\nLista original novamente:")
print(locais)
print("\nLista usando o reverse:")
locais.reverse()
print(locais)
print("\nRevertendo novamente:")
locais.reverse()
print(locais)
print("\nUsando sort:")
locais.sort()
print(locais)
locais.sort(reverse=True)
print(locais)
print(len(locais))
#erro intencional
t = ["h","d","l"]
print(t[2])

pizzas = ["calabreza","mussarela","portuguesa"]
for pizza in pizzas:
    print(pizza)
    print(f"Gosto de pizza de {pizza.title()}!")
print("Eu amo pizza!")

animals = ["cat","dog","dolphin"]
for animal in animals:
    print(animal.title())
    print(f"{animal.title()} seria um bom animal de estimacao (pet)!")
print("Todos os animais sao mamiferos!")

#exercicios ex 1
algarismos = []
for algarismo in range(1, 21):
    algarismos.append(algarismo)
print(algarismos)
#ex: 2
algarismos = list(range(1, 21))
print(algarismos)

codigos = []
for codigo in range(1, 10001):
    codigos.append(codigo)
print(codigos)
print(min(codigos))
print(max(codigos))
print(sum(codigos))

for codigo in range(1, 21, 3):
    print(codigo)
    
impares = []
for impar in range(3, 30, 3):
    impares.append(impar)
print(impares)

for valor in range(1, 11):
    b = valor**3
    print(b)
y = []
for valor in range (1, 11):
    b = valor**3
    y.append(b)
print(y)

y = [valor**3 for valor in range(1, 11)]
print(y)
    
want_eat = ["pizza","hamburger","feijoada","frutas","chocolate","pop-corn","suco de frutas"]
print("Os tres primeiros elemntos da lista sao:")
print(want_eat[0:3])
print("\nOs tres elemntos que ficam no meio da lista sao:")
print(want_eat[2:5])
print("\nOs tres ultimos elementos da lista sao:")
print(want_eat[-3:])
print("\nExercicios com pizzas:")

pizzas = ["calabreza","mussarela","portuguesa"]
friend_pizzas = (pizzas[:])

pizzas.append("frango")
friend_pizzas.append("atum")

print(pizzas)
print(friend_pizzas)
print("\nMinhas pizzas favoritas sao:")
for pizza in pizzas:
    print(pizza)

print("\nMinhas pizzas favoritas sao:")
for pizza in friend_pizzas:
    print(pizza)
    
foods = []
for pizza in pizzas:
    foods.append(pizza)
print(foods)
foods = [pizza for pizza in pizzas]
print(foods)
foods.append("ice-cream")
print(foods)
favorite_foods = foods[:]
print(foods)
print(favorite_foods)
print("\nMy foods is:")
for food in foods:
    print(food)
print("\nMy favotite foods is:")   
for food in favorite_foods:
    print(food)
    
foods.append("toscana")
favorite_foods.append("churrasco")
print("\nMy food is:")
print(foods)
print("\nMy favorite food is:")
print(favorite_foods)

buffets = ("feijoada","arroz","macaronada","strogonof","file")
print("\nBuffet restaurante:")
for buffet in buffets:
    print(buffet)
print("\nTestando modificar tuplar:erro intensional apresenta TypeError:'tuple' object does not support item assignment!")

print("\nLista de buffet original:")
buffets = ("feijoada","arroz","macaronada","strogonof","file")
for buffet in buffets:
    print(buffet)
print("\nNova lista de buffet:")
buffets = ("feijoada","farofa","acaraje","strogonof","file")
for buffet in buffets:
    print(buffet)
print("\n FIVE TRUE:")
car = "subaru"
print("is car == subaru? I predict True.")
print(car == "subaru")
balls = ["red","blue","green","yellow"]
ball = "yellow"
print(ball in balls)

apple_0 = 12
apple_1 = 13
print(apple_0 >= 11 and apple_1 >= 12)

orange_0 = 14
orange_1 = 16
print(orange_0 >= 15 or orange_1 >= 15)

list_wo = ["car","house","bus","train"]
wo = "airplane"
print(wo not in list_wo)
print("\nFIVE FALSE:")
number_fruits = []
for valor in range (1, 11):
    valor = valor**2
    number_fruits.append (valor)
print(number_fruits)
print(13 in number_fruits)
number_fruits = list (valor**2 for valor in range(1, 11))
print(number_fruits)

number = 15
print(number != 15)

flowers = ["margarida","rosa","tulipa","orquidea"]
print(flowers[1:])
print(flowers[1:3])
print("violeta" in flowers and "dente_de_leao" in flowers)
print("gracha" in flowers or "bem_me_quer" in flowers)

things = [3, 5, 2, 7, 6, 1]
things.sort()
print(things)
things.sort(reverse=True)
print(things)
print(9 in things)

print("Atividade 5.2:")
n = "jeane"
print(n!="jeane")
print(f"{n.title()} nao e diferente de n!")
print(n=="jeane")
print(f"{n.title()} e igual a n!")

digits=16
print(digits != 16)
print(digits == 16)
print(digits >= 17)
print(digits <= 17)
print(digits >= 16 and digits == 16)#ambos devem ser verdadeiros.
print(digits >= 16 or digits == 17)#pelo menos um tem que ser verdadeiro.
#Exercicio if, elif e else:
print("\nExercicios if, elif e else:")
print("Situação 01:")
alien_color = "green"
if alien_color == "green":
    print("You win 5 points for open fire against the alien!")
elif alien_color == "yellow":
    print("You win 10 points!")
elif alien_color == "red":
    print("You win 15 points!")
else:
    print("You lose!")
#Situação 02:    
print("\nSituação 02:")
alien_color = "yellow"
if alien_color == "green":
    print("You win 5 points!")
else:
    print("You lose! Try again!")

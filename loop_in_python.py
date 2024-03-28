magicians = ["harry","hermiony","sauron"]
for magician in magicians:
    print(magician.title())
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick,{magician.title()}.\n")
    x = "you shall not pass!"
print(f"Don't forget {magicians[2].title()}!{x.upper()} by Gandalf!")
print("thank you, everyone. That was a great magic show!")

#O RANGE NÃO IMPRIME O NÚMERO FINAL.
for value in range(1, 6):#instrução range para determinar inicio e final
    print(value)
    
for value in range(6):#instrução determina valor final, neste caso inicia do zero.
    print(value)
    
numbers = list(range(1, 9))#criando listas usando range.
print(numbers)

numbers = list(range(2, 11, 2))
print(numbers)

numbers = list(range(1, 11, 2))
print(numbers)

numbers = list(range(1, 20, 5))
print(numbers)

#ATRIBUINDO FUNÇÕES A LISTA RANGE.
squares = []
for values in range(1, 11):
    square = values**2
    squares.append(square)
print(squares)

numeros_quadrados = []
for values in range(1, 11):
    quadrado = values**2
    numeros_quadrados.append(quadrado)
print(numeros_quadrados)

quadrados = []
for values in range(1, 11):
    quadrados.append(values**2)
print(quadrados)

soma_quadrados = []
for values in range(1, 11):
    soma_quadrados.append(values**2 + values**2 + values**2)
print(soma_quadrados)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))#valor minimo.
print(max(digits))#valor maximo.
print(sum(digits))#valor soma.
#LIST_COMPREHENSIONS/ COMBINA O FOR E CRIA OUTROS ELEMENTOS.
digitos = [value**2 for value in range(1,11)]
print(digitos)  

algarismos = [value**3 for value in range(1, 11)]
print(algarismos)

#fatiando(slicing) permite pegar locais específicos da lista:
persons = ["raquel","sandra","pablo","afonso","rafael"]
print(persons[0: 3])
print(persons[1:4])
print(persons[1:5])#posso usar para pegar até o ultimo elemnto.
print(persons[1:])#caso mantenho o espaço em branco ele tras o ultimo elemento.
print(persons[-3:])
print(persons[-4:])
print(persons[0:5:2])
print("\nThis is my first three persons in my group:")
for person in persons[0:3]:
    print(person.title())
three_persons = []
for person in persons[0:3]:
    three_persons.append(person.title())
print(three_persons)

three_persons = [person for person in persons[0:3]]#list_comprehensions.
three_persons.sort()
print(three_persons)

#copy_the_list
food = ["pizza","hamburg","sorvete","feijoada","salada"]
favorite_food = food [:]#usado para copiar a lista.
print("Algumas comidas:")

print(food)

print("\nCopiando lista algumas comidas:")
print(favorite_food)

food.append ("suco de fruas")
favorite_food.append("chocolate")
print(food)
print(favorite_food)
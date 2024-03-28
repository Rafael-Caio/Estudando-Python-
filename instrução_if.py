#Usando instrumento if: geralmente usado para estabelecer condições.
#Exemplo do uso de if
cars = ["audi","bmw","subaru","toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
#Testes condicionais com if:True or False:
#Exemplo verificando igualdade
#Usando apenas um sinal de igual (=) INDICA que este é o valor da variável (x = "audi") 
#Usando o sinal de 2 iguais (==) VERIFICA se o valor da variável corresponde ao valo estimado (x=="audi")
b = "oculos"
c = "oculos"
d = "camisa"
print(d==c)
print(b==c)
#Envolvendo letras maiusculas e minusculas.
a = "Audi"
print(a=="audi")#Retorna False pois a string da variavel inicial maiuscula. 

a = "Audi"
print(a.lower()=="audi")#o metodo foi acrecido por isso o retorno é True.
print(a)#Mesmo acrescendo o metodo, o valor da variavel (a) não foi alterado.
#Verificando diferença:
requested_topping = "calabresa"
if requested_topping != "mussarela":#(!=)significa diferença
    print("Hold the atum")
    
sabor_solicitado = "chocolate"
if sabor_solicitado != "morango":#se o sabor solicitado for diferente de morango.
    print("Devolver a entrega")
else:
    print("Vamos pedir mais um sabor")
    
sabor_solicitado = "balnilha"
if sabor_solicitado == "balnilha":
    print("Vamos pedir outro sabor")
else:
    print("Eu nao quero")
#Testando valores numericos:
age = 18
print(age == 18)    

answer = 17
if answer != 42:#se a resposta for diferente de 42.
    print("That is not the correct answer. Please try again!")
    
age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)
#Verificando multiplas condições (and, or)
#AND
print("USANDO AND:")
age_0 = 22
age_1 = 18
print("Situacao_01:")
print(age_0 >= 21 and age_1 >= 21)
print("Situacao_02:")
age_1 = 22
print(age_0 >= 21 and age_1 >= 21)
print("Usando parenteses:")
print((age_0 >=21) and (age_1 >= 21))#Pode ser escrito com parenteses, mas ão é obrogatório.
#OR, no caso do "or"pelo menos 1 ou as 2 afirmações devem ser TRUE
print("USANDO OR:")
print("Situacao 01:")
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)
print("Situacao 02:")
age_0 = 18
print(age_0 >= 21 or age_1 >= 21)
#Verificando se um valor esta em uma lista:(in)
print("USANDO IN:")
print("Situacao_01:")
requested_topping = ["mushrooms","onions","pineapple"]
print("mushrooms" in requested_topping)
print("pepperone" in requested_topping)
#Verificando se um valor não esta na lista:
print("USANDO NOT:")
banned_users = ["rafael", "fabiane", "vanessa"]
user = "roberta"
print(user not in banned_users)
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.\n")

#INSTRUÇÕES IF SIMPLES
print("INSTRUÇÃO IF SIMPLES:")
age = 17#A condição para age 19 e agora para age 17.
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!\n")
#Usando if, elif e else: o python executa até a afirmação ser verdadeira, não realizando outros testes. 
print("Situacão 02:")
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admissin cost is $40.")
    
print("Situação 2: codigo mais simples")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.\n")
#Usando multiplos blocos elif:
print("Usando múltiplos blocos elif:")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.\n")
#Omitindo o bloco else:
print("Omitindo o bloco else:")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:#Foi usado para omitir o else.
    price = 20
print(f"Your admission cost is ${price}.,\n")
#Testando Múltiplas condições:neste caso usando apenas if o python testa todas as opções independente da verdadeira.
print("Testando múltiplas  condições:")
requested_toppings = ["mushrooms", "extra cheese"]
if "mushrooms" in requested_toppings:
    print("Adding mushrooms")
if "pepperoni" in requested_toppings:
    print("Adding pepperoni")
if "extra cheese" in requested_toppings:
    print("Adding extra cheese")
print("\nFinished making your pizza!")
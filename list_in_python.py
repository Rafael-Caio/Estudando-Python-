import this
numbers = [0, 1, 2, 3, 4, 5, 6]
names = ["Rafael", "Caio", "Maria", "Paulo", "marcela", "Clara", "Bruna", "Clarinha"] 
print (numbers)
print (names)
print(numbers[0])#[] representa indice, ou seja, posição do item na lista.
print(names[0].upper())
print(names[1].lower())
print(names[2].title())
print(names[2].removeprefix("Ma").upper())
print(names[2].removesuffix("a").upper())
print(names[2], names[5])
print(names[0])
print(names[1])
print(names[0], names[1])
print(names[-1])# número negativo no indice, retorna a partir do último começando de -1
print(names[-2])
print(names[-3].title())
message = f"My daughter is {names[7]}! I love her!"
print(message)
cores = ["azul,","amarelo","vermelho","verde"]
print(cores)

cores[0] = "rosa"
print(cores)
cores[1] = "laranja"
print(cores)
cores[2] = "preto"
print(cores)
cores[3] = "roxo"
print(cores)
cores.append("tutifruite")
print(cores)

frutas = []
frutas.append("abacate")
frutas.append("uva")
frutas.append("pera")
frutas.append("banana")
frutas.append("abacaxi")
print(frutas)

roupa = ["camisa","calca","gravata","tenis"]
roupa.insert(1,"meia")#usado para inserir na lista, na posição escolhida.
del roupa[3]
print(roupa)

objetos = ["caneta","livro","sofa","cadeira"]
objeto_retirado = objetos.pop()# pop sempre tira o ultimo elemento da lista e usa novamente.
print(objetos)
print(objeto_retirado)#o elemento pode ser usado novamente.
print(f"O objeto retirado usanso metodo pop foi a {objeto_retirado.upper()}")

coisas = ["sapato","roupa","cueca","baton"]
objeto_eliminado = coisas.pop(3)
print(coisas)
print(objeto_eliminado)
print(f"Eu retirei da lista o {objeto_eliminado}, porque eu não uso!")
coisas.insert(0,objeto_eliminado)
print(coisas)

nao_gosto = "baton"
coisas.remove(nao_gosto)
print(coisas)
print(f"O {nao_gosto} e vermelho!")

alfabetic = ["e","b","d","c","a"]#sort poe a lista em ordem alfabetica.
print("This is the original list:")
print(alfabetic)
print("\nThis is the sorted and reverse list:")
print(sorted(alfabetic))#permite alterar a lista e depois voltar para original.
print(sorted(alfabetic, reverse=True))#permite print reverso.
print("\nThis is the original list again:")
print(alfabetic)

print(alfabetic)
alfabetic.sort()#ordem alfabetica.
print(alfabetic)
alfabetic.sort(reverse=True)#permite colocar em ordem alfabetica de tras para frente.
print(alfabetic)

carros = ["onibus","caminhao","fusca","van"]
carros.reverse()#reverter a ordem dos elementos na lista permanentemente.
print(carros)
carros.reverse()#pode reurilizar para voltar a forma original.
print(carros)
print(len(carros))
print(f"A lista tem {len(carros)} elementos!")


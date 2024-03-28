#TUPLAS são listas de elementos que os valores não podem ser mudados, ou seja sã imutáveis
#A lista é construida com parenteses e virgula
dimensions = (200, 50)#tupla
print(dimensions[0])
print(dimensions[1])
my_t = (3,)#tupla construida com apenas 1 elemento
print("\nUsando for com a tupla:")
for dimension in dimensions:
    print(dimension)
#para alterar uma tupla é preciso atribuir uma nova tupla as variaveis
dimensions = (200, 50)
print("\nDimenssões originais:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (400, 100)
print("\nDimenssões alteradas:")
for dimension in dimensions:
    print(dimension) 
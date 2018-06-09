# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.

# Encontrando os dados para a exibição das 20 primeiras amostras
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for i in range(20):
  print(data_list[i])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

# Encontrando os 20 primeiros gêneros
for i in range(20):
  print(data_list[i])
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")

# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem

# Aqui crio colunas para a lista recebida como parametro
# recebo a lista juntamente com o index do elemento
def column_to_list(data, index):

    # PARAMETROS:
    # data: lista de para leitura
    # index: index de um valor na lista

    column_list = []
    for i in data:
      column_list.append(i[index])
    
    # Retorna uma lista preenchida com valores
    # da lista recebida (parametro 1) que antes
    # estava vazia
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.

# Contando quantos gêneros temos, masculino ou feminino, e armazendo
# em uma variável
male = 0
female = 0
for sexo in data_list:
  if sexo[-2] == "Male":
    male +=1
  elif sexo[-2] == "Female":
    female+=1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

# Novamente contandos os gêneros e inserindo estes
# em uma lista, que antes estava vazia
def count_gender(data_list):

    # PARAMETROS:
    # data_list: lista a qual será contada os generos

    count_male = 0
    count_female = 0
    # Criamos um loop para verificar qual
    # o tipo do gênero
    for i in data_list:
      if i[-2] == "Male":
        # Incrementamos um à variável 
        # count_male e, caso tenha sido 
        # Male o valor encontrado
        count_male += 1
      elif i[-2] == "Female":
        # Senão, incrementamos um à variável 
        # count_female caso tenha sido 
        # Female o valor encontrado
        count_female += 1
    
    # Retorna uma lista com os devidos valores
    # dos generos
    return [count_male, count_female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.

# Recebemos uma lista como parâmetro aqui
def most_popular_gender(data_list):
    
    # PARAMETROS:
    # data_list: lista da qual será verificada
    # qual o genero mais popular

    len_male = count_gender(data_list)[0]
    len_female = count_gender(data_list)[1]

    # Para descobrir qual gênero é
    # o mais popular, usamos if statements
    if len_male > len_female:
      answer = "Masculino"
    elif len_male == len_female:
      answer = "Igual"
    elif len_male < len_female:
      answer = "Feminino"
    else:
      # Caso não seja encontrado nenhum valor
      # answer será igual à Erro
      answer = "Erro"
    
    # Retorna o genero mais popular
    # como uma String (ou erro caso não tenha sido encontrado nenhum valor)
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

# Criando um contador de customer e subscriber
# Recebo com parâmetro uma lista
def count_type(data_list):

    # PARAMETROS:
    # data_list: lista para fazer a verificacao
    # dos dados para user_types 

    customer = 0
    subscriber = 0
    
    # Após isso, criando um loop
    # para ler a lista
    for data in data_list:
        # Caso um dos valores encontrados 
        # seja igual a customer, será
        # incrementado um na variável customer
        if (data[-3] == 'Customer'):
            customer += 1
        # senão, será incrementado um
        # na variável subscriber
        elif (data[-3] == 'Subscriber'):
            subscriber += 1
    
    # Retorna uma lista com os devidos
    # valores de customer e subscriber
    return [customer, subscriber]

type_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantity = count_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Type')
plt.xticks(y_pos, types)
plt.title('Quantity by Type')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque a soma dos sexos não é igual ao comprimento de data_list pois deve ser acrescentado um á len(data_list), o índice 1 inicia com 0"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)

# Para encontrar o valor máximo e mínimo
# na lista, primeiro converto todos os valores 
# da lista em ints, para que seja mais fácil trabalhar
# com os dados nela
trip_duration_list = [int(i) for i in trip_duration_list]

# Usando uma função para por 
# em ordem crescente os dados
trip_duration_list = sorted(trip_duration_list)

# Após isso eu seleciono o menor valor da lista
min_trip = trip_duration_list[0]

# E aqui, semelhantemente, seleciono 
# o maior valor da lista
max_trip = trip_duration_list[-1]

# Criando aqui uma variável para
# efetuar a soma dos dados da tabela
soma = 0

# Entrando em um loop com range definido 
# pelo inicio da lista até o fim
for i in range(0, len(trip_duration_list) - 1):
  soma+=trip_duration_list[i]

# Criando outra variável 
# para descobrir o comprimento
# da lista
size = len(trip_duration_list)

# Efetuo a divisão para encontrar a média
resultMean = soma/size

# Entendendo qual foi o valor encontrado
# Se for um número par
# a média é igual ao valor encontrado
if resultMean%2==0:
  mean_trip = resultMean
# caso não seja, converto o resultado 
# para inteiro, e adiciono um
else:
  mean_trip = int(resultMean) + 1

# Para encontrar a mediana
# verifico se o size da lista não tem
# resto, se não tiver, podemos efetuar
# os seguintes cálculos
if size % 2 == 0:
  # Se o comprimento da lista for 
  # um valor par, devemos pegar os
  # dois valores do centro da lista 
  indexOne = (size/2)-1
  indexTwo = (size/2)

  # Converto estes valores para inteiros
  median_trip = int(trip_duration_list[indexOne]) + int(trip_duration_list[indexTwo])
  # Após isso, apenas efetuamos o cálculo da média
  median_trip = int(median_trip /2)
# Caso haja resto diferente de zero,
# quer dizer que o comprimento da 
# lista é impar, o que significa 
# que a média é simplemente o valor
# encontrado no centro da lista
else:
  indexOne = int(size/2)
  median_trip = int(trip_duration_list[indexOne])

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()

# Nesta tarefa, primeiro verificamos 
# quantos tipos de estações iniciais
# nós temos, podemos usar o set para isso
start_stations = set()

# E então entramos em um loop
# para adicionar os valores encontrados
for start_station in column_to_list(data_list, -5):
  start_stations.add(start_station)

print("\nTAREFA 10: Imprimindo as start stations:")
# Depois disso apenas imprimimos o 
# comprimento desta lista
print(len(start_stations))
# E também imprimmos a própria lista
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
# """
# Example function with annotations.
# Args:
#   param1: The first parameter.
#   param2: The second parameter.
# Returns:
#   List of X values
#
# "

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.


# Este desafio vou deixar para a próxima


print("Você vai encarar o desafio? (yes ou no)")
answer = "no"

def count_items(column_list):
    item_types = []
    count_items = []
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
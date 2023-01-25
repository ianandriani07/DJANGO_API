import requests

# GET Avaliacoes

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')


# Acessando o código de status HTTP
#print(avaliacoes.status_code)


#Acessando os dados da resposta
#print(avaliacoes.json())
# print(type(avaliacoes.json()))

# Acessando a quantidade de registros
#print(avaliacoes.json()['count'])

# Acessando a próxima página de resultados
# print(avaliacoes.json()['next'])

# Acessando os resultados dessa página
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))

# Acessando o primeiro elemento da lista de resultados
#print(avaliacoes.json()['results'][-1])

# Acessando somente o nome da última pessoa que fez uma avaliação
#print(avaliacoes.json()['results'][-1]['nome'])


# GET Avaliacao

# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/6/')

# print(avaliacao.json())

#GET Cursos

headers = {'Authorization': 'Token ccac26634238223169fbd424e1ce1703ed8d05f7'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())

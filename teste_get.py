import requests

headers = {'Authorization': 'Token ccac26634238223169fbd424e1ce1703ed8d05f7'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

print(resultado.json())

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
# assert resultado.json()['count'] == 2

# Testando se o título do primeiro curso está correto
# assert resultado.json()['results'][0]['titulo'] == 'Criação de APIs REST com Django REST Framework'

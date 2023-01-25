import requests

headers = {'Authorization': 'Token ccac26634238223169fbd424e1ce1703ed8d05f7'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


novo_curso = {
    "titulo": "Gerência Ágil de Projetos com Scrum",
    "url": "http://www.geekuniversity.com.br/scrum"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)


# Testando o código de status HTTP 201
assert resultado.status_code == 201

# Testando se o título do curso retornado é o mesmo informado
assert resultado.json()['titulo'] == novo_curso['titulo']

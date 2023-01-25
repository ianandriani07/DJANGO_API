import requests

headers = {'Authorization': 'Token ccac26634238223169fbd424e1ce1703ed8d05f7'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'


resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

# Testando o código HTTP
assert resultado.status_code == 204

# Testando se o conteúdo do retornado é 0
assert len(resultado.text) == 0
import requests  # Importa a biblioteca 'requests' para fazer chamadas HTTP à API do IPMA

# Classe responsável por interagir com a API pública do IPMA
class classe_ipma:

    # Método estático que obtém todas as localidades disponíveis no IPMA
    @staticmethod
    def obter_todas_localidades():
        url = 'https://api.ipma.pt/public-data/forecast/locations.json'  # URL da API para obter localidades
        try:
            resposta = requests.get(url)     # Faz a requisição GET
            if resposta.status_code == 200:  # Verifica se a resposta foi bem-sucedida (HTTP 200)
                return resposta.json()       # Retorna os dados em formato JSON
        except:
            pass  # Em caso de erro (ex: sem internet), ignora a exceção
        return None  # Retorna None se não obtiver sucesso

    # Método estático que obtém a previsão agregada para uma localidade específica (com base no seu globalIdLocal)
    @staticmethod
    def obter_previsao_aggregate(global_id_local):
        # URL para obter previsao metreologica de acordo com o id
        url = f'https://api.ipma.pt/public-data/forecast/aggregate/{global_id_local}.json'
        try:
            resposta = requests.get(url)
            if resposta.status_code == 200:
                return resposta.json()
        except:
            pass
        return None

    # Método estático que devolve o globalIdLocal de uma cidade, necessário para obter previsões
    @staticmethod
    def obter_global_id_local(cidade):
        localidades = classe_ipma.obter_todas_localidades()  # Obtém todas as localidades
        if localidades is None:
            return None  # Se não conseguir obter localidades, retorna None
        for loc in localidades:
            # Verifica se o nome da localidade corresponde à cidade procurada (ignorando maiúsculas/minúsculas e espaços)
            if loc['local'] and loc['local'].strip().lower() == cidade.strip().lower():
                return loc['globalIdLocal']  # Retorna o ID correspondente
        return None  # Se não encontrar a cidade, retorna None


# Dicionário que associa IDs de distrito aos seus respetivos nomes (continente, Madeira e Açores)
distritos_por_id = {
    1: "Aveiro", 2: "Beja", 3: "Braga", 4: "Bragança", 5: "Castelo Branco",
    6: "Coimbra", 7: "Évora", 8: "Faro", 9: "Guarda", 10: "Leiria",
    11: "Lisboa", 12: "Portalegre", 13: "Porto", 14: "Santarém",
    15: "Setúbal", 16: "Viana do Castelo", 17: "Vila Real", 18: "Viseu",
    31: "Madeira", 41: "Açores - Vila do Porto", 42: "Açores - Nordeste / Ponta Delgada",
    43: "Açores - Angra do Heroísmo", 44: "Açores - Santa Cruz da Graciosa",
    45: "Açores - Velas (São Jorge)", 46: "Açores - Madalena (Pico)",
    47: "Açores - Horta (Faial)", 48: "Açores - Santa Cruz das Flores",
    49: "Açores - Vila do Corvo"
}


# Função que extrai todos os IDs de distritos únicos de uma lista de localidades
def extrair_distritos(localidades):
    distritos = set()  # Usa um conjunto para garantir unicidade
    for loc in localidades:
        distritos.add(loc['idDistrito'])  # Adiciona o ID do distrito à coleção
    return sorted(distritos)  # Retorna a lista ordenada de IDs


# Função que filtra e retorna apenas as localidades pertencentes a um determinado distrito
def filtrar_localidades_por_distrito(localidades, distrito_id):
    return [loc for loc in localidades if loc['idDistrito'] == distrito_id]  # Lista filtrada

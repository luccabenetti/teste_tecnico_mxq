import requests     # Biblioteca para fazer requisições HTTP
from datetime import datetime       # Biblioteca para manipulação de datas


def buscar_coordenadas(cidade):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    try:
        response = requests.get(url, params={"name": cidade, "count": 1}, timeout=10)   
        # Faz uma requisição GET para a API de geocodificação, passando o nome da cidade e timeout definido para 10 segundos.
        response.raise_for_status()
        data = response.json()

        if "results" not in data or len(data["results"]) == 0:      
            # Verifica se a resposta contém resultados válidos, caso contrário, gera o erro de Cidade não encontrada.
            raise ValueError("Cidade não encontrada")

        resultado = data["results"][0]

        return {
            "nome": f"{resultado['name']}, {resultado.get('admin1', '')}",
            "latitude": resultado["latitude"],
            "longitude": resultado["longitude"]
        }

    except requests.exceptions.RequestException as e:
        print(f"Erro de rede: {e}")
        return None
    except ValueError as e:
        print(f"Erro: {e}")
        return None


def obter_previsao(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": "temperature_2m_max,temperature_2m_min",   
        "timezone": "America/Sao_Paulo",
        "forecast_days": 7  # Define o número de dias para a previsão 
    }

    try:
        response = requests.get(url, params=params, timeout=10)     # Faz uma requisição GET para a API de previsão do tempo, passando os parâmetros acima, além do timeout definido para 10 segundos.
        response.raise_for_status()
        data = response.json()

        if "daily" not in data:
            raise ValueError("Resposta inválida da API")

        return data

    except requests.exceptions.RequestException as e:
        print(f"Erro de rede: {e}")
        return None
    except ValueError as e:
        print(f"Erro: {e}")
        return None


def formatar_previsao(data, cidade):
    daily = data["daily"]

    datas = [datetime.strptime(d, "%Y-%m-%d") for d in daily["time"]]
    temp_max = daily["temperature_2m_max"]
    temp_min = daily["temperature_2m_min"]

    media = sum([(max_ + min_) / 2 for max_, min_ in zip(temp_max, temp_min)]) / len(datas)     # Calcula a temperatura média do período, somando as médias diárias (máxima + mínima) e dividindo pelo número de dias.

    max_periodo = max(temp_max)
    min_periodo = min(temp_min)

    data_max = datas[temp_max.index(max_periodo)]
    data_min = datas[temp_min.index(min_periodo)]

    print("=" * 40)
    print(f" Previsão para: {cidade}")
    print("=" * 40)

    print(f" Período: {datas[0].strftime('%d/%m/%Y')} a {datas[-1].strftime('%d/%m/%Y')}")
    print(f" Temperatura média: {media:.1f}°C")
    print(f" Máxima do período: {max_periodo:.1f}°C ({data_max.strftime('%d/%m')})")
    print(f" Mínima do período: {min_periodo:.1f}°C ({data_min.strftime('%d/%m')})")

    print("-" * 40)

    for d, tmin, tmax in zip(datas, temp_min, temp_max):
        print(f" {d.strftime('%d/%m')}  Min: {tmin:.1f}°C  Max: {tmax:.1f}°C")

    print("=" * 40)


def main():
    cidade_input = input("Digite o nome da cidade: ")

    geo = buscar_coordenadas(cidade_input)

    if not geo:
        print("Não foi possível encontrar a cidade.")
        return

    previsao = obter_previsao(geo["latitude"], geo["longitude"])

    if previsao:
        formatar_previsao(previsao, geo["nome"])
    else:
        print("Erro ao obter previsão.")


if __name__ == "__main__":
    main()
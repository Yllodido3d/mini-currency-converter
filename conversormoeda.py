'''
💡 Projeto: Conversor de Moedas (com API gratuita)
um programinha de terminal que:
pede duas moedas (ex: USD → BRL)
busca a cotação em tempo real
mostra o valor convertido e salva o histórico num arquivo .csv
🧱 O que você vai treinar
uso de API (requests)
tratamento de erros e validações
manipulação de CSV com pandas
funções bem separadas (organização de código)
🚀 Etapas sugeridas
planejar:
entrada: valor, moeda base, moeda destino
saída: valor convertido, cotação atual
criar as funções:
buscar_cotacao(base, destino) → pega da API
converter_valor(valor, cotacao)
salvar_historico()
fazer um loop simples pra repetir até o usuário sair
⚙️ API gratuita sugerida
https://api.exchangerate-api.com/v4/latest/USD
'''

import requests
import pandas
from datetime import datetime
import os


def buscar_cotação(base, destino):
    # a base vai ser o input
    url = f"https://api.exchangerate-api.com/v4/latest/{base.upper()}"
    retorno = requests.get(url)
    dados = retorno.json()
    # se der erro
    if "error" in dados:
        raise ValueError("moeda invalida ou falha na API")
    # converter
    # pega o valor correspondente a moeda
    # vai passar o valor da chave (a moeda)
    taxa = dados["rates"].get(destino.upper())
    if not taxa:  # se dados["rates"] não passar nada pra taxa
        raise ValueError("moeda invalida")
    return taxa

# metodo pra converter o valor


def converter(valor, taxa):
    return round(valor * taxa, 2)
# salvar o historico, de conversão feita (pra ficar bonitinho)


def salvar_historico(base, destino, valor, convertido, taxa):
    df = pandas.DataFrame([{
        "Data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "De": base.upper(),
        "Para": destino.upper(),
        "Valor": valor,
        "Taxa": taxa,
        "Convertido": convertido
    }])
# verificar se o arquivo existe é bom né
    arquvio_existe = os.path.isfile("historico_conversões_fodas.csv")
# aplicar mudanças (e fazer se não existir) modo append, começo se o arquivo não existir
    df.to_csv("historico_conversões_fodas.csv", mode="a",
              header=not arquvio_existe, index=False)

# menuzinho fofo


def main():
    while True:
        base = input("coloque a moeda base (ex: BRL): ").strip()
        destino = input("coloque a moeda de destino (ex: USD): ").strip()
        valor = float(input("coloque o valor a ser convertido: "))

        try:
            taxa = buscar_cotação(base, destino)
            convertido = converter(valor, taxa)
            print(
                f"\n {valor} em {base.upper()} = {convertido} {destino.upper()}\n")
            salvar_historico(base, destino, valor, convertido, taxa)
        except Exception as erro:
            print(f"deu erro chefe, esse: {erro}")

        if input("quer converter mais ? (y/n)") != "y":
            break


# testar o if "main" KKKK
if __name__ == "__main__":
    main()

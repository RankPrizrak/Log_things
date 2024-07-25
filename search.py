import os

def buscar_palavra_chave(pasta, palavra_chave):
    nome_arquivo_resultado = f"resultados_{palavra_chave}.txt"
    resultados = []

    if not os.path.exists(pasta):
        print(f"A pasta '{pasta}' não existe.")
        return resultados

    with open(nome_arquivo_resultado, 'w', encoding='utf-8') as f_resultado:
        for arquivo in os.listdir(pasta):
            if arquivo.endswith('.txt'):
                caminho_arquivo = os.path.join(pasta, arquivo)
                try:
                    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                        for linha in f:
                            if palavra_chave in linha:
                                resultado = linha.strip()
                                resultados.append(resultado)
                                print(resultado)
                                f_resultado.write(resultado + "\n")
                                f_resultado.flush()  # Assegura que o conteúdo é escrito imediatamente
                except UnicodeDecodeError:
                    try:
                        with open(caminho_arquivo, 'r', encoding='iso-8859-1') as f:
                            for linha in f:
                                if palavra_chave in linha:
                                    resultado = linha.strip()
                                    resultados.append(resultado)
                                    print(resultado)
                                    f_resultado.write(resultado + "\n")
                                    f_resultado.flush()  # Assegura que o conteúdo é escrito imediatamente
                    except Exception as e:
                        print(f"Erro ao ler o arquivo '{arquivo}' com ISO-8859-1: {e}")

    return resultados

pasta_logs = 'logs'
palavra_chave = input("""
BY: PRIZRAK.
                      
grupo telegram: t.me/PrizrakApps

Digite a palavra-chave para buscar: """)

resultados = buscar_palavra_chave(pasta_logs, palavra_chave)
if resultados:
    print("""
========================================================
          BY:PRIZRAK t.me/prizrakapps
          17/07/2004
========================================================

Resultados encontrados:
          
""")
else:
    print("Nenhum resultado encontrado.")

    ###BY:RKZ/Prizrak
    ###t.me/prizrakapps


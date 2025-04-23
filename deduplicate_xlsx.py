import pandas as pd
from google.colab import files

def processar_arquivo():
    # Upload do arquivo
    uploaded = files.upload()

    if not uploaded:
        print("Nenhum arquivo foi enviado.")
        return

    nome_arquivo = next(iter(uploaded))

    try:

        df = pd.read_excel(nome_arquivo)


        if len(df.columns) < 4:
            print("O arquivo precisa ter pelo menos 4 colunas.")
            return

        coluna_A = df.columns[0]
        coluna_B = df.columns[1]
        coluna_C = df.columns[2]
        coluna_D = df.columns[3]
        coluna_E = df.columns[3]

        colunas_verificar = [coluna_A, coluna_B, coluna_C, coluna_D]

        print(f"Verificando colunas: {', '.join(colunas_verificar)}")

        df_filtrado = df.dropna(subset=colunas_verificar)

        df_unicos = df_filtrado.drop_duplicates(subset=colunas_verificar)

        nome_novo_arquivo = nome_arquivo.replace('.xlsx', '_processado_recebimento.xlsx')

        df_unicos.to_excel(nome_novo_arquivo, index=False)

        files.download(nome_novo_arquivo)

        print(f"\nProcessamento concluído! Arquivo salvo como {nome_novo_arquivo}")
        print(f"Total de linhas originais: {len(df)}")
        print(f"Linhas após remover vazios: {len(df_filtrado)}")
        print(f"Linhas únicas finais: {len(df_unicos)}")
        print("\nColunas verificadas (por posição):")
        print(f"A: {coluna_A}, B: {coluna_B}, C: {coluna_C}, D: {coluna_D}")

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

processar_arquivo()
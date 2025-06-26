import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações para melhorar a visualização dos gráficos
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12

print("Bibliotecas importadas com sucesso!")

# --- 1. Coleta e Preparação dos Dados ---

try:
    # Carregar dados da aba de Quantidade de Cartões de Crédito
     df_cartoes_credito = pd.read_excel(
       'caminho/para/sua/planilha_bcb_meios_pagamento.xlsx',
         sheet_name='1.1 Quantidade de Cartões de Crédito'
     )
     print("\nAba '1.1 Quantidade de Cartões de Crédito' carregada com sucesso!")
     print("Primeiras 5 linhas:")
     print(df_cartoes_credito.head())
     print("\nInformações sobre o DataFrame:")
     print(df_cartoes_credito.info())

   
    # Crregamento.
    print("\nCarregamento de dados")
    data_tipos = {
        'Período': pd.to_datetime(['2023-01-01', '2023-04-01', '2023-07-01', '2023-10-01', '2024-01-01', '2024-04-01']),
        'Crédito - Total': [200, 205, 210, 215, 220, 225], # em milhões
        'Débito - Total': [150, 152, 155, 158, 160, 163], # em milhões
        'Pré-Pago - Total': [50, 55, 60, 65, 70, 75]     # em milhões
    }
    df_quantidade_cartoes = pd.DataFrame(data_tipos)
    df_quantidade_cartoes.set_index('Período', inplace=True)

    data_transacoes = {
        'Período': pd.to_datetime(['2023-01-01', '2023-04-01', '2023-07-01', '2023-10-01', '2024-01-01', '2024-04-01']),
        'Crédito - Qtde (milhões)': [1000, 1050, 1100, 1150, 1200, 1250],
        'Crédito - Valor (bilhões R$)': [150, 160, 170, 180, 190, 200],
        'Débito - Qtde (milhões)': [800, 820, 840, 860, 880, 900],
        'Débito - Valor (bilhões R$)': [60, 62, 64, 66, 68, 70],
        'Pré-Pago - Qtde (milhões)': [200, 210, 220, 230, 240, 250],
        'Pré-Pago - Valor (bilhões R$)': [10, 11, 12, 13, 14, 15]
    }
    df_transacoes = pd.DataFrame(data_transacoes)
    df_transacoes.set_index('Período', inplace=True)

    data_taxas = {
        'Período': pd.to_datetime(['2023-01-01', '2023-04-01', '2023-07-01', '2023-10-01', '2024-01-01', '2024-04-01']),
        'Taxa Desconto Crédito (%)': [2.5, 2.4, 2.3, 2.2, 2.1, 2.0],
        'Taxa Intercâmbio Crédito (%)': [0.5, 0.5, 0.49, 0.48, 0.47, 0.46],
        'Taxa Desconto Débito (%)': [1.0, 0.98, 0.95, 0.92, 0.90, 0.88],
        'Taxa Intercâmbio Débito (%)': [0.2, 0.19, 0.18, 0.17, 0.16, 0.15]
    }
    df_taxas = pd.DataFrame(data_taxas)
    df_taxas.set_index('Período', inplace=True)

    print("\nDados de exemplo criados para demonstração.")
    print("\nDataFrame 'df_quantidade_cartoes':")
    print(df_quantidade_cartoes.head())
    print("\nDataFrame 'df_transacoes':")
    print(df_transacoes.head())
    print("\nDataFrame 'df_taxas':")
    print(df_taxas.head())


except Exception as e:
    print(f"\nErro ao carregar ou simular dados: {e}")
    print("Por favor, certifique-se de que o caminho do arquivo e o nome da aba estão corretos.")
    print("Ou, se estiver usando a simulação, verifique a criação dos DataFrames.")


# --- 2. Análise Exploratória e Visualização ---

print("\n--- Iniciando Análise Exploratória e Visualização ---")

# Exemplo 1: Evolução da Quantidade de Cartões
plt.figure(figsize=(14, 7))
plt.plot(df_quantidade_cartoes.index, df_quantidade_cartoes['Crédito - Total'], label='Crédito', marker='o')
plt.plot(df_quantidade_cartoes.index, df_quantidade_cartoes['Débito - Total'], label='Débito', marker='o')
plt.plot(df_quantidade_cartoes.index, df_quantidade_cartoes['Pré-Pago - Total'], label='Pré-Pago', marker='o')
plt.title('Evolução da Quantidade de Cartões por Tipo (Milhões)')
plt.xlabel('Período')
plt.ylabel('Quantidade de Cartões (Milhões)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Exemplo 2: Evolução do Valor das Transações
plt.figure(figsize=(14, 7))
plt.plot(df_transacoes.index, df_transacoes['Crédito - Valor (bilhões R$)'], label='Crédito', marker='o')
plt.plot(df_transacoes.index, df_transacoes['Débito - Valor (bilhões R$)'], label='Débito', marker='o')
plt.plot(df_transacoes.index, df_transacoes['Pré-Pago - Valor (bilhões R$)'], label='Pré-Pago', marker='o')
plt.title('Evolução do Valor Total das Transações por Tipo de Cartão (Bilhões R$)')
plt.xlabel('Período')
plt.ylabel('Valor Transacionado (Bilhões R$)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Exemplo 3: Comparação de Quantidade de Transações (último período)
# Pegando o último período disponível para uma visão geral
ultimo_periodo = df_transacoes.index[-1]
transacoes_ult_periodo_qtde = df_transacoes.loc[ultimo_periodo, ['Crédito - Qtde (milhões)', 'Débito - Qtde (milhões)', 'Pré-Pago - Qtde (milhões)']]
transacoes_ult_periodo_qtde.index = ['Crédito', 'Débito', 'Pré-Pago'] # Renomear para o gráfico

plt.figure(figsize=(10, 6))
sns.barplot(x=transacoes_ult_periodo_qtde.index, y=transacoes_ult_periodo_qtde.values, palette='viridis')
plt.title(f'Quantidade de Transações por Tipo de Cartão - {ultimo_periodo.strftime("%Y-%m")}')
plt.xlabel('Tipo de Cartão')
plt.ylabel('Quantidade de Transações (Milhões)')
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# Exemplo 4: Evolução das Taxas de Desconto
plt.figure(figsize=(14, 7))
plt.plot(df_taxas.index, df_taxas['Taxa Desconto Crédito (%)'], label='Desconto Crédito', marker='o')
plt.plot(df_taxas.index, df_taxas['Taxa Desconto Débito (%)'], label='Desconto Débito', marker='o')
plt.title('Evolução das Taxas de Desconto (%)')
plt.xlabel('Período')
plt.ylabel('Taxa de Desconto (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()


# Exemplo 5: Evolução das Taxas de Intercâmbio
plt.figure(figsize=(14, 7))
plt.plot(df_taxas.index, df_taxas['Taxa Intercâmbio Crédito (%)'], label='Intercâmbio Crédito', marker='o')
plt.plot(df_taxas.index, df_taxas['Taxa Intercâmbio Débito (%)'], label='Intercâmbio Débito', marker='o')
plt.title('Evolução das Taxas de Intercâmbio (%)')
plt.xlabel('Período')
plt.ylabel('Taxa de Intercâmbio (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

print("\n--- Análise Exploratória e Visualização Concluídas ---")

# --- 3. Interpretação e Geração de Insights ---
print("\n--- Interpretação e Geração de Insights ---")

print("\nBaseado nos gráficos simulados, podemos observar:")
print("- **Quantidade de Cartões:** Aparentemente, todos os tipos de cartão (crédito, débito, pré-pago) mostram um crescimento constante na quantidade de cartões em circulação.")
print("- **Valor das Transações:** O valor total transacionado com cartões de crédito domina significativamente, mas os cartões de débito e pré-pagos também mostram crescimento, indicando uma diversificação nos hábitos de consumo.")
print("- **Quantidade de Transações:** No último período, a quantidade de transações de crédito é a maior, mas débito também possui um volume considerável, reforçando a relevância de ambos no dia a dia.")
print("- **Taxas de Desconto e Intercâmbio:** As taxas simuladas mostram uma ligeira tendência de queda para as taxas de desconto e intercâmbio, o que poderia indicar maior competitividade no mercado ou regulamentação atuando na redução de custos para os lojistas e emissores, respectivamente.")
print("\nEsses são apenas exemplos de insights baseados nos dados simulados. Com os dados reais do Banco Central, as conclusões seriam muito mais precisas e relevantes.")

print("\n--- Projeto Concluído (com dados simulados) ---")

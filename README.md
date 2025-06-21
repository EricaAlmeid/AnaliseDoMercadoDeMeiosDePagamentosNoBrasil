# Análise do Mercado de Meios de Pagamento no Brasil
Este projeto em Python realiza uma análise exploratória e visualização de dados sobre o mercado de meios de pagamento no Brasil, utilizando informações agregadas disponibilizadas pelo Banco Central do Brasil. O objetivo é compreender as tendências, volumes de transações e dinâmicas de taxas para cartões de crédito, débito e pré-pagos.

🚀 Como Executar o Projeto
Para rodar este projeto em sua máquina, siga os passos abaixo:

📋 Pré-requisitos
Certifique-se de ter o Python 3 instalado. As seguintes bibliotecas Python são necessárias:

pandas: Para manipulação e análise de dados.
numpy: Para operações numéricas (usado por pandas).
matplotlib: Para criação de gráficos estáticos.
seaborn: Para visualizações estatísticas mais atraentes.
Você pode instalá-las usando pip (se ainda não o fez):

Bash

pip install pandas numpy matplotlib seaborn
📥 Obtenção dos Dados
Os dados utilizados neste projeto são públicos e provêm do Banco Central do Brasil.

Baixe a Planilha: Acesse o site do Banco Central do Brasil e procure pela publicação "Instrumentos de Pagamento – Adendos Estatísticos" referente ao 1º Semestre de 2024 (ou o período mais recente disponível). Faça o download do arquivo em formato Excel (.xlsx).
Salve o Arquivo: Salve o arquivo Excel em um local de fácil acesso em seu computador. Recomendamos criar uma pasta data/ na raiz do seu projeto e salvar o arquivo lá. Por exemplo: data/planilha_bcb_meios_pagamento.xlsx.
▶️ Executando o Script
Atualize o Caminho do Arquivo: Abra o arquivo Python do projeto (analise_bcb.py ou o nome que você deu).

Edite a linha:

Python

# df_quantidade_cartoes = pd.read_excel(
#     'caminho/para/sua/planilha_bcb_meios_pagamento.xlsx',
#     sheet_name='1.1 Quantidade de Cartões de Crédito'
# )
Você precisará descomentar essa linha e substituir 'caminho/para/sua/planilha_bcb_meios_pagamento.xlsx' pelo caminho real para o arquivo Excel que você baixou. Além disso, ajuste o sheet_name para as abas que você deseja analisar (ex: '1.1 Quantidade de Cartões de Crédito', '2.1.a Cartões de Crédito - Transações Domésticas - por Arranjo de Pagamento (Quantidade)', etc.).

Importante: O código atualmente utiliza dados simulados para demonstração. Você precisará remover ou comentar a seção de "Simulação de Dados" e habilitar o carregamento real dos dados do Excel para uma análise completa. Pode ser necessário ajustar parâmetros como skiprows ou header no pd.read_excel dependendo da estrutura exata da planilha do BCB.

Execute o Script: Abra seu terminal ou PowerShell, navegue até o diretório onde o arquivo Python está salvo e execute:

Bash

python seu_arquivo_de_projeto.py
(Substitua seu_arquivo_de_projeto.py pelo nome do seu script, por exemplo, analise_bcb.py)

O script irá processar os dados e exibir os gráficos gerados, que serão salvos ou mostrados em janelas separadas, dependendo do seu ambiente.

📊 Estrutura dos Dados (Exemplos de Abas Relevantes)
Este projeto foca em dados de diversas abas da planilha do Banco Central, incluindo (mas não se limitando a):

1. Quantidade de Cartões: Informações sobre o número de cartões de crédito, débito e pré-pago em circulação.
1.1 Quantidade de Cartões de Crédito
1.5 Quantidade de Cartões de Débito
1.7 Quantidade de Cartões de Pré-Pago Ativos por Arranjo de Pagamento
2. Transações com Cartões: Detalhes sobre a quantidade e o valor das transações.
2.1.a Cartões de Crédito - Transações Domésticas - por Arranjo de Pagamento (Quantidade)
2.2.b Cartões de Crédito - Transações Domésticas - por Modalidade (Valor)
2.6.a Cartões de Débito - Transações Domésticas - por Arranjo de Pagamento (Quantidade)
2.8.a Cartões Pré-Pagos - Transações Domésticas - por Arranjo de Pagamento (Quantidade)
3. Taxa de desconto e Tarifa de intercâmbio: Dados sobre as taxas de mercado.
3.1.a Taxa de Desconto Média do Mercado - por Função (%)
3.1.b Tarifa de Intercâmbio Média do Mercado - por Função (%)
📈 Análise Realizada
O script Python realiza as seguintes análises principais:

Evolução Temporal: Gráficos de linha mostrando o crescimento da quantidade de cartões e do valor/quantidade das transações ao longo do tempo para diferentes tipos de cartões.
Comparativos de Volume: Gráficos de barras para comparar o volume de transações entre cartões de crédito, débito e pré-pago em períodos específicos.
Dinâmica das Taxas: Visualização das tendências das taxas de desconto e intercâmbio, essenciais para entender a rentabilidade e competitividade do setor.
Insights: Observações sobre as principais tendências e comportamentos identificados nos dados.
🤝 Contribuições
Sinta-se à vontade para explorar, modificar e expandir este projeto! Sugestões para melhorias, novas análises ou correção de bugs são sempre bem-vindas.

📝 Licença
Este projeto é de código aberto e está disponível sob a licença MIT.

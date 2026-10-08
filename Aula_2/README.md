# Aula 2 - Análise de Cancelamentos de Clientes

Esta aula realiza uma análise exploratória de dados para entender e prever cancelamentos de clientes, utilizando Python com as bibliotecas pandas e plotly.

## Objetivo

Identificar as principais causas de cancelamento de clientes e propor soluções baseadas em dados para reduzir a taxa de churn.

## Estrutura do Projeto

```
Aula_2/
├── main.ipynb          # Notebook principal com toda a análise
├── data/
│   └── cancelamentos.csv  # Base de dados dos clientes
├── images/             # Imagens e visualizações geradas
└── README.md           # Este arquivo
```

## Pré-requisitos

Para executar este projeto, você precisa ter instalado:

- Python 3.x
- Jupyter Notebook

Bibliotecas necessárias:
```bash
pip install pandas numpy openpyxl nbformat ipykernel plotly
```

## Passo a Passo da Análise

### Passo 1: Importação da Base de Dados
- Carrega o arquivo `cancelamentos.csv` usando pandas
- Remove a coluna `CustomerID` que não é necessária para a análise

### Passo 2: Visualização da Base de Dados
- Exibe as primeiras linhas da tabela para entender a estrutura dos dados
- A base contém informações como idade, sexo, tempo como cliente, frequência de uso, ligações ao call center, dias de atraso, tipo de assinatura, duração do contrato, total gasto, meses desde última interação e se cancelou ou não

### Passo 3: Limpeza dos Dados
- Verifica informações sobre tipos de dados e valores nulos
- Remove linhas com valores vazios usando `dropna()`
- A base original tinha 50.000 registros, reduzida para 49.996 após limpeza

### Passo 4: Análise Inicial dos Cancelamentos
- Conta quantos clientes cancelaram vs. não cancelaram
- Calcula a taxa de cancelamento em percentual

### Passo 5: Análise das Causas dos Cancelamentos
- Gera histogramas para cada coluna, diferenciando por status de cancelamento
- Permite visualizar quais características estão mais associadas ao cancelamento

## Insights Identificados

Após análise dos gráficos, foram identificadas três principais causas de cancelamento:

1. **Contrato Mensal**: Clientes com contrato mensal cancelam 100%
   - **Solução**: Oferecer descontos nos planos anuais e trimestrais

2. **Ligações ao Call Center**: Clientes que ligam mais de 4 vezes para o call center cancelam
   - **Solução**: Criar processo para resolver problemas em no máximo 3 ligações

3. **Atrasos no Pagamento**: Clientes que atrasam mais de 20 dias cancelam
   - **Solução**: Implementar política de resolver atrasos em até 10 dias (equipe financeira)

## Filtragem Aplicada

Após identificar as causas, foram aplicados filtros para simular o impacto das soluções propostas:

```python
tabela = tabela[tabela["duracao_contrato"]!="Monthly"]
tabela = tabela[tabela["ligacoes_callcenter"]<=4]
tabela = tabela[tabela["dias_atraso"]<=20]
```

## Como Executar

1. Abra o notebook Jupyter:
```bash
jupyter notebook main.ipynb
```

2. Execute as células sequencialmente para acompanhar a análise

## Colunas da Base de Dados

- `idade`: Idade do cliente
- `sexo`: Gênero do cliente
- `tempo_como_cliente`: Tempo que o cliente está com a empresa
- `frequencia_uso`: Frequência de uso do serviço
- `ligacoes_callcenter`: Número de ligações ao call center
- `dias_atraso`: Dias de atraso no pagamento
- `assinatura`: Tipo de assinatura
- `duracao_contrato`: Duração do contrato (Monthly, Quarterly, Annual)
- `total_gasto`: Total gasto pelo cliente
- `meses_ultima_interacao`: Meses desde a última interação
- `cancelou`: Indicador se o cliente cancelou (0 ou 1)

## Resultados

A análise permite identificar padrões de comportamento que levam ao cancelamento e propor ações estratégicas para reduzir a taxa de churn, focando nos principais fatores identificados.

# Aula 4 - Sistema de Vendas com Streamlit

Sistema interativo de gerenciamento de vendas com dashboard visual, desenvolvido com Python, Streamlit, Pandas e Plotly.

## 📋 Descrição

Este projeto implementa um sistema completo de vendas com as seguintes funcionalidades:

- **Interface Web**: Painel interativo para gerenciamento de vendas
- **Formulário de Cadastro**: Registro de novas vendas com data, vendedor, produto, quantidade e valor
- **Persistência de Dados**: Salvamento automático em arquivo CSV
- **Visualização de Dados**: Tabela com todas as vendas cadastradas
- **Dashboard Analítico**: Gráficos interativos para análise de vendas

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework para criação de aplicações web em Python
- **Pandas**: Manipulação e análise de dados
- **Plotly**: Criação de gráficos interativos

## 📦 Instalação

1. Clone o repositório ou navegue até o diretório da aula:
```bash
cd C:\GIT\pythonIA\Aula_4
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

Ou instale manualmente:
```bash
pip install streamlit pandas plotly
```

## 🚀 Como Executar

Execute o aplicativo com o seguinte comando:

```bash
streamlit run main.py
```

O sistema abrirá automaticamente no navegador (geralmente em `http://localhost:8501`).

## 📊 Funcionalidades

### 1. Cadastro de Vendas
Preencha o formulário na barra lateral com:
- **Data**: Data da venda
- **Vendedor**: Selecione entre Ana, Bruno ou Carla
- **Produto**: Notebook, Celular ou Fone
- **Quantidade**: Número de unidades vendidas
- **Valor**: Valor total da venda

Clique em "Cadastrar venda" para salvar.

### 2. Visualização da Base de Dados
Todas as vendas cadastradas são exibidas em uma tabela interativa.

### 3. Dashboard
- **Faturamento Total**: Métrica com soma de todos os valores
- **Gráfico de Barras**: Vendas por vendedor, coloridas por produto
- **Gráfico de Pizza**: Distribuição de vendas por produto

## 📁 Estrutura do Projeto

```
Aula_4/
├── main.py          # Código principal do sistema
├── requirements.txt # Dependências do projeto
├── vendas.csv       # Base de dados de vendas
└── README.md        # Documentação
```

## 💡 Estrutura do Código

O projeto está organizado em 5 passos principais:

1. **Passo 1**: Criação da tela do sistema
2. **Passo 2**: Criação do formulário de cadastro
3. **Passo 3**: Salvamento da venda na base de dados
4. **Passo 4**: Exibição da base de dados na tela
5. **Passo 5**: Criação do dashboard com gráficos

## 📝 Exemplo de Uso

1. Execute o comando `streamlit run main.py`
2. Na barra lateral, preencha os dados de uma nova venda
3. Clique em "Cadastrar venda"
4. Visualize a venda adicionada na tabela
5. Analise os gráficos atualizados no dashboard

## 🔧 Personalização

Para adicionar novos vendedores ou produtos, edite as listas no arquivo `main.py`:

```python
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla", "Novo Vendedor"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone", "Novo Produto"])
```

## 📚 Conceitos Aprendidos

- Criação de interfaces web com Streamlit
- Manipulação de dados com Pandas
- Criação de gráficos interativos com Plotly
- Persistência de dados em CSV
- Desenvolvimento de dashboards analíticos

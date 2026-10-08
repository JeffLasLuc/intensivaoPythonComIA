# 🤖 Automação de Cadastro de Produtos

Este projeto foi desenvolvido durante a **Aula 1** do Intensivão de Python da Hashtag Treinamentos. O objetivo principal é criar uma automação (RPA - *Robotic Process Automation*) para ler uma base de dados e cadastrar dezenas de produtos em um sistema web de forma rápida, autônoma e livre de erros manuais.

## 🚀 Funcionalidades

- Abertura automática do navegador (Google Chrome).
- Acesso ao link do sistema da empresa.
- Preenchimento automático de formulário de login.
- Leitura e processamento de uma base de dados externa (`produtos.csv`).
- Cadastro iterativo de todos os produtos da tabela, preenchendo campo a campo e enviando os dados.

## 🛠️ Tecnologias Utilizadas

- **[Python](https://www.python.org/)**: Linguagem de programação principal.
- **[PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/)**: Biblioteca para controle automático do mouse e teclado.
- **[Pandas](https://pandas.pydata.org/)**: Biblioteca para leitura e manipulação da base de dados em CSV.

## 📁 Estrutura do Projeto

*   `codigo.py`: Script principal que contém todo o passo a passo da automação (abrir navegador, logar e cadastrar).
*   `pegar_posicao.py`: Script auxiliar que ajuda a descobrir as coordenadas `(X, Y)` do mouse na tela. Muito útil caso você precise adaptar a automação para clicar em locais específicos do seu monitor.
*   `produtos.csv`: Arquivo contendo a massa de dados dos produtos que serão inseridos no sistema.

## ⚙️ Como executar na sua máquina

1. **Pré-requisitos:**
   Certifique-se de ter o Python instalado em seu computador.

2. **Instalação das bibliotecas:**
   Abra o terminal (ou prompt de comando) e instale as dependências executando:
   ```bash
   pip install pyautogui pandas
   ```

3. **Preparação dos arquivos:**
   Verifique se o arquivo `produtos.csv` está no mesmo diretório esperado pelo código. No `codigo.py`, o caminho configurado atualmente é `"Aula_1/produtos.csv"`. Se os arquivos estiverem todos na mesma pasta raiz, altere a linha no código para:
   ```python
   tabela = pd.read_csv("produtos.csv")
   ```

4. **Execução:**
   Rode o script principal no terminal:
   ```bash
   python codigo.py
   ```

## ⚠️ Avisos e Boas Práticas

*   **Resolução e Tela:** O `pyautogui` interage diretamente com o seu sistema operacional. O script utiliza majoritariamente atalhos de teclado (como a tecla `TAB`), o que o torna menos dependente da resolução da tela. No entanto, o sistema deve estar visível e em primeiro plano.
*   **Tempo de Carregamento:** A velocidade de carregamento das páginas web e do navegador pode variar dependendo do computador e da internet. Caso o script comece a digitar antes da tela carregar, aumente os valores do comando `time.sleep()`.
*   **Safety (Emergência):** Se perder o controle durante a automação, uma forma rápida de cancelar o script é arrastar o mouse bruscamente para qualquer um dos quatro cantos da tela (mecanismo de segurança padrão do PyAutoGUI).

---
*Projeto construído durante o Intensivão Python.*
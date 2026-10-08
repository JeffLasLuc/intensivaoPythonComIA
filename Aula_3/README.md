# Aula 3 - ChatBot com IA

Aplicativo de chat interativo utilizando inteligência artificial, desenvolvido com Streamlit e a biblioteca OpenAI SDK conectada à API do Groq.

## 🎯 Objetivo

Criar um chatbot que permite conversar com modelos de linguagem (LLMs) através de uma interface web amigável, mantendo o histórico da conversa.

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework Python para criar aplicações web interativas
- **OpenAI SDK**: Biblioteca para integração com APIs compatíveis com OpenAI
- **Groq API**: Provedor de modelos de IA com alta performance e baixa latência

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Chave de API do Groq (obtenha em: https://console.groq.com/keys)
- Dependências instaladas

## 🚀 Instalação

1. Clone ou baixe este repositório
2. Instale as dependências:

```bash
pip install streamlit openai
```

## ▶️ Como Executar

**Importante**: Não execute com `python main.py`. Use o comando do Streamlit:

```bash
streamlit run main.py
```

O aplicativo será iniciado e estará disponível em `http://localhost:8501`

## 📖 Como Usar

1. Abra o navegador no endereço indicado
2. Insira sua chave de API do Groq na barra lateral (campo password)
3. Digite sua mensagem no campo de chat
4. Aguarde a resposta da IA
5. Continue a conversa - o histórico é mantido automaticamente

## 🔧 Configuração

O modelo atual configurado é:
- **Modelo**: `openai/gpt-oss-120b`
- **API**: Groq (https://api.groq.com/openai/v1)

Para alterar o modelo, edite a variável `NOME_MODELO` no arquivo `main.py`.

Outros modelos disponíveis no Groq:
- `llama-3.3-70b-versatile` (recomendado para chat)
- `mixtral-8x7b-32768`
- `gemma2-9b-it`

## 🧩 Funcionalidades

- ✅ Interface de chat intuitiva
- ✅ Histórico de conversa persistente (session_state)
- ✅ Tratamento de erros de API
- ✅ Indicador de carregamento ("Pensando...")
- ✅ Proteção de chave de API (campo password)
- ✅ Exibição de erro detalhado para debugging

## 📁 Estrutura do Código

- **Autenticação**: Chave de API inserida via sidebar
- **Memória**: `st.session_state["lista_mensagens"]` mantém o histórico
- **Interface**: `st.chat_message` para exibir mensagens do usuário e da IA
- **API**: Integração via OpenAI SDK com endpoint compatível do Groq
- **Tratamento de Erros**: Bloco try/except para capturar erros da API

## ⚠️ Troubleshooting

### Erro 404 - Model not found
Verifique se o nome do modelo está correto e disponível na API do Groq.

### Erro 429 - Quota exceeded
Você excedeu o limite de requisições da sua conta do Groq. Verifique seu plano em https://console.groq.com/

### Erro 401 - Unauthorized
Verifique se sua chave de API está correta e ativa.

### Erro ao executar com `python main.py`
Sempre use `streamlit run main.py` para executar o aplicativo.

## 📝 Aprendizados

- Como usar Streamlit para criar interfaces web
- Integração com APIs de IA usando OpenAI SDK
- Gerenciamento de estado em Streamlit (session_state)
- Tratamento de erros em aplicações de IA
- Estrutura de mensagens em chat (role: user/assistant)

## 🔄 Histórico de Mudanças

- Começou com Google Gemini API (base_url: generativelanguage.googleapis.com)
- Alterado para Groq API devido a limites de quota
- Modelo alterado de classificação para chat (llama-prompt-guard → llama-3.3-70b-versatile)
- Adicionada exibição de erro detalhado para debugging

## 📚 Recursos Adicionais

- [Documentação Streamlit](https://docs.streamlit.io/)
- [Documentação Groq](https://console.groq.com/docs)
- [OpenAI SDK Python](https://github.com/openai/openai-python)

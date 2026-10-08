import streamlit as st
from openai import OpenAI
import openai

NOME_MODELO = "openai/gpt-oss-120b"

chave_usuario = st.sidebar.text_input("Insira sua Chave de API do Groq (https://console.groq.com/keys)", type="password")

if chave_usuario:
    st.sidebar.success(f"Chave lida com sucesso! Inicia com: {chave_usuario[:5]}...")

if not chave_usuario:
    st.info("👈 Por favor, insira sua chave de API na barra lateral para continuar.")
    st.stop() # Para a execução do código aqui
    
modelo = OpenAI(
    api_key=chave_usuario,
    base_url="https://api.groq.com/openai/v1")

st.write("### 🤖 ChatBot com IA") # markdown

# session_state = memoria do streamlit
if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

# adicionar uma mensagem
# st.session_state["lista_mensagens"].append(mensagem)

# exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

mensagem_usuario = st.chat_input("Escreva sua mensagem aqui...")

if mensagem_usuario:
    # user -> ser humano
    # assistant -> inteligencia artificial
    st.chat_message("user").write(mensagem_usuario)
    st.session_state["lista_mensagens"].append({"role": "user", "content": mensagem_usuario})
    
# tratativa pra lidar com erros de conexão/sobrecarga
    try:
        # "Pensando..." enquanto aguarda o servidor (mostra um indicador)
        with st.spinner("Pensando..."):
            resposta_modelo = modelo.chat.completions.create(
                messages=st.session_state["lista_mensagens"],
                model=NOME_MODELO
            )
            
            # Extrai o texto da resposta da estrutura da API
            resposta_ia = resposta_modelo.choices[0].message.content

        # Se tudo certo, mostra a resposta da IA e salva no histórico
        st.chat_message("assistant").write(resposta_ia)
        st.session_state["lista_mensagens"].append({"role": "assistant", "content": resposta_ia})

    except openai.OpenAIError as e:
        # Se o servidor estiver sobrecarregado (Erro 503, 429, etc), 
        # removemos a pergunta do usuário do histórico para ele tentar de novo
        st.session_state["lista_mensagens"].pop()
        
        # Exibe o erro real para diagnóstico
        st.error(f"⚠️ Erro da API: {e}")

    except Exception as e:
        # Captura qualquer outro erro inesperado (ex: sem internet, chave errada)
        st.session_state["lista_mensagens"].pop()
        st.error(f"⚠️ Ocorreu um erro inesperado: {e}")
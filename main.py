# Importando as dependências
import streamlit as st
#Titulo da página
st.title("Inclusão de Usuário")

# Formulário de inserção
with st.form(key="include_cliente"):
    # Campos do formulário
    input_name = st.text_input(label="Insira o nome")
    input_age = st.date_input(label="Insira a data de nascimento")
    input_tipo = st.selectbox(label="Selecione o tipo do cadastro", options=["Fornecedor", "Vendedor", "Cliente", "Gestor", "Administrador"])
    input_button_submit = st.form_submit_button("ENVIAR")

#Configurando a ação de submit
if input_button_submit:
    st.write(f'nome: {input_name}')
    st.write(f'idade: {input_age}')
    st.write(f'tipo: {input_tipo}')

import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import time
import pandas as pd

# Título centralizado
st.markdown("<h1 style='text-align: center;'>COMO FOI SEU DIA, MAY MAY?</h1>", unsafe_allow_html=True)

# # FORMULÁRIO
# st.sidebar.title('MAY')
# Page_cliente = st.sidebar.selectbox(' ', ['INCLUIR', 'CONSULTAR'],)

# if Page_cliente == 'CONSULTAR':
#     st.title('CONSULTAR')
#     costumerList = []

#     for item in ClienteController.SelecionarTodos():
#         costumerList.append([item.data, item.comeu, item.mood, item.fofoca])

#     df = pd.DataFrame(
#         costumerList,
#         columns=['Data', 'Comeu', 'Mood', 'Fofoca']
#     )

#     st.table(df)

# if Page_cliente == 'INCLUIR':
#     st.title('INCLUIR')

with st.form(key='include_cliente', clear_on_submit=True):

    # Dia
    input_dia = st.date_input('Que dia é hoje?', value=None)
    st.markdown("---")
    # Comeu
    input_comeu = st.radio('Fez todas as refeições hoje?', ["SIM", 'NÃO (ta fudida)'])
    st.markdown("---")
    # Mood
    input_mood = st.slider("Como está seu mood hoje? (0 TA UM CU, 10 TA RADIANTE).", 0, 10, 0)
    st.markdown("---")
    # Fofoca
    input_fofoca = st.text_input('Se tem alguma fofoca, digite palavras chaves para eu perguntar depois:')
    st.markdown("---")

    st.write('Envia ai que vejo já já ❤️')
    input_button_submit = st.form_submit_button('Enviar')

if input_button_submit:
    input_comeu = input_comeu.split(' (')[0]  # Remove qualquer parte extra do input "NÃO (ta fudida)"
    ClienteController.Incluir(cliente.Cliente(0, input_data, input_comeu, input_mood, input_fofoca))
    # ESPERA
    with st.spinner('Cadastrando...'):
        time.sleep(2)
        st.success('Feito')
        st.balloons()

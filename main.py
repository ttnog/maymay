import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import time
from datetime import datetime, timedelta

# Título centralizado
st.markdown("<h1 style='text-align: center;'> </h1>", unsafe_allow_html=True)

# Obter a data de hoje
hoje = datetime.now()
# Calcular a data do dia seguinte
amanha = hoje + timedelta(days=1)
# Formatando a data do dia seguinte para um formato específico, por exemplo, DD/MM/YYYY
amanha_formatada = amanha.strftime('%d/%m/%Y')

# FORMULÁRIO PARA PREENCHIMENTO
with st.form(key='include_cliente', clear_on_submit=True):
    # Dia
    input_data = st.date_input('Que dia é hoje?', value=None)
    st.markdown("---")
    # Hora dormir
    input_horario = st.time_input("Qual horario você pretende dormir hoje?", value=None)
    st.markdown("---")
    # Comeu
    input_comeu = st.radio('Fez todas as refeições hoje?', ["SIM", 'NÃO'])
    st.markdown("---")
    #REMEDIO
    input_remedio = st.radio('Tomou todos os remédios?', ["SIM", 'NÃO'])
    st.markdown("---")
    #MOOD
    input_mood = st.slider("Como está seu mood hoje? (0 TA UM CU, 10 TA RADIANTE).", 0, 10, 0)
    st.markdown("---")
    # Fofoca
    st.write("Our secret space, tell me something that you d like me to know or just gossips, whatever u want")
    input_fofoca = st.text_input('nobody can hear us here.')
    st.markdown("---")

    input_button_submit = st.form_submit_button('Enviar')

if input_button_submit:
    input_comeu = input_comeu.split(' (')[0]  # Remove qualquer parte extra do input "NÃO (ta fudida)"
    # Converte input_data e input_horario para strings no formato adequado
    data_str = input_data.strftime('%Y-%m-%d')
    horario_str = input_horario.strftime('%H:%M:%S') if input_horario else None
    ClienteController.Incluir(cliente.Cliente(0, data_str, input_comeu, input_remedio, input_mood, input_fofoca, horario_str))
    # ESPERA
    with st.spinner('Cadastrando...'):
        time.sleep(2)
        st.success(f"Te espero dia {amanha_formatada}, may ❤️")
        st.balloons()
        st.snow()
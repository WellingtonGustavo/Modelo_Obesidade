import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.title("🩺 Risco e Tipo de Obesidade")
st.markdown("Preencha os dados do paciente")

modelo_caminho = '../Models/random_forest_obesity_model.pkl'

@st.cache_data
def carregar_modelo(caminho):
    return joblib.load(caminho)

modelo = carregar_modelo(modelo_caminho)

mapa_binario = {'no': 0, 'yes': 1}
mapa_genero = {'Male': 0, 'Female': 1}
mapa_scc = {'no': 1, 'yes': 0}
mapa_frequencia = {
    'no': 0,
    'Sometimes': 1,
    'Frequently': 2,
    'Always': 4
}

def preprocessamento(input):
    df_pred = pd.DataFrame([input])
    df_pred['IMC'] = df_pred['Weight'] / (df_pred['Height'] * 2)

    df_pred['family_history_Encoding'] = df_pred['family_history'].map(mapa_binario)
    df_pred['FAVC_Encoding'] = df_pred['FAVC'].map(mapa_binario)
    df_pred['SMOKE_Encoding'] = df_pred['SMOKE'].map(mapa_binario)
    df_pred['Gender_Encoding'] = df_pred['Gender'].map(mapa_genero)
    df_pred['SCC_Encoding'] = df_pred['SCC'].map(mapa_scc)
    df_pred['CAEC_Encoding'] = df_pred['CAEC'].map(mapa_frequencia)
    df_pred['CALC_Encoding'] = df_pred['CALC'].map(mapa_frequencia)

    mtrans_colunas = ['MTRANS_Automobile', 'MTRANS_Bike', 'MTRANS_Motorbike',
                  'MTRANS_Public_Transportation', 'MTRANS_Walking']
    
    for col in mtrans_colunas:
        df_pred[col] = 0

    selected_mtrans_col = f"MTRANS_{df_pred['MTRANS'].iloc[0]}"
    if selected_mtrans_col in mtrans_colunas:
        df_pred[selected_mtrans_col] = 1

    colunas_originais = ['Gender', 'family_history', 'FAVC', 'CAEC', 'SMOKE',
                         'SCC', 'CALC', 'MTRANS', 'Height', 'Weight']
    
    df_final = df_pred.drop(columns=colunas_originais, errors='ignore')

    return df_final

with st.sidebar:
    st.header('Entrada de Dados')

    Gender = st.radio('Gênero:', ['Male', 'Female'])
    Age = st.slider('Idade:', min_value=10, max_value=80, value=30)
    Height = st.number_input('Altura (m):', min_value=1.0, max_value=2.5, value=1.70, step=0.01)
    Weight = st.number_input('Peso (kg):', min_value=30.0, max_value=200.0, value=70.0, step=0.1)

    st.markdown('---')
    st.subheader('Hábitos e Histórico')

    family_history = st.radio('Tem Histórico Familiar de Obesidade?', ['yes', 'no'])
    FAVC = st.radio('Consome Alimentos Hipercalóricos?', ['yes', 'no'])
    SMOKE = st.radio('É Fumante?', ['yes', 'no'])
    SCC = st.radio('Monitora Calorias?', ['yes', 'no'])

    FCVC = st.slider('Frequência de Consumo de Vegetais (1=Nunca, 3=Sempre):', 1.0, 3.0, 2.0, 0.5)
    NCP = st.slider('Frequência de Refeições Pricipais (1=Mínimo, 4=Máximo):', 1.0, 4.0, 3.0, 0.5)
    CH20 = st.slider('Frequência de Consumo de Água (1=Mínimo, 3=Máximo):', 1.0, 3.0, 2.0, 0.5)
    FAF = st.slider('Frequência de Atividade Física (0=Nenhuma, 3=Diariamente):', 0.0, 3.0, 1.0, 0.5)
    TUE = st.slider('Tempo de Uso de Aparelhos Eletrônicos (0=Mínimo, 2=Muito):', 0.0, 2.0, 1.0, 0.5)

    CAEC = st.selectbox('Comer entre Refeições:', list(mapa_frequencia.keys()))
    CALC = st.selectbox('Consumo de Álcool:', list(mapa_frequencia.keys()))
    MTRANS = st.selectbox('Principal Meio de Transporte:', ['Automobile', 'Bike', 'Motorbike', 'Public_Transportation', 'Walking'])

    botao_predicao = st.button('Fazer Predição')

    if botao_predicao:
        input_data = {
            'Gender': Gender, 'Age': Age, 'Height': Height, 'Weight': Weight,
            'family_history': family_history, 'FAVC': FAVC, 'FCVC': FCVC, 'NCP': NCP,
            'CAEC': CAEC, 'SMOKE': SMOKE, 'CH20': CH20, 'SCC': SCC, 'FAF': FAF,
            'TUE': TUE, 'CALC': CALC, 'MTRANS': MTRANS
        }

        df_processed = preprocessamento(input_data)

        pred_encoding = modelo.predict(df_processed)[0]

        decodificacao_obesidade = {v: k for k, v in [
            ('Insufficient_Weight', 0), ('Normal_Weight', 1), ('Ovreweight_Level_I', 2),
            ('Overweight_Level_II', 3), ('Obesity_Type_I', 4), ('Obesity_Type_II', 5),
            ('Obesity_Type_III', 6)
        ]}

        resultado_final = decodificacao_obesidade.get(pred_encoding, 'Erro de Classificação')

        st.subheader('Resultado da Predição')

        if pred_encoding >= 4:
            st.error(f'⚠️ Risco Elevado: {resultado_final}')
        elif pred_encoding >= 2:
            st.warning(f'🟡 Risco Moderado: {resultado_final}')
        else:
            st.success(f'✅ Risco Baixo: {resultado_final}')
        
        st.markdown('---')
        st.write(f'Nível de Obesidade Codificado: {pred_encoding}')
        st.caption('Verifique o IMC calculado: {:.2}'.format(df_processed['IMC'].iloc[0]))
    

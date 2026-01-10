# 📈 Projeto de Análise e Previsão de Obesidade (Nome do Projeto)

## 🎯 Desafio de Negócios
## 🧠 Metodologia Técnica e Ferramentas
### 1. Limpeza e Engenharia de Dados (Python/Pandas)
### 2. Modelagem (Machine Learning)
### 3. Visualização e Entrega de Valor (Power BI & Streamlit)
## ✨ Resultados e Insights Principais
## ⚙️ Como Executar o Projeto


## 🎯 Desafio de Negócios

O objetivo principal deste projeto foi **estabilizar e analisar** um *dataset* de saúde contendo informações demográficas e comportamentais (idade, peso, altura, hábitos) para:

1.  **Corrigir a base de dados:** Eliminar inconsistências e erros de formatação nos dados críticos (`Height`, `Weight`) que impediam o cálculo correto do IMC.
2.  **Desenvolver um perfil de risco:** Mapear a distribuição de pacientes nas diferentes categorias de risco de obesidade (`NObeyesdad`).
3.  **Entregar uma ferramenta de diagnóstico e visualização:** Fornecer um *dashboard* interativo (Power BI) e um aplicativo (Streamlit) para consulta rápida e análise de fatores preditivos.

## 🧠 Metodologia Técnica e Ferramentas

O projeto seguiu um pipeline robusto usando Python para tratamento e modelagem, e ferramentas de BI para entrega.

### 1. Limpeza e Engenharia de Dados (Python/Pandas)

O foco primário foi a correção de erros de formato que estavam gerando *outliers* ou valores nulos (`NaN`) críticos.

* **Identificação do Erro:** Foi descoberto que variáveis como `Height` e `Weight` frequentemente omitiam o ponto decimal (ex: `1622397` em vez de `1.62`).
* **Ação Corretiva (String Manipulation):**
    * **Altura (Height):** Usamos a função `.apply()` com uma lógica que insere o ponto decimal após o primeiro dígito em valores longos, corrigindo a conversão de centímetros para metros.
    * **Peso (Weight):** O ponto decimal foi inserido após o terceiro dígito em valores grandes (ex: `11079263` $\rightarrow$ `110.79263`), mantendo a precisão e integridade dos dados.
* **Feature Engineering:** As variáveis categóricas (como Gênero, Histórico Familiar) foram convertidas para formato numérico (Label Encoding/One-Hot Encoding) para que pudessem ser usadas no modelo de Machine Learning.

### 2. Modelagem (Machine Learning)

* **Algoritmo:** Random Forest Classifier.
* **Objetivo do Modelo:** Classificar a categoria de obesidade de um paciente com base em suas características (idade, altura, peso, hábitos).
* **Performance:** Acurácia de 98%.
### 3. Visualização e Entrega de Valor (Power BI & Streamlit)

* **Power BI Dashboard:** Permite a análise interativa dos dados limpos, visualizando a distribuição do IMC, a prevalência por categoria de risco e filtros demográficos, [Dashboard](https://app.powerbi.com/groups/me/reports/ca3af396-35d0-4a54-91e5-5882124274fe/b27fc188e2c929042509?experience=power-bi).
* **Streamlit App:** Um aplicativo web que permite à equipe médica inserir dados de um novo paciente e obter uma **previsão instantânea** de sua categoria de obesidade, [Aplicação](https://modeloobesidade-cg44qccw4pb3opmqk9hzgd.streamlit.app/).

## ✨ Resultados e Insights Principais

* **Base de Dados Confiável:** A limpeza resultou em uma base de dados coerente, com o **IMC recalculado corretamente** e valores de `Height` e `Weight` padronizados, tornando a base segura para qualquer pesquisa futura.
* **[Insight 1]:** Histórico Familiar é um fator para casos de Obesidade e Sobrepeso
* **[Insight 2]:** O publico após os 40 anos tem menos casos de Obesidade.




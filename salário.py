import streamlit as st

def calcular_salario (salário,horas):
    salario  = (salário * horas )
    return salario

def classificar_salario(media):
    if media >=  3484:
        classificacao ="VOCÊ GANHA BEM"
    elif media >= 2500:
        classificacao ="mais ou menos"
    else:
        classificacao = "mal não é justo"
    return classificacao

st.title("calcular o salario")

st.header("digite seu salário:")
salario = st.number_input("salario:", min_value=0.0, max_value=5000.00)
horas = st.number_input("horas:", min_value=4, max_value= 8)

st.divider ()

if st.button ("calcular salario"):
    media = calcular_salario (salario,horas)
    situacao = classificar_salario (media)

    st.subheader(" 🧐Resultado")
    st.write(f"**salario:** {media:.2f}")
    st.success(f"**Situação:** {situacao}")
else:
    st.info("☝🏾☝🏾Clique no botão acima para calcular a salario ☝🏾☝🏾")




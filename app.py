import streamlit as st

# Função para calcular a média
def calcular_media(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    return media

# Função para classificar a média
def classificar_media(media):
    if media >= 7:
        classificacao = "Aprovado(a) ✅"
    elif media >= 5:
        classificacao = "Recuperação ⚠️"
    else:
        classificacao = "Reprovado(a) ❌"
    return classificacao

# Título principal
st.title("🙃Calculadora de Média Escolar")

# Entradas das notas
st.header("Digite as notas do aluno:")
nota1 = st.number_input("Primeira nota😨:", min_value=0.0, max_value=10.0, step=0.5)
nota2 = st.number_input("Segunda nota😩:", min_value=0.0, max_value=10.0, step=0.5)
nota3 = st.number_input("Terceira nota🤯:", min_value=0.0, max_value=10.0, step=0.5)
nota4 = st.number_input("Quarta nota😱:", min_value=0.0, max_value=10.0, step=0.5)

st.divider()

# Botão para calcular
if st.button("Calcular Média"):
    media = calcular_media(nota1, nota2, nota3, nota4)
    situacao = classificar_media(media)

    st.subheader(" 🧐Resultado")
    st.write(f"**Média:** {media:.2f}")
    st.success(f"**Situação:** {situacao}")
else:
    st.info("☝🏾☝🏾Clique no botão acima para calcular a média☝🏾☝🏾")

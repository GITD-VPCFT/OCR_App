# Bibliotecas a serem utilizadas
import pytesseract
import cv2
import streamlit as st

# Identificação do local onde realmente se encontra o tesseract (o pip instala em lugar errado)
pytesseract.pytesseract.tesseract_cmd = "D:\\Users\\50109192\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"


# FUNÇÃO PARA OCR COMPLETO DE PÁGINA DO PDF
def extracao_texto(nome_arquivo):
    # Leitura da imagem
    img = cv2.imread(nome_arquivo)
    
    # OCR da imagem lida
    return pytesseract.image_to_string(img, lang='por')

# CRIANDO INTERFACE

# Título da página

st.header("📃Extrator de Textos (OCR)")
st.subheader("Carregue abaixo arquivos em formato .png para exrair textos. ")
st.write("Obs.: O reconhecimento dos textos não é 100%. Confira e valide antes de qualquer uso.")

# Campo para upload de arquivo
img_user = st.file_uploader(label="Selecione seu arquivo:",accept_multiple_files=False, type=['png'])

# Se imagem selecionada...
if img_user:

    # Conferência da imagem  
    #with st.expander("Confira se a imagem selecionada está correta:"):
    #    st.image(img_user)

    # Botão de envio
    check_envio = st.button(label="Enviar")

    # Se botão de envio selecionado...
    if check_envio:

        # Invocando a função de extração criada
        resultado_ocr = extracao_texto(img_user.name)

        # Gerando o texto extraído
        st.text(resultado_ocr)

# Assinatura GITD
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.write('')
st.divider()
st.markdown("_Aplicativo desenvolvido e mantido pela Gerência de Inovação e Transformação Digital - VPFCT_")
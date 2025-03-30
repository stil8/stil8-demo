import streamlit as st
import openai

st.set_page_config(page_title="Stil8 AI", page_icon="👗")
st.title("👗 Stil8 – La tua stylist AI personale")

st.markdown("""
Fai una domanda di moda a Stil8, l'assistente AI ispirata a Sara Salerno.  
Consigli personalizzati su stile, abbinamenti, tessuti e Made in Italy.
""")

openai.api_key = st.secrets["OPENAI_API_KEY"]

stil8_prompt = """
Agisci come se fossi un'assistente virtuale di moda chiamata Stil8, ispirata a Sara Salerno.
Parla in italiano, con tono elegante, empatico e competente.
Dai consigli su abbinamenti, tessuti di qualità, body shape e valorizzazione dello stile personale. 
Concentrati su moda Made in Italy, dettagli sartoriali e buon gusto.
"""

user_input = st.text_input("Scrivi qui la tua domanda di moda:")

if user_input:
    with st.spinner("Stil8 sta pensando al look perfetto..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": stil8_prompt},
                {"role": "user", "content": user_input},
            ],
            temperature=0.7,
            max_tokens=400
        )
        output = response.choices[0].message.content.strip()
        st.success("Stil8 consiglia:")
        st.markdown(output)

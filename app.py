import streamlit as st
from electoral_calculator import process_divipola

st.set_page_config(page_title="Proyección de Testigos", page_icon="📊", layout="centered")

st.title("📥 Proyección de Testigos Electorales")
st.write("Carga un archivo DIVIPOLA en formato Excel y selecciona el número de candidatos para ver los resultados.")

uploaded_file = st.file_uploader("📎 Cargar archivo DIVIPOLA (.xlsx)", type=["xlsx"])
candidatos = st.number_input("👤 Número de candidatos", min_value=1, step=1)

if uploaded_file and candidatos:
    try:
        resultados = process_divipola(uploaded_file, candidatos)

        st.success(f"📍 {resultados['sitio']} | {resultados['candidatos']} candidatos | {resultados['puestos']} puestos | {resultados['total_mesas']} mesas")
        st.markdown("---")
        st.markdown(f"""
        - **Remanentes**: {resultados['total_remanentes']}  
        - **Mesa principal**: {resultados['total_mesas']}  
        - **Total mesa/candidato**: {resultados['total_mesa_pc']}  

        - **Comisión municipal**: {resultados['municipal']}  
        - **Comisión general**: {resultados['general']}  
        - **Auxiliares**: {resultados['auxiliar']}  
        - **Total comisión/candidato**: {resultados['total_comm_pc']}  

        - **Total por candidato**: {resultados['total_x_candidato']}  
        - ✅ **Total general**:  
            - Mesas: {resultados['total_mesa_all']}  
            - Comisiones: {resultados['total_comm_all']}  
            - **Total final**: {resultados['total_all']}
        """)
    except Exception as e:
        st.error(f"❌ Error al procesar el archivo: {e}")

import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="NASA Reconexión Magnética",
    page_icon="🌌",
    layout="centered"
)

# Función para la página de bienvenida
def pagina_bienvenida():
    # Crea 3 columnas
    left_col, mid_col, right_col = st.columns(3)

    # Muestra la imagen en la columna central
    mid_col.image("Nasa.jpg", width=200)
    st.title("Bienvenido a la página de la NASA sobre la Reconexión Magnética de la Tierra")
    st.write("La reconexión magnética es un proceso importante en la interacción entre el viento solar y el campo magnético de la Tierra.")
    st.header("Cómo afecta al clima de la Tierra")
    st.write("La reconexión magnética puede tener un impacto en el clima de la Tierra al influir en las tormentas geomagnéticas y las auroras.")
    # Botón
    if st.button("¡Celebremos con globos!"):
        st.balloons()

# Función para la página de información (Opción 2)
def pagina_informacion():
    st.title("Información sobre Reconexión Magnética")
    # Agrega más contenido informativo aquí si lo deseas

# Función para la página de contacto (Opción 3)
def pagina_contacto():
    st.title("Contáctenos")
    # Agrega información de contacto si lo deseas

# Menú de opciones
opciones = ["Bienvenida", "Información", "Contacto"]
eleccion = st.sidebar.selectbox("Selecciona una opción:", opciones)

# Contenido de la página según la elección
if eleccion == "Bienvenida":
    pagina_bienvenida()
elif eleccion == "Información":
    pagina_informacion()
elif eleccion == "Contacto":
    pagina_contacto()


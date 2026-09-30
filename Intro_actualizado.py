import streamlit as st

st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Aplicaciones de Inteligencia Artificial")
st.markdown(
    "Explora diferentes aplicaciones de Inteligencia Artificial, "
    "análisis de datos y aprendizaje automático."
)

with st.sidebar:
    st.header("📚 Aplicaciones con Inteligencia Artificial")
    st.write(
        "La inteligencia artificial permite analizar datos, automatizar tareas, "
        "crear modelos predictivos y visualizar resultados de forma interactiva."
    )
    st.info("Pulsa el botón de cada tarjeta para abrir la aplicación.")

apps = [
    {
        "title": "Clasificación de Datos",
        "description": "Aplicación para explorar conceptos de clasificación y aprendizaje automático.",
        "url": "https://class1-jq9yonrbapfszdvqbtlujk.streamlit.app",
        "image": "https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?auto=format&fit=crop&w=800&q=80",
    },
    {
        "title": "Análisis de Datos",
        "description": "Herramienta interactiva para trabajar con datos y observar sus resultados.",
        "url": "https://jpqj6s2wucnaissu6fwcwr.streamlit.app",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
    },
    {
        "title": "Series de Tiempo",
        "description": "Aplicación para analizar y realizar predicciones sobre datos organizados en el tiempo.",
        "url": "https://appseriestiempopy-hfs3xryhldu9l7meyvgpki.streamlit.app",
        "image": "https://images.unsplash.com/photo-1535320903710-d993d3d77d29?auto=format&fit=crop&w=800&q=80",
    },
    {
        "title": "Modelos Predictivos",
        "description": "Aplicación interactiva para experimentar con modelos de aprendizaje automático.",
        "url": "https://6rgfqstaz3dbrhxcwoisqn.streamlit.app",
        "image": "https://images.unsplash.com/photo-1518186285589-2f7649de83e0?auto=format&fit=crop&w=800&q=80",
    },
    {
        "title": "Nivel Cornare",
        "description": "Aplicación interactiva para trabajar con datos y predicciones relacionadas con niveles.",
        "url": "https://appnivelcornarepy-7jpsbpj89y9dntum78f92z.streamlit.app",
        "image": "https://images.unsplash.com/photo-1538300342682-cf57afb97285?auto=format&fit=crop&w=800&q=80",
    },
    {
        "title": "Clasificación KNN",
        "description": "Herramienta para comprender cómo funciona el algoritmo de vecinos más cercanos.",
        "url": "https://ea7evtp7hvlrokwmqw5n8v.streamlit.app",
        "image": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
    },
    {
        "title": "Aprendizaje Automático",
        "description": "Aplicación educativa para experimentar con conceptos de aprendizaje automático.",
        "url": "https://q5jmjqscd4ihxkibctmipe.streamlit.app",
        "image": "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?auto=format&fit=crop&w=800&q=80",
    },
    {
        "title": "Regresión y Predicción",
        "description": "Aplicación para explorar relaciones entre variables y realizar predicciones.",
        "url": "https://tenxjxuarbcr4336zd22kw.streamlit.app",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
    },
    {
        "title": "Conceptos de Regresión",
        "description": "Aplicación educativa para comprender los fundamentos de la regresión.",
        "url": "https://regresionconceptosapppy-y33b8r2kesirbfoqrshzjh.streamlit.app",
        "image": "https://images.unsplash.com/photo-1509228468518-180dd4864904?auto=format&fit=crop&w=800&q=80",
    },
    {
        "title": "Regresión Logística",
        "description": "Aplicación para explorar la regresión logística y la clasificación de datos.",
        "url": "https://appregresionlogisticapy-4vzpwvj3me6pt8mfpsimyf.streamlit.app",
        "image": "https://images.unsplash.com/photo-1553877522-43269d4ea984?auto=format&fit=crop&w=800&q=80",
    },
]

for i in range(0, len(apps), 3):
    cols = st.columns(3)

    for j, col in enumerate(cols):
        idx = i + j
        if idx >= len(apps):
            break

        app = apps[idx]

        with col:
            st.subheader(app["title"])
            st.image(app["image"], use_container_width=True)
            st.write(app["description"])
            st.link_button(
                "🚀 Abrir aplicación",
                app["url"],
                use_container_width=True
            )
            st.divider()

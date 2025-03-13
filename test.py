import streamlit as st
from pathlib import Path

# Pfad zur PDF-Datei
file_path = 'BF.png'

st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)


def get_file_content_as_bytes(file_path):
    with open(file_path, "rb") as file:
        return file.read()

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)


# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)


left, right = st.columns([3,3], gap="medium")
with left:
    st.image("BF.png", caption=None, width=300,)


with right:
  st.markdown("""
  <h3>Marcel Aria</h3>
    <em>Ich bin ein technikbegeisterter Programmierer, der die digitale Transformation aktiv mitgestalten und in der IT-Welt Außergewöhnliches leisten möchte.</em>
    """, unsafe_allow_html=True)
  st.write("📩", "marcel.aria.2009@gmail.com")

st.header("IT-Kompetenzen", anchor=False, divider="blue")
st.markdown(r'''
-  **Webentwicklung:** Fundierte Grundkenntnisse in HTML, CSS und Streamlit
-  **Programmierung:** Praktische Erfahrung in Python,CSS und HTML Entwicklung kleiner Anwendungen und Skripte
-  **Office-Suite:** Versierter Umgang mit Microsoft Word, Excel und PowerPoint
-  **Eigene Projekte:** Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
''')

st.header("Schulbildung", anchor=False, divider="blue")
st.subheader("Fachmittelschule Schaumburgergasse 4, Wien")
st.markdown(r'''
  **Schwerpunkt:** Intensive IT-Spezialisierung, Fokus auf modernen Webtechnologien und Wirtschaft
 **Zeitraum:** September 2024 - Juli 2025
  **Derzeitiger Notenschnitt:** 1,2
''')

st.subheader("Sportmittelschule Pastorstr 29, Wien")
st.markdown(r'''
 **Zeitraum:** September 2020 – Juli 2024
 **Abschluss-Notendurchschnitt:** 2,9
''')

st.header("Arbeitserfahrung", anchor=False, divider="blue")
st.markdown(r'''
 Berufspraktische Tage 3:**Bei Siemens von 18. bis 22. Nov. 2024**
            
Berufspraktische Tage 2:**Bei einer Pizzeria und Eissalon von 18. bis 22. Nov 2023**
            
 Berufspraktische Tage 2:**Im Kindergarten vom 18. bis 22. Nov 2022**
''')

st.header("Zusätzliche Qualifikationen", anchor=False, divider="blue")
st.markdown(r'''
  -**Schnelle Auffassungsgabe** für neue Softwareanwendungen und Technologien
            
  -**Großes Interesse** an der kontinuierlichen Weiterentwicklung im IT-Bereich
            
  -**Starke Problemlösungsfähigkeiten** bei der Entwicklung individueller Webprojekte
            
  -**Eigenständige Konzeption**, Gestaltung und Umsetzung mehrerer Webseiten

            -**Teamfähigkeit und Kommunikationsstärke** bei gemeinsamen Coding-Projekten   
               ''')

st.header("Interessen und Hobbys", anchor=False, divider="blue")
st.write("💻**Programmierung**")
st.write("🥊**Kraftsport**")
st.write("🥋**Kampfsport**")


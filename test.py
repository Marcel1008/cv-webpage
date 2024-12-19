import streamlit as st
from pathlib import Path


st.markdown("<style> .stAppHeader {display:none;} ul {list-style-type: none; } </style>", unsafe_allow_html=True)



def get_file_content_as_bytes(file_path):''
    with open(file_path, "rb") as file:
        return file.read()

# Pfad zur PDF-Datei
file_path = 'test.jpg'

# Lese den Inhalt der PDF-Datei als Bytes
file_bytes = get_file_content_as_bytes(file_path)


left, right = st.columns([3,3], gap="medium")
with left:
    st.image("profile-pic.png", caption=None, width=200,)


with right:
  st.markdown("""
  <h3>Marcel Aria</h3>
    <em>Ich bin eine technikbegeisterter Programmierer, der die digitale Transformation aktiv mitgestalten und in der IT-Welt Außergewöhnliches leisten möchte.</em>
    """, unsafe_allow_html=True)

with right:
    st.title("test.pdf", anchor=None)
    st.markdown(f"<em> <p>'Ich bin IT-Enthusiastin und Programmiererin, <br> die in dem Bereich eine echte Expertin werden möchte und gespannt auf die Zukunft ist.'</p> </em>", unsafe_allow_html=True)
    # Der Download-Button, der die Datei zur Verfügung stellt
    st.download_button(
        label="📄 Download CV",
        data=file_bytes,
        file_name=file_path,
        mime='application/pdf'
    )
    st.write("📩", "lisa.bauer@gmx.at")




   



st.write("\n")

st.header("IT-Kompetenzen", anchor=False, divider="blue")
st.markdown(r'''
-  **Webentwicklung:** Fundierte Grundkenntnisse in HTML, CSS und Streamlit (Fullstack-Framework)
-  **Programmierung:** Praktische Erfahrung in Python,CSS und HTML Entwicklung kleiner Anwendungen und Skripte
-  **Office-Suite:** Versierter Umgang mit Microsoft Word, Excel und PowerPoint
-  **Eigene Projekte:** Konzeption und Umsetzung verschiedener Projekte inklusive Hosting
''')

st.header("Schulbildung", anchor=False, divider="blue")
st.subheader("Fachmittelschule Schaumburgergasse, Wien")
st.markdown(r'''
  **Schwerpunkt:** Intensive IT-Spezialisierung, Fokus auf modernen Webtechnologien und Wirtschaft
 **Zeitraum:** September 2024 - Juli 2025
  **Derzeitiger Notenschnitt:** 1,2
''')

st.subheader("Sportmittelschule Pastorstr, Wien")
st.markdown(r'''
 **Zeitraum:** September 2020 – Juli 2024
 **Abschluss-Notendurchschnitt:** 2,9
''')

st.header("Arbeitserfahrung", anchor=False, divider="blue")
st.markdown(r'''
 Berufspraktische Tage 3:** Bei Siemens von 18. bis 22. Nov. 2024
            
Berufspraktische Tage 2:** Bei einer Pizzeria und Eissalon von 18. bis 22. Nov 2023
            
 Berufspraktische Tage 2:** Im Kindergarten vom 18. bis 22. Nov 2022
''')

st.header("Zusätzliche Qualifikationen", anchor=False, divider="blue")
st.markdown(r'''
  -**Schnelle Auffassungsgabe** für neue Softwareanwendungen und Technologien
  -**Großes Interesse** an der kontinuierlichen Weiterentwicklung im IT-Bereich
  -  **Teamfähigkeit und Kommunikationsstärke** bei gemeinsamen Coding-Projekten
  -**Starke Problemlösungsfähigkeiten und kreative Ansätze bei der Realisierung individueller Webprojekte
  -**Eigenständige Konzeption, Gestaltung und Umsetzung mehrerer Webseiten
               ''')

st.header("Interessen und Hobbys", anchor=False, divider="blue")
st.write("🥊**Kraftsport**")
st.write("🥋**Kampsport**")
st.write("💻**Programmierung**")

st.write("#")
st.write("#")
st.write("#")

import streamlit as st
import streamlit_authenticator as stauth
import time
import os
import dotenv
def main():
    st.session_state['authenticated'] = st.session_state.get('authenticated', False)
    save_path = './files/nasini'  # Cambia esto por la ruta donde quieres guardar los archivos
    st.image('./logo_nasini.png', width=50)  # Ajusta la ruta y el tamaño según tus necesidades
    # Asegúrate de que la ruta de guardado exista
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Muestra la página de login si el usuario no está autenticado
    if not st.session_state['authenticated']:
        login_page()
    else:
        home_page(save_path)

def login_page():
    st.title("Login")

    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.session_state['authenticated'] = True
            st.experimental_rerun()
        else:
            st.error("Error de autenticación")

def home_page(save_path):
    st.title("Nasini Files")
    file_uploader(save_path)

    if st.button("Cerrar sesión"):
        st.session_state['authenticated'] = False
        st.experimental_rerun()

def authenticate(username, password):
    # Implementa aquí tu lógica de autenticación real
    user_=os.getenv('USERNAME')
    pass_=os.getenv('PASSWORD')
    return username == user_ and password == pass_

def file_uploader(save_path):
        uploaded_files = st.file_uploader("Sube un archivo", accept_multiple_files=True, type=['pdf', 'txt'], key="file_uploader")
        if st.button("Subir archivos.."):
            if uploaded_files is not None:
                with st.spinner('Subiendo archivos...'):
                    progress_bar = st.progress(0)
                    total_files = len(uploaded_files)
                    for i, uploaded_file in enumerate(uploaded_files, start=1):
                        file_path = os.path.join(save_path, uploaded_file.name)
                        with open(file_path, "wb") as f:
                            f.write(uploaded_file.getvalue())  # Guarda el archivo en la ruta especificada
                        # Aquí puedes agregar el código para procesar cada archivo
                        # Simulamos un tiempo de procesamiento
                        time.sleep(0.5)  # Simular tiempo de procesamiento
                        progress_bar.progress(int(i / total_files * 100))

                    st.success("¡Archivos subidos con éxito!")

if __name__ == "__main__":
    main()
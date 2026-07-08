import streamlit as st

def style_background_home():
    st.markdown("""

        <style>
                .stApp {
                    background: #5865f2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color: #E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius:5rem !important;
                }
        </style>
    """
    , unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""

        <style>
                .stApp {
                    background: #E0E3FF !important;
                }
        </style>
    """
    , unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""

        <style>
                
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            #MainMenu, header , footer {
                visibility: hidden;
            }
                
            .block-container{
                padding-top:1.5rem !important;
            }
                
            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size:3.5rem !important;
                line-height: 1.05 !important;
                margin-bottom: 0rem !important;
            }
                
            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size:2rem !important;
                line-height: 1.05 !important;
                margin-bottom: 0rem !important;
            }
                
            h3,h4,p {
                font-family: 'Outfit', sans-serif !important;
            }

            button{
                border-radius: 1.5rem !important;
                background-color: #5865f2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                teansition: transform 0.25s ease-in-out !important;
            }
                
            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #eb459e !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                teansition: transform 0.25s ease-in-out !important;
            } 
                
            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                teansition: transform 0.25s ease-in-out !important;
            } 
                
            button:hover{
                transform: scale(1.05)
            }
                
            /* Force light-mode styles on all text inputs */
            .stTextInput > div > div > input {
                background-color: #ffffff !important;
                color: #31333F !important;
                border: 1px solid #cccccc !important;
                border-radius: 0.375rem !important;
            }

            /* Input focus state */
            .stTextInput > div > div > input:focus {
                border-color: #4A90E2 !important;
                box-shadow: 0 0 0 2px rgba(74, 144, 226, 0.2) !important;
            }

            /* Input label */
            .stTextInput label {
                color: #31333F !important;
            }

            /* Input placeholder */
            .stTextInput > div > div > input::placeholder {
                color: #aaaaaa !important;
            }

            /* Input container background */
            .stTextInput > div {
                background-color: #ffffff !important;
            }
                
        </style>
    """
    , unsafe_allow_html=True)
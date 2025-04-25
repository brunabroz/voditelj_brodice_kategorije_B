import os
import random
from PIL import Image
import streamlit as st

# Path to the image folder — must be relative to your .py file or repo
folder_path = ".\Brodska_Svjetla"  # Put the folder with all 39 images in the same folder as this script
total_images = 39

# --- Descriptions ---
def get_description(image_number):
    descriptions = {
        1: "Motorni brod dulji od 50m",
        2: "Motorni brod kraci od 50m",
        3: "Motorni brod kraci od 12m (15m)",
        4: "Motorni brod kraci od 7m, max brzina 7 cvorova",
        5: "Brod na vesla ili Jedrilica koja plovi (do 20m), manja od 7m moze imati samo kruzno bijelo",
        6: "Jedrilica koja plovi dulja od 20m",
        7: "Jedrilica koja istodobno koristi i motor danju",
        8: "Brod na vesla ili Jedrilica koja plovi (do 20m), manja od 7m moze imati samo kruzno bijelo",
        9: "Motorni brod kraci od 50m ,tegalj kraci od 200m",
        10: "Motorni brod kraci od 50m ,tegalj dulji od 200m",
        11: "Motorni brod dulji od 50m ,tegalj kraci od 200m",
        12: "Motorni brod dulji od 50m ,tegalj dulji od 200m",
        13: "Motorni brod kraci od 50m, tegli bocno",
        14: "tegljeni brod/objekt ili brod na vesla ili jedrenjak",
        15: "Motorni brod kraci/dulji od 50m, tegalj dulji od 200m",
        16: "Slabo uocljiv ili uronjen brod/objekt koji se tegli",
        17: "Brod dulji od 50m koji kocari i usidern je (nema bocnih svjetala)",
        18: "Brod dulji od 50m koji kocari i nije usidren",
        19: "Ribarica koja se ne krece <50m",
        20: "Ribarica koja se krece <50m",
        21: "Brod koji ribari ili kocari danju",
        22: "Brod nesposoban za manevar koji se ne krece",
        23: "Brod nesposoban za manevar koji se krece, <50m",
        24: "Brod ogranicen manevrom danju",
        25: "Brod ogranicen manevrom koji se ne krece, <50m",
        26: "Brod ogranicen manevrom koji se krece, >50m",
        27: "Brod ogranicenog manevra danju",
        28: "Motorni brod <50m koji tegli, ogranicenog mavera, tegalj kraci od 200m",
        29: "Brod zauzet podvodnim radovima, ogranicenog manevra koji se krece, zapreka na njegovoj desnoj strani",
        30: "Motorni brod koji razminirava, krece se i <50m.",
        31: "Razminirava i sa strane se vide kao dvije kugle, ali zapravo su odnaprijed 3 u kriz.",
        32: "Motorni brod ogranicen gazom, dulji od 50m koji se krece.",
        33: "Motorni brod ogranicen gazom danju.",
        34: "Peljar koji se krece, manji od 50m. Danju H-zastavica.",
        35: "Motorni brod usidren, dulji od 50m.",
        36: "Usidreni brod manji od 50m.",
        37: "Usidreni brod danju. (kraci od 7m ne moraju ovo pokazivati)",
        38: "Nasukani brod (usidren i nesposoban manevrom). (ako je kraci od 12m, ne mora)",
        39: "Nasukani brod danju (1 kugla = usidren & 2 kugle = nesposoban za manevar)"
    }
    return descriptions.get(image_number, "No description available.")

# --- Streamlit App Setup ---
st.set_page_config(page_title="Brodska Svjetla", layout="centered", page_icon="🚢")
st.title("🚢 Brodska Svjetla — Edukacija")

# Initialize session state
if "shown_images" not in st.session_state:
    st.session_state.shown_images = []
if "current_image" not in st.session_state:
    st.session_state.current_image = None
    st.session_state.current_description = ""

# --- Show new image ---
def show_new_image():
    remaining = [i for i in range(1, total_images + 1) if i not in st.session_state.shown_images]
    if not remaining:
        st.session_state.shown_images = []
        remaining = list(range(1, total_images + 1))

    chosen_number = random.choice(remaining)
    st.session_state.shown_images.append(chosen_number)

    file_path = os.path.join(folder_path, f"{chosen_number}.png")
    if os.path.exists(file_path):
        st.session_state.current_image = file_path
        st.session_state.current_description = get_description(chosen_number)
    else:
        st.error(f"Slika {chosen_number}.png nije pronađena!")

# --- UI ---
if st.button("🎴 Prikaži novu sliku"):
    show_new_image()

if st.session_state.current_image:
    st.image(st.session_state.current_image, width=600)
    if st.button("📄 Prikaži opis"):
        st.markdown(f"### Opis:\n{st.session_state.current_description}")

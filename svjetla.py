import os
import random
import streamlit as st
from PIL import Image

# Folder and total images setup
folder_path = './Brodska_Svjetla'  # Use a relative path for your image folder
total_images = 39
shown_images = []

# Description generation based on image number
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
        14: "Tegljenje brod/objekt ili brod na vesla ili jedrenjak",
        15: "Motorni brod kraci/dulji od 50m, tegalj dulji od 200m",
        16: "Slabo uocljiv ili uronjen brod/objekt koji se tegli",
        17: "Brod dulji od 50m koji kocari i usidren je (nema bocnih svjetala)",
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
        28: "Motorni brod <50m koji tegli, ogranicenog manevra, tegalj kraci od 200m",
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

def get_new_image():
    global shown_images

    # Reset if all images have been shown
    if len(shown_images) == total_images:
        shown_images = []

    # Pick a new number that hasn't been shown yet
    remaining = [i for i in range(1, total_images + 1) if i not in shown_images]
    chosen_number = random.choice(remaining)
    shown_images.append(chosen_number)

    filename = f"{chosen_number}.png"
    return os.path.join(folder_path, filename), chosen_number

# Streamlit code
st.title("Svjetla na plovilima i dnevne oznake")

# Store whether an image has been shown or not in session state
if "image_shown" not in st.session_state:
    st.session_state.image_shown = False
    st.session_state.image_path = None
    st.session_state.image_number = None
    st.session_state.show_description = False  # Store description visibility status

# Add two buttons next to each other (show image and show description)
col1, col2 = st.columns([1, 1])  # Create two columns

# Show image when "Pokazi sliku" is clicked
with col1:
    if st.button('Pokazi sliku'):
        # Remove any description if shown
        st.session_state.show_description = False

        # Show a new image
        image_path, image_number = get_new_image()
        if os.path.exists(image_path):
            # Save the image path and number to session state
            st.session_state.image_shown = True
            st.session_state.image_path = image_path
            st.session_state.image_number = image_number
            # Show image (Increase image size)
            img = Image.open(image_path)
            st.image(img, caption=f"Image {image_number}", use_container_width=True)  # Use the full width
        else:
            st.error("Image not found.")

# Show description when "Pokazi opis" is clicked
with col2:
    if st.button('Pokazi opis') and st.session_state.image_shown:
        st.session_state.show_description = True

# Show description under the image if it's shown, but keep the image
if st.session_state.image_shown and st.session_state.show_description:
    description = get_description(st.session_state.image_number)
    st.text(description)

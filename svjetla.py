import os
import random
from PIL import Image, ImageTk
import tkinter as tk

# Folder and total images setup
folder_path = r'/Users/brunabrozovic/Desktop/Brodska_Svjetla'  
total_images = 39
shown_images = []

# Description generation based on image number
def get_description(image_number):
    if image_number == 1:
        return "Motorni brod dulji od 50m"
    elif image_number == 2:
        return "Motorni brod kraci od 50m"
    elif image_number == 3:
        return "Motorni brod kraci od 12m (15m)"
    elif image_number == 4:
        return "Motorni brod kraci od 7m, max brzina 7 cvorova"
    elif image_number == 5:
        return "Brod na vesla ili Jedrilica koja plovi (do 20m), manja od 7m moze imati samo kruzno bijelo"
    elif image_number == 6:
        return "Jedrilica koja plovi dulja od 20m"
    elif image_number == 7:
        return "Jedrilica koja istodobno koristi i motor danju"
    elif image_number == 8:
        return "Brod na vesla ili Jedrilica koja plovi (do 20m), manja od 7m moze imati samo kruzno bijelo"
    elif image_number == 9:
        return "Motorni brod kraci od 50m ,tegalj kraci od 200m"
    elif image_number == 10:
        return "Motorni brod kraci od 50m ,tegalj dulji od 200m"
    elif image_number == 11:
        return "Motorni brod dulji od 50m ,tegalj kraci od 200m"
    elif image_number == 12:
        return "Motorni brod dulji od 50m ,tegalj dulji od 200m"
    elif image_number == 13:
        return "Motorni brod kraci od 50m, tegli bocno"
    elif image_number == 14:
        return "tegljeni brod/objekt ili brod na vesla ili jedrenjak"
    elif image_number == 15:
        return "Motorni brod kraci/dulji od 50m, tegalj dulji od 200m"
    elif image_number == 16:
        return "Slabo uocljiv ili uronjen brod/objekt koji se tegli"
    elif image_number == 17:
        return "Brod dulji od 50m koji kocari i usidern je (nema bocnih svjetala)"
    elif image_number == 18:
        return "Brod dulji od 50m koji kocari i nije usidren"
    elif image_number == 19:
        return "Ribarica koja se ne krece <50m"
    elif image_number == 20:
        return "Ribarica koja se krece <50m"
    elif image_number == 21:
        return "Brod koji ribari ili kocari danju"
    elif image_number == 22:
        return "Brod nesposoban za manevar koji se ne krece"
    elif image_number == 23:
        return "Brod nesposoban za manevar koji se krece, <50m"
    elif image_number == 24:
        return "Brod ogranicen manevrom danju"
    elif image_number == 25:
        return "Brod ogranicen manevrom koji se ne krece, <50m"
    elif image_number == 26:
        return "Brod ogranicen manevrom koji se krece, >50m"
    elif image_number == 27:
        return "Brod ogranicenog manevra danju"
    elif image_number == 28:
        return "Motorni brod <50m koji tegli, ogranicenog mavera, tegalj kraci od 200m"
    elif image_number == 29:
        return "Brod zauzet podvodnim radovima, ogranicenog manevra koji se krece, zapreka na njegovoj desnoj strani"
    elif image_number == 30:
        return "Motorni brod koji razminirava, krece se i <50m."
    elif image_number == 31:
        return "Razminirava i sa strane se vide kao dvije kugle, ali zapravo su odnaprijed 3 u kriz."
    elif image_number == 32:
        return "Motorni brod ogranicen gazom, dulji od 50m koji se krece."
    elif image_number == 33:
        return "Motorni brod ogranicen gazom danju."
    elif image_number == 34:
        return "Peljar koji se krece, manji od 50m. Danju H-zastavica."
    elif image_number == 35:
        return "Motorni brod usidren, dulji od 50m."
    elif image_number == 36:
        return "Usidreni brod manji od 50m. "
    elif image_number == 37:
        return "Usidreni brod danju. (kraci od 7m ne moraju ovo pokazivati)"
    elif image_number == 38:
        return "Nasukani brod (usidren i nesposoban manevrom). (ako je kraci od 12m, ne mora) "
    elif image_number == 39:
        return "Nasukani brod danju (1 kugla = usidren & 2 kugle = nesposoban za manevar)"
    else:
        return "No description available."

def get_new_image():
    global shown_images

    # Reset if all images have been shown
    if len(shown_images) == total_images:
        print("All images shown. Resetting.")
        shown_images = []

    # Pick a new number that hasn't been shown yet
    remaining = [i for i in range(1, total_images + 1) if i not in shown_images]
    chosen_number = random.choice(remaining)
    shown_images.append(chosen_number)

    filename = f"{chosen_number}.png"
    return os.path.join(folder_path, filename), chosen_number

# Function to display a new image
def show_image():
    global current_image_number, current_image_path, img_tk

    image_path, image_name = get_new_image()

    if os.path.exists(image_path):
        img = Image.open(image_path)
        max_width = 800  # Max width for the image (adjusted for larger image size)
        max_height = 600  # Max height for the image (adjusted for larger image size)

        # Maintain aspect ratio
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality downsampling
        img_tk = ImageTk.PhotoImage(img)

        current_image_number = image_name  # Save the current image number globally
        current_image_path = image_path  # Save the current image path globally

        label_image.config(image=img_tk)  # Display the image in the Tkinter label
        label_image.image = img_tk  # Keep a reference to the image to prevent garbage collection

        # Clear the description label when a new image is shown
        description_label.config(text="")

    else:
        print(f"Image {image_name} not found.")

# Function to show the description for the currently displayed image
def show_description():
    if 'current_image_number' in globals():
        image_description = get_description(current_image_number)
        description_label.config(text=f"{image_description}")  # Display description in the window
        print(f"Description: {image_description}")
    else:
        description_label.config(text="Please generate an image first to view its description.")  # Handle if no image is shown yet

# Setup the Tkinter window
root = tk.Tk()
root.title("Image Viewer and Description Generator")

# Set the window to full screen
root.attributes("-fullscreen", True)

# Set background color to blue
root.config(bg="blue")

# Frame to center the content
frame = tk.Frame(root, bg="blue")
frame.pack(expand=True)

# Frame for the buttons, placed at a reasonable height
button_frame = tk.Frame(root, bg="blue")
button_frame.pack(side=tk.BOTTOM, pady=30)  # Added pady to lift the buttons a little above the bottom

# Button to generate a photo
button_image = tk.Button(button_frame, text="Pokazi sliku", command=show_image, bg="white", font=("Arial", 16))
button_image.pack(side=tk.LEFT, padx=20)

# Button to generate a description
button_description = tk.Button(button_frame, text="Pokazi opis", command=show_description, bg="white", font=("Arial", 16))
button_description.pack(side=tk.LEFT, padx=20)

# Label to display the generated image
label_image = tk.Label(frame, bg="blue")  # This label will hold the image
label_image.pack(pady=20)

# Label to display the description (no background color)
description_label = tk.Label(frame, text="", bg="blue", fg="white", font=("Arial", 18), wraplength=800)
description_label.pack(pady=20)

# Start the Tkinter loop
root.mainloop()

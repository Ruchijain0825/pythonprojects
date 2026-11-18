
from PIL import Image, ImageTk
import tkinter as tk
from itertools import cycle

root = tk.Tk()
root.title("Image Slideshow Viewer")
root.geometry("800x700")

image_path = [
    "google_pay_qr.png",
    "paytm_qr.png",
    "phonepe_qr.png"
]

image_size = (600, 550)

# Load images
images = [
    Image.open(path).resize(image_size)
    for path in image_path
]


photo_images = [
    ImageTk.PhotoImage(image)
    for image in images
]

slideshow = cycle(photo_images)

label = tk.Label(root)
label.pack(pady=20)

is_playing = False

def update_image():
    if is_playing:
        photo_image = next(slideshow)

        label.config(image=photo_image)
        label.image = photo_image

        root.after(3000, update_image)


def start_slideshow():
    global is_playing

    if not is_playing:
        is_playing = True
        update_image()


def stop_slideshow():
    global is_playing
    is_playing = False


play_button = tk.Button(
    root,
    text="Play Slideshow",
    command=start_slideshow
)
play_button.pack(pady=10)

stop_button = tk.Button(
    root,
    text="Stop Slideshow",
    command=stop_slideshow
)
stop_button.pack(pady=10)

root.mainloop()

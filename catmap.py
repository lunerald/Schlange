import numpy as np
from PIL import Image, ImageTk
import tkinter as tk

# -------------------------------
# Arnold-Katzenkarte
# -------------------------------
def arnold_cat_map(img_array):
    N = img_array.shape[0]
    new = np.zeros_like(img_array)
    for x in range(N):
        for y in range(N):
            x_new = (x + y) % N
            y_new = (x + 2*y) % N
            new[x_new, y_new] = img_array[x, y]
    return new

# -------------------------------
# Bild laden
# -------------------------------
img = Image.open("cat.png").convert("RGB").resize((256, 256))
start_img = np.array(img)
current = start_img.copy()
history = [start_img.copy()]

# -------------------------------
# GUI
# -------------------------------
root = tk.Tk()
root.title("Arnold-Katzenkarte — Poincaré Wiederkehr")

label = tk.Label(root)
label.pack()

step_label = tk.Label(root, text=f"Schritt: 0")
step_label.pack()

paused = True
step = 0

# Bild anzeigen
def update_image(arr):
    im = Image.fromarray(arr)
    tk_im = ImageTk.PhotoImage(im)
    label.img = tk_im
    label.config(image=tk_im)
    step_label.config(text=f"Schritt: {step}")

update_image(current)

# -------------------------------
# Steuerung
# -------------------------------
def do_step():
    global current, step
    current = arnold_cat_map(current)
    history.append(current.copy())
    step += 1
    update_image(current)

    if np.array_equal(current, start_img):
        root.title(f"Wiederkehr nach {step} Schritten!")

    if not paused:
        root.after(500, do_step)

def toggle_pause():
    global paused
    paused = not paused
    if not paused:
        do_step()

def step_forward():
    global paused
    paused = True
    do_step()

def step_back():
    global step, current
    if step > 0:
        step -= 1
        current = history[step].copy()
        update_image(current)

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

toggle_btn = tk.Button(frame, text="Start / Pause", command=toggle_pause)
step_bw_btn = tk.Button(frame, text="←", command=step_back)
step_fw_btn = tk.Button(frame, text="→", command=step_forward)

toggle_btn.grid(row=0, column=0, padx=5)
step_bw_btn.grid(row=0, column=1, padx=5)
step_fw_btn.grid(row=0, column=2, padx=5)

root.mainloop()

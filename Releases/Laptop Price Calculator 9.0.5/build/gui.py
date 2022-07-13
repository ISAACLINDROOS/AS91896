# coding: utf8

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox
import tkinter as tk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def genonClick():
    messagebox.showinfo("","Message goes here")


window = tk.Tk()

window.geometry("1000x600")
window.configure(bg = "#FFFFFF")
window.title("Laptop Price Calculator")
logo = tk.PhotoImage(file=ASSETS_PATH / "usd-circle.png")
window.call('wm', 'iconphoto', window._w, logo)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    418.0,
    600.0,
    fill="#007BFF",
    outline="")

canvas.create_rectangle(
    0.0,
    60.0,
    418.0,
    507.0,
    fill="#6C757D",
    outline="")

canvas.create_rectangle(
    0.0,
    57.0,
    418.0,
    63.0,
    fill="#FFFFFF",
    outline="")
    
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    208.0,
    284.0,
    image=image_image_1
)

canvas.create_text(
    148.0,
    451.0,
    anchor="nw",
    text=" Easy, Simple!",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 20 * -1)
)

canvas.create_text(
    84.0,
    12.0,
    anchor="nw",
    text="Laptop Price Calculator",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 24 * -1)
)

canvas.create_text(
    25.0,
    80.0,
    anchor="nw",
    text="The best way to find the right laptop that works for you!",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 15 * -1)
)

canvas.create_text(
    103.0,
    545.0,
    anchor="nw",
    text="Click Generate to calculate Laptop Cost",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 12 * -1)
)

canvas.create_text(
    113.0,
    576.0,
    anchor="nw",
    text="Exit at any time to close the window",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 12 * -1)
)

canvas.create_text(
    68.0,
    514.0,
    anchor="nw",
    text="Select an option in each row according to your needs ",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 12 * -1)
)

canvas.create_text(
    603.0,
    12.0,
    anchor="nw",
    text="Find a laptop for you!",
    fill="#000000",
    font=("RobotoRoman Regular", 24 * -1)
)

canvas.create_text(
    624.0,
    65.0,
    anchor="nw",
    text="What will be the main purpose of Laptop?",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    555.0,
    579.0,
    anchor="nw",
    text="Please wait until results have been Generated before exiting this window",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    524.0,
    472.0,
    anchor="nw",
    text="Results will be shown in a seperate window ",
    fill="#000000",
    font=("RobotoRoman Regular", 20 * -1)
)

canvas.create_text(
    676.0,
    114.0,
    anchor="nw",
    text="Operating System",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    677.0,
    163.0,
    anchor="nw",
    text="Storage Capacity",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    671.0,
    212.0,
    anchor="nw",
    text="RAM (Memory) Size",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    688.0,
    261.0,
    anchor="nw",
    text="Display Size",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    687.0,
    310.0,
    anchor="nw",
    text="Touchscreen",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    677.0,
    359.0,
    anchor="nw",
    text="Brand Preference",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    700.0,
    408.0,
    anchor="nw",
    text="Notes:",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    715.0,
    441.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F5F5F5",
    highlightthickness=0
)
entry_1.place(
    x=511.0,
    y=422.0,
    width=408.0,
    height=37.0
)

canvas.create_rectangle(
    0.0,
    57.0,
    1000.0,
    63.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    106.0,
    1000.0,
    112.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    155.0,
    1000.0,
    161.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    204.0,
    1000.0,
    210.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    253.0,
    1000.0,
    259.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    302.0,
    1000.0,
    308.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    351.0,
    1000.0,
    357.0,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    400.0,
    1000.0,
    406.0,
    fill="#D9D9D9",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=genonClick,
    relief="flat"
)


button_1.place(
    x=656.0,
    y=507.0,
    width=120.0,
    height=36.44775390625
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=679.0,
    y=81.0,
    width=74.0,
    height=21.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=558.0,
    y=81.0,
    width=74.0,
    height=21.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=800.0,
    y=81.0,
    width=74.0,
    height=21.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=679.0,
    y=130.0,
    width=74.0,
    height=21.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=558.0,
    y=130.0,
    width=74.0,
    height=21.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=800.0,
    y=130.0,
    width=74.0,
    height=21.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=739.0,
    y=179.0,
    width=74.0,
    height=21.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=619.0,
    y=179.0,
    width=74.0,
    height=21.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=499.0,
    y=179.0,
    width=74.0,
    height=21.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=859.0,
    y=179.0,
    width=74.0,
    height=21.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=739.0,
    y=228.0,
    width=74.0,
    height=21.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=619.0,
    y=228.0,
    width=74.0,
    height=21.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat"
)
button_14.place(
    x=499.0,
    y=228.0,
    width=74.0,
    height=21.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
button_15.place(
    x=859.0,
    y=228.0,
    width=74.0,
    height=21.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
)
button_16.place(
    x=739.0,
    y=277.0,
    width=74.0,
    height=21.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
)
button_17.place(
    x=619.0,
    y=277.0,
    width=74.0,
    height=21.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat"
)
button_18.place(
    x=739.0,
    y=326.0,
    width=74.0,
    height=21.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
)
button_19.place(
    x=619.0,
    y=326.0,
    width=74.0,
    height=21.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_20 clicked"),
    relief="flat"
)
button_20.place(
    x=499.0,
    y=277.0,
    width=74.0,
    height=21.0
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_21 clicked"),
    relief="flat"
)
button_21.place(
    x=859.0,
    y=277.0,
    width=74.0,
    height=21.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_22 clicked"),
    relief="flat"
)
button_22.place(
    x=672.0,
    y=375.0,
    width=74.0,
    height=21.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_23 clicked"),
    relief="flat"
)
button_23.place(
    x=793.0,
    y=375.0,
    width=74.0,
    height=21.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_24 clicked"),
    relief="flat"
)
button_24.place(
    x=914.0,
    y=375.0,
    width=74.0,
    height=21.0
)

button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_25 clicked"),
    relief="flat"
)
button_25.place(
    x=551.0,
    y=375.0,
    width=74.0,
    height=21.0
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_26 clicked"),
    relief="flat"
)
button_26.place(
    x=430.0,
    y=375.0,
    width=74.0,
    height=21.0
)

button_image_27 = PhotoImage(
    file=relative_to_assets("button_27.png"))
button_27 = Button(
    image=button_image_27,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_27 clicked"),
    relief="flat"
)
button_27.place(
    x=680.0,
    y=549.0,
    width=72.0,
    height=18.44775390625
)
window.resizable(False, False)
window.mainloop()

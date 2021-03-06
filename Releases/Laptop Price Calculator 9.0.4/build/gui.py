from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1000x600")
window.configure(bg = "#FFFFFF")


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
    5.684341886080802e-14,
    418.0,
    600.0,
    fill="#007BFF",
    outline="")

canvas.create_rectangle(
    0.0,
    59.99999999999994,
    418.0,
    506.99999999999994,
    fill="#6C757D",
    outline="")

canvas.create_rectangle(
    0.0,
    56.99999999999994,
    418.0,
    62.99999999999994,
    fill="#FFFFFF",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    208.0,
    283.99999999999994,
    image=image_image_1
)

canvas.create_text(
    148.0,
    450.99999999999994,
    anchor="nw",
    text=" Easy, Simple!",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 20 * -1)
)

canvas.create_text(
    84.0,
    11.999999999999943,
    anchor="nw",
    text="Laptop Price Calculator",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 24 * -1)
)

canvas.create_text(
    25.0,
    79.99999999999994,
    anchor="nw",
    text="The best way to find the right laptop that works for you!",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 15 * -1)
)

canvas.create_text(
    0.0,
    540.0,
    anchor="nw",
    text="Click Generate to calculate Laptop Cost",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 12 * -1)
)

canvas.create_text(
    0.0,
    573.0,
    anchor="nw",
    text="Exit at any time to close the window",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 12 * -1)
)

canvas.create_text(
    0.0,
    506.99999999999994,
    anchor="nw",
    text="Select an option in each row according to your needs ",
    fill="#FFFFFF",
    font=("RobotoRoman Regular", 12 * -1)
)

canvas.create_text(
    603.0,
    11.999999999999943,
    anchor="nw",
    text="Find a laptop for you!",
    fill="#000000",
    font=("RobotoRoman Regular", 24 * -1)
)

canvas.create_text(
    624.0,
    64.99999999999994,
    anchor="nw",
    text="What will be the main purpose of Laptop?",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    555.0,
    573.0,
    anchor="nw",
    text="Please wait until results have been Generated before exiting this window",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    524.0,
    471.99999999999994,
    anchor="nw",
    text="Results will be shown in a seperate window ",
    fill="#000000",
    font=("RobotoRoman Regular", 20 * -1)
)

canvas.create_text(
    676.0,
    113.99999999999994,
    anchor="nw",
    text="Operating System",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    677.0,
    162.99999999999994,
    anchor="nw",
    text="Storage Capacity",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    671.0,
    211.99999999999994,
    anchor="nw",
    text="RAM (Memory) Size",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    688.0,
    260.99999999999994,
    anchor="nw",
    text="Display Size",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    687.0,
    309.99999999999994,
    anchor="nw",
    text="Touchscreen",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    677.0,
    358.99999999999994,
    anchor="nw",
    text="Brand Preference",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    700.0,
    407.99999999999994,
    anchor="nw",
    text="Notes:",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    715.0,
    441.49999999999994,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#F5F5F5",
    highlightthickness=0
)
entry_1.place(
    x=511.0,
    y=421.99999999999994,
    width=408.0,
    height=37.0
)

canvas.create_rectangle(
    0.0,
    56.99999999999994,
    1000.0,
    62.99999999999994,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    105.99999999999994,
    1000.0,
    111.99999999999994,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    154.99999999999994,
    1000.0,
    160.99999999999994,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    203.99999999999994,
    1000.0,
    209.99999999999994,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    252.99999999999994,
    1000.0,
    258.99999999999994,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    301.99999999999994,
    1000.0,
    307.99999999999994,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    350.99999999999994,
    1000.0,
    356.99999999999994,
    fill="#D9D9D9",
    outline="")

canvas.create_rectangle(
    418.0,
    399.99999999999994,
    1000.0,
    405.99999999999994,
    fill="#D9D9D9",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=656.0,
    y=506.99999999999994,
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
    x=680.0,
    y=549.0,
    width=72.0,
    height=18.44775390625
)
window.resizable(False, False)
window.mainloop()

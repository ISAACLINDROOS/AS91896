from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("862x519")
window.configure(bg = "#343A40")


canvas = Canvas(
    window,
    bg = "#343A40",
    height = 519,
    width = 862,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    5.684341886080802e-14,
    450.0,
    519.0,
    fill="#343A40",
    outline="")

canvas.create_rectangle(
    449.0,
    0.0,
    862.0,
    519.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    0.0,
    51.99999999999994,
    449.0,
    78.99999999999994,
    fill="#007BFF",
    outline="")

canvas.create_text(
    0.0,
    0.0,
    anchor="nw",
    text="Student Laptop Price Calculator",
    fill="#FFFFFF",
    font=("Basic Regular", 32 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    224.5,
    65.49999999999994,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=0.0,
    y=51.99999999999994,
    width=449.0,
    height=25.0
)

canvas.create_text(
    189.0,
    423.99999999999994,
    anchor="nw",
    text=" Simple!",
    fill="#FFFFFF",
    font=("Carme", 20 * -1)
)

canvas.create_text(
    17.0,
    458.99999999999994,
    anchor="nw",
    text="Select your prefrences according to your requirments & needs. Hit Go, done!  ",
    fill="#FFFFFF",
    font=("Carme", 12 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    223.0,
    258.99999999999994,
    image=image_image_1
)

canvas.create_text(
    466.0,
    14.999999999999943,
    anchor="nw",
    text="Find your laptop.",
    fill="#000000",
    font=("RobotoRoman Regular", 20 * -1)
)

canvas.create_rectangle(
    466.0,
    51.99999999999994,
    846.0,
    506.99999999999994,
    fill="#6C757D",
    outline="")

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    655.5,
    81.99999999999994,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#F8F9FA",
    highlightthickness=0
)
entry_2.place(
    x=479.0,
    y=61.99999999999994,
    width=353.0,
    height=38.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    655.5,
    125.99999999999994,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#F8F9FA",
    highlightthickness=0
)
entry_3.place(
    x=479.0,
    y=105.99999999999994,
    width=353.0,
    height=38.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    655.5,
    169.99999999999994,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#F8F9FA",
    highlightthickness=0
)
entry_4.place(
    x=479.0,
    y=149.99999999999994,
    width=353.0,
    height=38.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    655.5,
    213.99999999999994,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#F8F9FA",
    highlightthickness=0
)
entry_5.place(
    x=479.0,
    y=193.99999999999994,
    width=353.0,
    height=38.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    655.5,
    257.99999999999994,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#F8F9FA",
    highlightthickness=0
)
entry_6.place(
    x=479.0,
    y=237.99999999999994,
    width=353.0,
    height=38.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    655.5,
    301.99999999999994,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#F8F9FA",
    highlightthickness=0
)
entry_7.place(
    x=479.0,
    y=281.99999999999994,
    width=353.0,
    height=38.0
)

canvas.create_rectangle(
    476.0,
    399.99999999999994,
    835.0,
    494.99999999999994,
    fill="#F8F9FA",
    outline="")

canvas.create_text(
    478.0,
    63.99999999999994,
    anchor="nw",
    text="Device Purpose",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    478.0,
    107.99999999999994,
    anchor="nw",
    text="RAM",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    478.0,
    151.99999999999994,
    anchor="nw",
    text="Storage",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    478.0,
    195.99999999999994,
    anchor="nw",
    text="Operating System",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    478.0,
    239.99999999999994,
    anchor="nw",
    text="Battery Life",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

canvas.create_text(
    478.0,
    283.99999999999994,
    anchor="nw",
    text="Touchscreen",
    fill="#000000",
    font=("RobotoRoman Regular", 10 * -1)
)

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
    x=565.0,
    y=334.99999999999994,
    width=180.0,
    height=55.0
)
window.resizable(False, False)
window.mainloop()

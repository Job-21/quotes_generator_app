from tkinter import *
import requests

url = "https://api.kanye.rest"


def get_quote():
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    canvas.itemconfig(quote_text, text=data["quote"])


window = Tk()
window.title("Job Says...")
window.config(padx=50, pady=50)
window.resizable(False, False)

canvas = Canvas(width=350, height=474)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Job's Quotes Goes HERE, click on the image below.", width=250, font=("Arial", 30, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()

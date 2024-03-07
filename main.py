import wolframalpha
import base64
import tkinter as tk
from urllib.request import urlopen

API_KEY = 'A7JAXX-3R9AEUP8WY'
client = wolframalpha.Client(API_KEY)


def math():
    eq = entry.get()
    res = client.query(eq.strip(), params=(("format", "image,plaintext"),))
    data = {}
    for p in res.pods:
        if p.title.lower() == "plots of sample individual solutions":
            data['subPlot'] = p.subpod.img.src
        for s in p.subpods:
            if s.img.alt.lower() == "root plot":
                data['rootPlot'] = s.img.src
            elif s.img.alt.lower() == "number line":
                data['numberLine'] = s.img.src
    data['results'] = [i.texts for i in list(res.results)][0]

    items = canvas.find_all()
    for item in items:
        if item > 2:
            canvas.delete(item)

    try:
        image1_url = data['rootPlot']
        image1_byt = urlopen(image1_url).read()
        image1_b64 = base64.encodebytes(image1_byt)
        photo1 = tk.PhotoImage(data=image1_b64)
        canvas.photo1 = photo1
        canvas.create_image(w / 2, 150, image=canvas.photo1)
    except:
        pass

    try:
        image2_url = data['numberLine']
        image2_byt = urlopen(image2_url).read()
        image2_b64 = base64.encodebytes(image2_byt)
        photo2 = tk.PhotoImage(data=image2_b64)
        canvas.photo2 = photo2
        canvas.create_image(w / 2, 280, image=canvas.photo2)
    except:
        pass

    try:
        image3_url = data['subPlot']
        image3_byt = urlopen(image3_url).read()
        image3_b64 = base64.encodebytes(image3_byt)
        photo3 = tk.PhotoImage(data=image3_b64)
        canvas.photo3 = photo3
        canvas.create_image(w / 2, 150, image=canvas.photo3)
    except:
        pass

    canvas.create_text(w / 2, 400, fill="darkblue", font="Arial 15", text=data['results'])


root = tk.Tk()
root.title("Math Visualizion")

w = 800
h = 500

canvas = tk.Canvas(bg='white')
canvas.config(height=h, width=w)
canvas.pack()

entry = tk.Entry(root)
canvas.create_window(w / 2 - 50, 15, window=entry)

submit = tk.Button(text='Solve', command=math, height=1, width=3)
canvas.create_window(w / 2 + 50, 15, window=submit)

root.mainloop()
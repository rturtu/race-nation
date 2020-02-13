from PIL import Image, ImageColor, ImageDraw, ImageFont
from tkinter import Label, Entry, Button, Tk
from generation import Generation

window = Tk()

window.title("Start a new generation for more info")
window.geometry('350x200')
generation_info = Label(window, text="Hello")
generation_info.grid(column=0, row=0)

lbl1 = Label(window, text="Individuals")
lbl1.grid(row=1, column=0)
txt1 = Entry(window, width=5)
txt1.grid(row=1, column=1)
txt1.insert(0, '100')

lbl2 = Label(window, text="Gene Length")
lbl2.grid(row=2, column=0)
txt2 = Entry(window, width=5)
txt2.grid(row=2, column=1)
txt2.insert(0, '100')

current_generation = None


def create_generation():
    global current_generation
    individuals = int(txt1.get())
    gene_length = int(txt2.get())
    current_generation = Generation(individuals, gene_length)
    generation_info.configure(text=str(current_generation))


def next_generation(add_genes=0):
    global current_generation
    if current_generation is not None:
        current_generation = current_generation.get_next_generation()
        generation_info.configure(text=str(current_generation))


def get_blank_image(outside_function):
    im = Image.new('RGB', (400, 400))
    for i in range(400):
        for j in range(400):
            x = (i - 200) / 100
            y = (j - 200) / -100
            color = None
            if outside_function((x, y)):
                color = ImageColor.getcolor('red', 'RGB')
            else:
                color = ImageColor.getcolor('green', 'RGB')
            im.putpixel((i, j), color)
    return im

def draw_point(point, color=ImageColor.getcolor('black', 'RGB'), radius=1, image=None):
    if image is None:
        return
    for i in range(-radius, radius):
        for j in range(-radius, radius):
            image.putpixel((int(point[0] + i), int(point[1] + j)), color)
            print((int(point[0] + i), int(point[1] + j)))



def show_best_individual():
    global current_generation
    if current_generation is not None:
        individual = current_generation.individuals[0]
        positions = individual.fitness.positions
        im = get_blank_image(individual.fitness.is_outside)
        for position in positions:
            if position is None:
                break
            x = int(position[0] * 100 + 200)
            y = int(position[1] * -1 * 100 + 200)
            im.putpixel((x, y), ImageColor.getcolor('black', 'RGB'))
            im.putpixel((x+1, y), ImageColor.getcolor('black', 'RGB'))
            im.putpixel((x, y+1), ImageColor.getcolor('black', 'RGB'))
            im.putpixel((x+1, y+1), ImageColor.getcolor('black', 'RGB'))
        title = "#" + str(current_generation.age) + " " + individual.name + " " + str(individual.get_score())
        draw = ImageDraw.Draw(im)
        fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
        draw.text((0, 0), title, (255, 255, 255), size=20, font=fnt)
        starting_position = individual.fitness.get_first_position()
        if starting_position is not None:
            starting_position = (starting_position[0] * 100 + 200, -starting_position[1] * 100 + 200)
            draw_point(starting_position, ImageColor.getcolor('purple', 'RGB'), 3, im)
        ending_position = individual.fitness.get_last_position()
        if ending_position is not None:
            ending_position = (ending_position[0] * 100 + 200, -ending_position[1] * 100 + 200)
            draw_point(ending_position, ImageColor.getcolor('yellow', 'RGB'), 3, im)

        im.show(title=title)


btn1 = Button(window, text="Create generation", command=create_generation)
btn1.grid(row=3, column=0)

btn2 = Button(window, text="Next generation", command=next_generation)
btn2.grid(row=4, column=0)

btn3 = Button(window, text="Show best individual", command=show_best_individual)
btn3.grid(row=5, column=0)

lbl3 = Label(window, text="Gene Length")
lbl3.grid(row=6, column=0)
txt3 = Entry(window, width=5)
txt3.grid(row=6, column=1)
txt3.insert(0, '0')

window.mainloop()

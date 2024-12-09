from tkinter import *

# Функция для добавления фигуры
def Vtoroe_Okno():
    # Второе окно
    figure_window = Toplevel(root)
    figure_window.title("Фигура")
    figure_window.geometry("250x150")

    # Поля для ввода координат
    Label(figure_window, text="x1").grid(row=0, column=0, padx=5, pady=5)
    x1_entry = Entry(figure_window, width=5)
    x1_entry.grid(row=0, column=1, padx=5, pady=5)

    Label(figure_window, text="y1").grid(row=0, column=2, padx=5, pady=5)
    y1_entry = Entry(figure_window, width=5)
    y1_entry.grid(row=0, column=3, padx=5, pady=5)

    Label(figure_window, text="x2").grid(row=1, column=0, padx=5, pady=5)
    x2_entry = Entry(figure_window, width=5)
    x2_entry.grid(row=1, column=1, padx=5, pady=5)

    Label(figure_window, text="y2").grid(row=1, column=2, padx=5, pady=5)
    y2_entry = Entry(figure_window, width=5)
    y2_entry.grid(row=1, column=3, padx=5, pady=5)

    # Радиокнопки
    figure_type = StringVar(value="rectangle")
    r1 = Radiobutton(figure_window, text='Прямоугольник', variable=figure_type, value='rectangle')
    r2 = Radiobutton(figure_window, text='Овал', variable=figure_type, value='oval')

    r1.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
    r2.grid(row=2, column=2, columnspan=2, padx=5, pady=5)

    # Функция для рисования фигуры
    def Risovat():
        x1 = x1_entry.get()
        y1 = y1_entry.get()
        x2 = x2_entry.get()
        y2 = y2_entry.get()

        if x1.isdigit() and y1.isdigit() and x2.isdigit() and y2.isdigit():
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            if figure_type.get() == "rectangle":
                canvas.create_rectangle(x1, y1, x2, y2, outline="black")
            elif figure_type.get() == "oval":
                canvas.create_oval(x1, y1, x2, y2, outline="black")

            figure_window.destroy()  # Закрытие окна


    Button(figure_window, text="Нарисовать", command=Risovat).grid(row=3, column=0, columnspan=4, pady=10)


root = Tk()
root.title("Рисование")
root.geometry("400x400")


canvas = Canvas(root, width=300, height=300, bg="white")
canvas.pack(pady=10)


Button(root, text="Добавить фигуру", command=Vtoroe_Okno).pack()

root.mainloop()

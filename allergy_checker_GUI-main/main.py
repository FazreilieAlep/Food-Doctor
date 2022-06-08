from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk
import re
from tkinter import messagebox


class User:
    def __init__(self, allergens, food_name, ingredient):
        self.allergens = allergens
        self.food_name = food_name
        self.ingredient = ingredient


allergens = []


def allergens_picker_1():
    if 'egg' in allergens:
        allergens.remove('egg')
        allergen_button_1.configure(bg='white')
    else:
        allergens.append('egg')
        allergen_button_1.configure(bg="green")
    print(allergens)


def allergens_picker_2():
    if 'seafood' in allergens:
        allergens.remove('seafood')
        allergen_button_2.configure(bg='white')
    else:
        allergens.append('seafood')
        allergen_button_2.configure(bg="green")
    print(allergens)


def allergens_picker_3():
    if 'crustacean' in allergens:
        allergens.remove('crustacean')
        allergen_button_3.configure(bg='white')
    else:
        allergens.append('crustacean')
        allergen_button_3.configure(bg="green")
    print(allergens)


def allergens_picker_4():
    if 'peanut' in allergens:
        allergens.remove('peanut')
        allergen_button_4.configure(bg='white')
    else:
        allergens.append('peanut')
        allergen_button_4.configure(bg="green")
    print(allergens)


def allergens_picker_5():
    if 'tree nut' in allergens:
        allergens.remove('tree nut')
        allergen_button_5.configure(bg='white')
    else:
        allergens.append('tree nut')
        allergen_button_5.configure(bg="green")
    print(allergens)


def allergens_picker_6():
    if 'milk' in allergens:
        allergens.remove('milk')
        allergen_button_6.configure(bg='white')
    else:
        allergens.append('milk')
        allergen_button_6.configure(bg="green")
    print(allergens)


def allergens_picker_7():
    if 'gluten' in allergens:
        allergens.remove('gluten')
        allergen_button_7.configure(bg='white')
    else:
        allergens.append('gluten')
        allergen_button_7.configure(bg="green")
    print(allergens)


def allergens_picker_8():
    if 'sesame' in allergens:
        allergens.remove('sesame')
        allergen_button_8.configure(bg='white')
    else:
        allergens.append('sesame')
        allergen_button_8.configure(bg="green")
    print(allergens)


def allergens_picker_9():
    if 'celery' in allergens:
        allergens.remove('celery')
        allergen_button_9.configure(bg='white')
    else:
        allergens.append('celery')
        allergen_button_9.configure(bg="green")
    print(allergens)


def allergens_picker_10():
    if 'haram' in allergens:
        allergens.remove('haram')
        allergen_button_10.configure(bg='white')
    else:
        allergens.append('haram')
        allergen_button_10.configure(bg="green")
    print(allergens)


def check_button():
    if (len(allergens) != 0) & (len(text_1.get("1.0", 'end-1c')) != 0) & (len(text_2.get("1.0", 'end-1c')) != 0):
        print(text_1.get("1.0", 'end-1c'))
        print(text_2.get("1.0", 'end-1c'))
        allergens_final = list(set(allergens))
        print(allergens_final)
        user = User(
            allergens_final,
            text_1.get("1.0", 'end-1c'),
            text_2.get("1.0", 'end-1c')
        )
        result_page(user)
        # window.destroy()
        window.withdraw()
    else:
        print("require values")
        messagebox.showinfo("Notice", "You need to select allergens, input the food name and the food ingredients")


def result_page(user):
    window_2 = Toplevel()
    window_2.title("Result Page - " + user.food_name)
    window_2.geometry("850x450")
    window_2.resizable(0, 0)
    columns = ("Ingredient", "Conflict")
    treeview = ttk.Treeview(window_2, height=20, show="headings", columns=columns)
    treeview.column("Ingredient", width=100)
    treeview.column("Conflict", width=100)
    treeview.heading("Ingredient", text="Ingredient")
    treeview.heading("Conflict", text="Conflict")

    label_3 = Label(window_2, text="Result")
    # label_4 = Label(window_2, image=PhotoImage(file="1.png"), width=20, height=20)
    label_4 = Label(window_2, text="Ok to Eat", fg="green")
    canvas_1 = Canvas(window_2, width=30, height=30)
    x0, y0, x1, y1 = 5, 5, 20, 20
    canvas_1.create_oval(x0 + 5, y0, x1 + 5, y1, fill='green', outline='green', width=2)

    label_5 = Label(window_2, text="Extra Explanation", justify='left')
    text_3 = Text(window_2)

    # THIS IS THE TEXT USED IN THE EXTRA EXPLANATION
    text_3.insert('1.0', 'THIS IS THE CONTENT THAT INSERTED INTO THE EXTRA EXPLANATION PART')

    text_3.configure(state=DISABLED)

    treeview.grid(column=1, columnspan=4, row=0, rowspan=5, padx=5, pady=5)
    label_3.grid(column=5, row=0, sticky=NW, rowspan=2, padx=5, pady=5)
    canvas_1.grid(column=5, row=1, sticky=NW, rowspan=2, padx=5, pady=5)
    label_4.grid(column=5, row=2, sticky=NW, rowspan=2, padx=5, pady=5)
    label_5.grid(column=5, row=3, sticky=NW, rowspan=2, padx=5, pady=5)
    text_3.grid(column=5, row=4, sticky=NW, rowspan=2, padx=5, pady=5)

    for i in range(len(user.allergens)):
        treeview.insert("", i,
                        values=(user.allergens[i], bool(re.search(user.allergens[i], user.ingredient, re.IGNORECASE))))
        if bool(re.search(user.allergens[i], user.ingredient, re.IGNORECASE)):
            label_4.configure(text="Not Ok to Eat", fg="red")
            canvas_2 = Canvas(window_2, width=30, height=30)
            x0, y0, x1, y1 = 5, 5, 20, 20
            canvas_2.create_oval(x0 + 5, y0, x1 + 5, y1, fill='red', outline='red', width=2)
            canvas_2.grid(column=5, row=1, sticky=NW, rowspan=2, padx=5, pady=5)


if __name__ == '__main__':
    window = Tk()
    window.title("Food Allergy Checker")
    window.geometry("850x450")
    window.resizable(0, 0)
    allergen_button_1 = Button(window, text='egg', font=('Arial', 20), width=10, command=allergens_picker_1, bg='white')
    allergen_button_2 = Button(window, text='seafood', font=('Arial', 20), width=10,
                               command=allergens_picker_2, bg='white')
    allergen_button_3 = Button(window, text='crustacean', font=('Arial', 20), width=10,
                               command=allergens_picker_3, bg='white')
    allergen_button_4 = Button(window, text='peanut', font=('Arial', 20), width=10, command=allergens_picker_4,
                               bg='white')
    allergen_button_5 = Button(window, text='tree nut', font=('Arial', 20), width=10,
                               command=allergens_picker_5, bg='white')
    allergen_button_6 = Button(window, text='milk', font=('Arial', 20), width=10, command=allergens_picker_6,
                               bg='white')
    allergen_button_7 = Button(window, text='gluten', font=('Arial', 20), width=10, command=allergens_picker_7,
                               bg='white')
    allergen_button_8 = Button(window, text='sesame', font=('Arial', 20), width=10, command=allergens_picker_8,
                               bg='white')
    allergen_button_9 = Button(window, text='celery', font=('Arial', 20), width=10, command=allergens_picker_9,
                               bg='white')
    allergen_button_10 = Button(window, text='haram', font=('Arial', 20), width=10, command=allergens_picker_10,
                                bg='white')
    label_1 = Label(window, text="Food Name")
    text_1 = Text(window, width=12, height=2, font=('Arial', 15))

    label_2 = Label(window, text="Scanned Ingredient")
    text_2 = scrolledtext.ScrolledText(window, width=20, height=10, font=('Arial', 10))

    allergen_button_11 = Button(window, text='Check!', font=('Arial', 20), width=10, command=check_button)

    allergen_button_1.grid(column=1, row=0)
    allergen_button_2.grid(column=2, row=0)
    allergen_button_3.grid(column=3, row=0)
    allergen_button_4.grid(column=4, row=0)
    allergen_button_5.grid(column=5, row=0)
    allergen_button_6.grid(column=1, row=1)
    allergen_button_7.grid(column=2, row=1)
    allergen_button_8.grid(column=3, row=1)
    allergen_button_9.grid(column=4, row=1)
    allergen_button_10.grid(column=5, row=1)

    label_1.grid(column=3, row=2)
    text_1.grid(column=3, row=3, padx=5, pady=5)
    label_2.grid(column=3, row=4)
    text_2.grid(column=3, row=5, padx=5, pady=5)
    allergen_button_11.grid(column=3, row=6)

    window.mainloop()

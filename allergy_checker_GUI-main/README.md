# Allergy Checker (GUI)
This is a demo GUI for Allergy Checker with working functions developed using Python Tkinter.


## Button-triggered Function
#### allergens_picker_n
This is the function used to run command after the button of allergen is clicked.

n is from 1 to 10

#### check_button
This is the function used to run command after the button of check is clicked.


## Window
#### window
window variable is the first window asking user to fill in the food name, allergens and so on

#### window_2
window_2 variable is the second window showing the result

## Layout
#### grid
grid is the way to put all components in grid.

All the layout in this GUI is using grid.

Example:
```python
label_3.grid(column=5, row=0, sticky=NW, rowspan=2, padx=5, pady=5)
```

## Components Example
#### Button
```python
allergen_button_1 = Button(window, text='TEXT ON THE BUTTON', font=('Arial', 20), width=10, command=THE TRIGGTERD FUNCTION)
```
#### Text
```python
text_1 = Text(window, width=12, height=2, font=('Arial', 15))
```
#### Label
```python
label_5 = Label(window_2, text="Extra Explanation", justify='left')
```
#### scrolledtext.ScrolledText
```python
text_2 = scrolledtext.ScrolledText(window, width=20, height=10, font=('Arial', 10))
```

#### Canvas
```python
canvas_1 = Canvas(window_2, width=30, height=30)
x0, y0, x1, y1 = 5, 5, 20, 20
canvas_1.create_oval(x0 + 5, y0, x1 + 5, y1, fill='green', outline='green', width=2)
```

#### ttk.Treeview
```python
treeview = ttk.Treeview(window_2, height=20, show="headings", columns=columns)
treeview.column("Ingredient", width=100)
treeview.column("Conflict", width=100)
treeview.heading("Ingredient", text="Ingredient")
treeview.heading("Conflict", text="Conflict")
for i in range(len(user.allergens)):
    treeview.insert("", i, values=(user.allergens[i], bool(re.search(user.allergens[i], user.ingredient))))
```

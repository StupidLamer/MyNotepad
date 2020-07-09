from tkinter import *
from tkinter import messagebox, filedialog


def about_program():
    messagebox.showinfo(title='About app', message='Notepad\nVersion 0.1')


def my_quit():
    answer = messagebox.askokcancel(title='Exit', message='Are you sure?')
    if answer:
        root.destroy()


def open_file():
    file_path = filedialog.askopenfilename(title='Select file', filetypes=(('Text docs', '*.txt'),
                                                                           ('All', '*.*')))
    if file_path:
        t.delete('1.0', END)
        t.insert('1.0', open(file_path).read())


def save_file():
    file_path = filedialog.asksaveasfilename(title='Save file', filetypes=(('Text docs', '*.txt'),
                                                                           ('All', '*.*')))
    f = open(file_path, 'w')
    f.write(t.get('1.0', END))
    f.close()


def change_theme(theme):
    t['bg'] = theme_colors[theme]['text_bg']
    t['fg'] = theme_colors[theme]['text_fg']
    t['insertbackground'] = theme_colors[theme]['cursor']
    t['selectbackground'] = theme_colors[theme]['select_bg']


root = Tk()
root.geometry('800x480')

main_menu = Menu(root)
root.config(menu=main_menu)

# FILE
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=my_quit)
main_menu.add_cascade(label='File', menu=file_menu)

# THEME
theme_menu = Menu(main_menu, tearoff=0)
theme_menu_sub = Menu(theme_menu, tearoff=0)
theme_menu_sub.add_command(label='Dark', command=lambda: change_theme('dark'))
theme_menu_sub.add_command(label='Light', command=lambda: change_theme('light'))
theme_menu.add_cascade(label='Theme', menu=theme_menu_sub)
theme_menu.add_command(label='About app', command=about_program)
main_menu.add_cascade(label='Any', menu=theme_menu)


f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

theme_colors = {
    'dark': {
        'text_bg': '#343d46', 'text_fg': '#fff',
        'cursor': '#eda756', 'select_bg': '#4e5a65'
    },
    'light': {
        'text_bg': '#fff', 'text_fg': '#000',
        'cursor': '#b000ff', 'select_bg': '#777'
    }
}

t = Text(f_text, bg=theme_colors['dark']['text_bg'],
         fg=theme_colors['dark']['text_fg'],
         padx=10, pady=10, wrap=WORD,
         insertbackground=theme_colors['dark']['cursor'],
         selectbackground=theme_colors['dark']['select_bg'],
         width=30, spacing3=10, font=('Courier New', 12))
t.pack(expand=1, fill=BOTH, side=LEFT)

scroll = Scrollbar(f_text, command=t.yview)
scroll.pack(fill=Y, side=LEFT)
t.config(yscrollcommand=scroll.set)

root.mainloop()

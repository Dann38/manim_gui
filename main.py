from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import os
import shutil


class App:
    def __init__(self):
        self.PATH = os.getcwd()
        self.path_templates = os.path.join(os.path.dirname(__file__), "templates")
        self.root = Tk()

        self.frame = Frame()
        self.btn_select_file = Button(self.frame, text="Выбор файла",
                                      width=15, height=2,
                                      bg="blue", fg="yellow",
                                      command=self.create_name)
        self.filename = ""

        self.btn_create_file = Button(self.frame, text="Сборка",
                                      width=10, height=2,
                                      bg="green",
                                      command=self.create_file)

        self.btn_select_templates = Button(self.frame, text="Выбор \nшаблона",
                                           width=10, height=3,
                                           bg="yellow",
                                           command=self.create_class_manim)
        self.isPreview = BooleanVar()
        self.isPreview.set(1)
        self.check_btn_is_preview = Checkbutton(self.frame, text="Вывод результата",
                                                variable=self.isPreview,
                                                onvalue=1, offvalue=0)

        self.quality = ttk.Combobox(self.frame, values=["854x480 15FPS -l",
                                                        "1280x720 30FPS -m",
                                                        "1920x1080 60FPS -h",
                                                        "2560x1440 60FPS -p",
                                                        "3840x2160 60FPS -k"])

        self.text = Label(text="Файл не выбран")
        self.grid_root()

        self.root.mainloop()

    def grid_root(self):
        self.frame.grid(row=0, column=0)
        self.check_btn_is_preview.grid(row=0, column=0)
        self.quality.grid(row=1, column=0)
        self.btn_select_file.grid(row=0, column=1)
        self.btn_create_file.grid(row=0, column=2)
        self.btn_select_templates.grid(row=0, column=3)
        self.text.grid(row=1)

    def create_name(self):
        self.filename = filedialog.askopenfilename(initialdir=self.PATH, title="Select file",
                                                   filetypes=(("python files", "*.py"), ("all files", "*.*")))
        self.text.config(text=self.filename)

    def create_file(self):
        q = self.quality.get()
        if q != "":
            q = q.split('-')[1]
        else:
            return

        if self.filename != "":
            os.system(f"manim { '-p' if self.isPreview.get() else ''} -q{q} {self.filename}")

    def create_class_manim(self):
        self.set_templates_form = Toplevel(self.root)

        btn = Button(self.set_templates_form, text="Создать",
                     width=15, height=2,
                     bg="blue", fg="yellow",
                     command=self.create_file_templates)

        templates_py_name = os.listdir(self.path_templates)
        self.files_templates = ttk.Combobox(self.set_templates_form,
                             values=templates_py_name)
        self.files_templates.grid(row=0, column=0)
        btn.grid(row=1, column=0)

    def create_file_templates(self):
        file = os.path.join(self.path_templates, self.files_templates.get())
        new_file = os.path.join(self.PATH, self.files_templates.get())
        shutil.copy(file, new_file)
        self.set_templates_form.destroy()


App()

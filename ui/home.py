import tkinter as tk
import customtkinter as ctk

class Home(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.create_widgets()
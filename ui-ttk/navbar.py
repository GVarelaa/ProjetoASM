import tkinter as tk
import customtkinter as ctk

class NavBar(ctk.CTkFrame):
    def __init__(self, master=None, page_switch_callback=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.page_switch_callback = page_switch_callback
        self.create_widgets()

    def create_widgets(self):
        home_container = ctk.CTkFrame(self)
        home_container.pack(side=tk.LEFT, padx=(10,0), pady=(15,15))
        self.home_button = ctk.CTkButton(home_container, text="Home", command=lambda: self.page_switch_callback('home'))
        self.home_button.pack(side=tk.LEFT, padx=(10,0), pady=(15,15))
        self.home_button.pack(side=tk.LEFT)

        influencers_container = ctk.CTkFrame(self)
        influencers_container.pack(side=tk.LEFT, padx=(10,0), pady=(15,15))
        self.influencers_button = ctk.CTkButton(influencers_container, text="Influencers", command=lambda: self.page_switch_callback('influencers'))
        self.influencers_button.pack(side=tk.LEFT)

        history_container = ctk.CTkFrame(self)
        history_container.pack(side=tk.LEFT, padx=(10,0), pady=(15,15))
        self.history_button = ctk.CTkButton(history_container, text="History", command=lambda: self.page_switch_callback('history'))
        self.history_button.pack(side=tk.LEFT)
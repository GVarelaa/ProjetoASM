import tkinter as tk
import customtkinter as ctk

class Influencers(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.influencers = ["gui", "gabs"]
        self.create_widgets()


    def create_widgets(self):
        self.display_area = ctk.CTkFrame(self)
        self.display_area.pack(fill="both", expand=True, pady=20)

        self.label = ctk.CTkLabel(self, text="Add New Influencer")
        self.label.pack(pady=(20, 10))

        self.entry = ctk.CTkEntry(self)
        self.entry.pack()

        self.add_button = ctk.CTkButton(self, text="Add", command=self.add_influencer)
        self.add_button.pack(pady=10)

        self.update_display()


    def add_influencer(self):
        name = self.entry.get()
        if name:
            self.influencers.append(name)
            self.update_display()


    def update_display(self):
        # Clear the display area
        for widget in self.display_area.winfo_children():
            widget.destroy()

        # Display each influencer with a remove button
        for idx, name in enumerate(self.influencers):
            frame = ctk.CTkFrame(self.display_area)
            frame.pack(fill="x", pady=5)
            label = ctk.CTkLabel(frame, text=name)
            label.pack(side="left", padx=10)
            remove_button = ctk.CTkButton(frame, text="Remove", command=lambda idx=idx: self.remove_influencer(idx))
            remove_button.pack(side="right")


    def remove_influencer(self, idx):
        del self.influencers[idx]
        self.update_display()

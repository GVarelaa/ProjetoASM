# Importing Tkinter Library
import tkinter as tk
import customtkinter as ctk
from navbar import NavBar
from influencers import Influencers

class MainApplication(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Portfolio Manager")
        
        # Setting up theme of your app
        ctk.set_appearance_mode("dark")
        
        # Setting up theme of your components
        ctk.set_default_color_theme("dark-blue")
        
        # Creating Window of our App
        root = ctk.CTk()

        # Settings Window width and height
        root.geometry('1280x720')

        # Initialize navbar with a reference to the page switching function
        self.nav_bar = NavBar(self, page_switch_callback=self.switch_page)
        self.nav_bar.pack(side="top", fill="x")

        # Dictionary to hold the different pages
        self.pages = {}
        self.create_pages()


    def create_pages(self):
        self.pages['home'] = ctk.CTkFrame(self, width=800, height=500)
        home_label = ctk.CTkLabel(self.pages['home'], text="Home Page")
        home_label.pack(pady=20)

        self.pages['influencers'] = Influencers(self)

        self.pages['history'] = ctk.CTkFrame(self, width=800, height=500)
        history_label = ctk.CTkLabel(self.pages['history'], text="History Page")
        history_label.pack(pady=20)

        # Start with the Home page
        self.pages['home'].pack(fill="both", expand=True)


    def switch_page(self, page_name):
        # Hide all pages
        for page in self.pages.values():
            page.pack_forget()

        # Show the requested page
        self.pages[page_name].pack(fill="both", expand=True)

# Running the app
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
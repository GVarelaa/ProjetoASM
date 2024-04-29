import ttkbootstrap as ttk
from influencers import InfluencersPage
from settings import SettingsPage
from history import HistoryPage

class MainPage:
    def __init__(self):
        self.root = ttk.Window(themename="vapor")
        self.root.title("Portfolio Manager")
        self.root.geometry("600x500")

        self.create_widgets()

    def create_widgets(self):
        
        # Logo
        # Label para exibir o texto "Portfolio Manager"
        label = ttk.Label(self.root, text="Portfolio Manager", font=('Lato', 42), bootstyle="light")
        label.pack(pady=(130,0))
        
        # Influencer
        influencers_button = ttk.Button(bootstyle="light-outline", text="Influencers", width=30,command=self.open_influencers_page)
        influencers_button.pack(pady=(50,0))
        
        # History
        history_button = ttk.Button(bootstyle="light-outline", text="History", width=30,command=self.open_history_page)
        history_button.pack(pady=(15,0))
        
        # Settings
        settings_button = ttk.Button(bootstyle="light-outline", text="Settings", width=30,command=self.open_settings_page)
        settings_button.pack(pady=(15,0))

    def open_influencers_page(self):
        self.root.destroy()  # Close current window
        ttk.Style.instance = None
        InfluencersPage()
        

    def open_history_page(self):
        self.root.destroy()  # Close current window
        ttk.Style.instance = None
        HistoryPage()

    def open_settings_page(self):
        self.root.destroy()  # Close current window
        ttk.Style.instance = None
        SettingsPage()
        
        

if __name__ == "__main__":
    app = MainPage()
    app.root.mainloop()

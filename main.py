import ttkbootstrap as ttk
from ui.influencers import InfluencersPage
from ui.settings import SettingsPage
from ui.history import HistoryPage
from ui.portfolio import PortfolioPage
from agents.manager import ManagerAgent
from agents.collector import CollectorAgent
from agents.mapper import MapperAgent
from agents.caller import CallerAgent
from agents.manager import ManagerAgent
from spade import quit_spade
import time



XMPP_SERVER = 'localhost'
PASSWORD = 'admin'




class MainPage:
    def __init__(self, manager: ManagerAgent):
        self.root = ttk.Window(themename="vapor")
        self.root.title("Portfolio Manager")
        self.root.geometry("600x500")
        self.manager  = manager
        
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
        
        # Portfolio
        portfolio_button = ttk.Button(bootstyle="light-outline", text="Portfolio", width=30,command=self.open_portfolio_page)
        portfolio_button.pack(pady=(15,0))

    def open_influencers_page(self):
        self.root.destroy()  # Close current window
        ttk.Style.instance = None
        InfluencersPage(self.manager)
        

    def open_history_page(self):
        self.root.destroy()  # Close current window
        ttk.Style.instance = None
        HistoryPage(self.manager)

    def open_settings_page(self):
        self.root.destroy()  # Close current window
        ttk.Style.instance = None
        SettingsPage(self.manager)
    
    def open_portfolio_page(self):
        self.root.destroy()
        ttk.Style.instance = None
        PortfolioPage(self.manager)
        

if __name__ == "__main__":
    
    caller = CallerAgent(f"caller@{XMPP_SERVER}", PASSWORD)
    manager = ManagerAgent(f"manager@{XMPP_SERVER}", PASSWORD)

    res_manager = manager.start(auto_register=True)
    res_manager.result()

    time.sleep(1)
   
    #res_caller = caller.start(auto_register=True)
    #res_caller.result()
    
    app = MainPage(manager)
    app.root.mainloop()
    
  
    
    time.sleep(1)

        # Handle interruption of all agents
    while manager.is_alive():
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            # stop all agents
            caller.stop()
            manager.stop()

            break

    print("Agents finished")

    quit_spade()
    
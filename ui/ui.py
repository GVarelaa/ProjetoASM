import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from agents.manager import ManagerAgent
from agents.caller import CallerAgent

influencers = []
influencers_agents = {}

XMPP_SERVER = 'localhost'
PASSWORD = 'admin'

class PortfolioPage:   
    def __init__(self, manager):
        self.root = ttk.Window(themename="vapor")
        self.root.title("Settings")
        self.root.geometry("800x600")
        self.current_page = 1
        self.rows_per_page = 10
        self.manager = manager
        #vou assumir que a wallet seja assim
        self.wallet = self.manager.get_portfolio()


        self.create_widgets()
    
    def create_widgets(self):
        # Label for the page title
        title_label = ttk.Label(self.root, text="Portfolio", font=('Lato', 30), bootstyle="light")
        title_label.pack(pady=10)
        
        # Frame
        frame = ttk.Frame(self.root, bootstyle="dark")
        frame.pack(padx=20, pady=20)
        
        total = ttk.Label(frame, text=f"Total: {self.calcular_total_criptomoedas()}", bootstyle="light", font=('Lato', 18, 'bold'))
        total.pack(pady=5)
        
        coldata = [
            {"text": "Crypto", "stretch": False},
            "Quantity",
            {"text": "Price", "stretch": True},
            {"text": "Total Value", "stretch": False},
        ]   
        
        rowdata = []
        
        for criptomoeda, (quantidade, valor) in self.wallet.items():
            rowdata.append((criptomoeda, quantidade, valor, quantidade * valor))
        
        dt = Tableview(
            master=self.root,
            coldata=coldata,
            rowdata=rowdata,
            paginated=True,
            searchable=True,
            bootstyle=PRIMARY,
            stripecolor=(None, None),
        )
        dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)
        
        
        # Button to go back to the previous page
        return_button = ttk.Button(self.root, text="Back", command=self.return_to_main, bootstyle="light-outline")
        return_button.pack(pady=50)
    
    def calcular_total_criptomoedas(self):
        total = 0
        for criptomoeda, (quantidade, valor) in self.wallet.items():
            total += quantidade * valor
        return total

        
    def return_to_main(self):
        # Import MainPage class here to avoid circular import
        from main import MainPage
        
        # Destroy current page
        self.root.destroy()

        # Create and display Main page
        ttk.Style.instance = None
        MainPage(self.manager)


class SettingsPage:
    def __init__(self, manager):
        self.root = ttk.Window(themename="vapor")
        self.root.title("Settings")
        self.root.geometry("600x500")
        self.manager = manager
        self.threshold_value = self.manager.get_threshold()
        self.loss_value = self.manager.get_loss()

        self.create_widgets()

    def create_widgets(self):
        
        # Label for the page title
        title_label = ttk.Label(self.root, text="Settings", font=('Lato', 30), bootstyle="light")
        title_label.pack(pady=10)
        
       # Frame to contain label, textbox, and button
        frame = ttk.Frame(self.root)
        frame.pack(pady=20)

        #Threshold
        # Label for displaying current threshold value
        self.current_threshold_label = ttk.Label(frame, text=f"Threshold: {self.threshold_value}", bootstyle="light", font=('Lato', 18, 'bold'))
        self.current_threshold_label.grid(row=0, column=0, padx=(0, 5))

        # Text box for entering new threshold value
        self.threshold_entry = ttk.Entry(frame, width=15, style="primary.TEntry")
        self.threshold_entry.insert(0,self.threshold_value)  # Set initial value
        self.threshold_entry.grid(row=0, column=1, padx=(50,0))

        # Button to save new threshold value
        save_button = ttk.Button(frame, text="Change", command=self.save_threshold, bootstyle="light-outline")
        save_button.grid(row=0, column=2, padx=(15, 0))
        
        
        #Loss
        # Label for displaying current loss value
        self.current_loss_label = ttk.Label(frame, text=f"Loss: {self.loss_value}", bootstyle="light", font=('Lato', 18, 'bold'))
        self.current_loss_label.grid(row=1, column=0, padx=(0, 5), pady=(20,0))
        
        # Text box for entering new loss value
        self.loss_entry = ttk.Entry(frame, width=15, style="primary.TEntry")
        self.loss_entry.insert(0,self.loss_value)
        self.loss_entry.grid(row=1, column=1, padx=(50,0), pady=(20,0))
        
        # Button to save new loss value
        save_button_loss= ttk.Button(frame, text="Change", command=self.save_loss, bootstyle="light-outline")
        save_button_loss.grid(row=1, column=2, padx=(15, 0), pady=(20,0))
        
        # Button to go back to the previous page
        return_button = ttk.Button(self.root, text="Back", command=self.return_to_main, bootstyle="light-outline")
        return_button.pack(pady=100)
        
    def save_threshold(self):
        # Get the threshold value from the entry widget
        threshold_value = self.threshold_entry.get()
        # Process the threshold value as needed (e.g., save to file, update configuration)
        self.threshold_value = threshold_value
        self.current_threshold_label.config(text=f"Threshold: {self.threshold_value}")
        self.manager.set_threshold(self.threshold_value)
        toast = ToastNotification(
            title="Settings",
            message="Threshold value successfully saved!",
            duration=3000,
            bootstyle="dark",
            position=(70,30,"ne")
        )
        toast.show_toast()

    
    def save_loss(self):
        loss_value = self.loss_entry.get()
        self.loss_value = loss_value
        self.current_loss_label.config(text=f"Loss: {self.loss_value}")
        self.manager.set_loss(self.loss_value)
        toast = ToastNotification(
            title="Settings",
            message="Loss value successfully saved!",
            duration=3000,
            bootstyle="dark",
        )
        toast.show_toast()
    
    def return_to_main(self):
        # Import MainPage class here to avoid circular import
        from main import MainPage
        
        # Destroy current page
        self.root.destroy()

        # Create and display Main page
        ttk.Style.instance = None
        MainPage(self.manager)
    

class HistoryPage:
    def __init__(self, manager):
        self.root = ttk.Window(themename="vapor")
        self.root.title("History")
        self.root.geometry("600x500")
        self.manager = manager
        self.history_data = self.manager.get_history()
        self.current_page = 1
        self.rows_per_page = 10
        

        self.create_widgets()

    def create_widgets(self):
        
        # Label for the page title
        title_label = ttk.Label(self.root, text="History", font=('Lato', 30), bootstyle="light")
        title_label.pack(pady=10)
        
        frame = ttk.Frame(self.root, bootstyle="dark")
        frame.pack(padx=20, pady=20)

        # Calcular o índice inicial e final para a página atual
        start_index = (self.current_page - 1) * self.rows_per_page
        end_index = min(start_index + self.rows_per_page, len(self.history_data))
        
        if len(self.history_data) == 0:
            label = ttk.Label(frame, text="No data available", bootstyle="light")
            label.pack(anchor="w", pady=5)

        else:
            # Exibir as strings na página atual
            for i in range(start_index, end_index):
                label = ttk.Label(frame, text=self.history_data[i], bootstyle="light")
                label.pack(anchor="w",padx=(30,0),pady=5)

            # Adicionar controles de paginação, se necessário
            if len(self.history_data) > self.rows_per_page:
                pagination_frame = ttk.Frame(self.root)  # Frame para os botões de paginação com estilo padrão
                pagination_frame.pack()
                self.create_pagination_controls(pagination_frame)
        
    
        
        # Button to go back to the previous page
        return_button = ttk.Button(self.root, text="Back", command=self.return_to_main, bootstyle="light-outline")
        return_button.pack()
    
    def create_pagination_controls(self, frame):
        # Calcular o número total de páginas
        total_pages = (len(self.history_data) + self.rows_per_page - 1) // self.rows_per_page

        # Botão "Página Anterior"
        prev_button = ttk.Button(frame, text="Página Anterior", command=self.prev_page, bootstyle="light-outline")
        prev_button.pack(side="left", padx=5, pady=15)

        # Label para exibir a página atual e o número total de páginas
        page_label = ttk.Label(frame, text=f"Página {self.current_page}/{total_pages}", bootstyle="light")
        page_label.pack(side="left", padx=5)

        # Botão "Próxima Página"
        next_button = ttk.Button(frame, text="Próxima Página", command=self.next_page, bootstyle="light-outline")
        next_button.pack(side="left", padx=5)

    def prev_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.refresh_page()

    def next_page(self):
        total_pages = (len(self.history_data) + self.rows_per_page - 1) // self.rows_per_page
        if self.current_page < total_pages:
            self.current_page += 1
            self.refresh_page()

    def refresh_page(self):
        # Limpar o frame atual
        for widget in self.root.winfo_children():
            widget.destroy()
        # Criar novamente os widgets com a página atualizada
        self.create_widgets()
    
    def return_to_main(self):
        # Import MainPage class here to avoid circular import
        from main import MainPage
        
        # Destroy current page
        self.root.destroy()

        # Create and display Main page
        ttk.Style.instance = None
        MainPage(self.manager)



class InfluencersPage:
    def __init__(self, manager):
        self.root = ttk.Window(themename="vapor")
        self.root.title("Influencers")
        self.root.geometry("600x500")
        self.manager = manager

        self.create_widgets()

    def create_widgets(self):
        # Label for the page title
        title_label = ttk.Label(self.root, text="Influencers", font=('Lato', 18), bootstyle="light")
        title_label.pack(pady=10)
        
        # Frame for adding an influencer
        add_frame = ttk.Frame(self.root)
        add_frame.pack(fill='x', padx=10, pady=5)

        # Text box to enter the influencer name
        self.influencer_entry = ttk.Entry(add_frame, width=50)
        self.influencer_entry.pack(side='left', padx=(15, 5))  # Add padding to the right side of the entry widget

        # Button to add the influencer
        add_button = ttk.Button(add_frame, width=10, text="Add", command=self.add_influencer, bootstyle="light-outline")
        add_button.pack(side='left', padx=(15, 0))  # Add padding to the left side of the button

        # Frame to contain the list of influencers
        self.influencers_frame = ttk.Frame(self.root, bootstyle="dark")
        self.influencers_frame.pack(expand=True, fill='both', pady=10)

        # List of influencers
        self.influencer_widgets = []
        for influencer in influencers:
            influencer_frame = ttk.Frame(self.influencers_frame)
            influencer_frame.pack(fill='x', padx=10, pady=5)

            influencer_label = ttk.Label(influencer_frame, font=('Lato', 12, 'bold'),text=influencer, bootstyle="light")
            influencer_label.pack(side='left')

            remove_button = ttk.Button(influencer_frame, text="Remove", command=lambda i=influencer: self.remove_influencer(i), bootstyle="light-outline")
            remove_button.pack(side='right')

            self.influencer_widgets.append((influencer_frame, influencer_label, remove_button))

        # Button to go back to the previous page
        return_button = ttk.Button(self.root, text="Back", command=self.return_to_main, bootstyle="light-outline")
        return_button.pack(pady=10)
        

    def add_influencer(self):
        influencer_name = self.influencer_entry.get()  # Get the influencer name from the entry widget
        if influencer_name:  # Check if the influencer name is not empty
            influencers.append(influencer_name) 
            
            caller = CallerAgent(f"{influencer_name}@{XMPP_SERVER}", PASSWORD)

            caller.start(auto_register=True)

            influencers_agents[influencer_name] = caller

            self.update_widgets()  # Update the widgets to reflect the changes
        else:
            # You may want to display a message or handle empty input differently
            print("Please enter a valid influencer name.")

    def remove_influencer(self, influencer):
        influencers.remove(influencer)
        influencers_agents[influencer].stop()
        del influencers_agents[influencer]
        
        self.update_widgets()

    def update_widgets(self):
        # Clear the influencers frame
        for widget_tuple in self.influencer_widgets:
            widget_tuple[0].destroy()

        # Recreate the widgets for each updated influencer
        self.influencer_widgets.clear()
        for influencer in influencers:
            influencer_frame = ttk.Frame(self.influencers_frame)
            influencer_frame.pack(fill='x', padx=10, pady=5)

            influencer_label = ttk.Label(influencer_frame, font=('Lato', 12, 'bold'),text=influencer, bootstyle="light")
            influencer_label.pack(side='left')

            remove_button = ttk.Button(influencer_frame, text="Remove", command=lambda i=influencer: self.remove_influencer(i), bootstyle="light-outline")
            remove_button.pack(side='right')

            self.influencer_widgets.append((influencer_frame, influencer_label, remove_button))
    
    def return_to_main(self):
        # Import MainPage class here to avoid circular import
        from main import MainPage
        
        # Destroy current page
        self.root.destroy()

        # Create and display Main page
        ttk.Style.instance = None
        MainPage(self.manager)
        

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
    
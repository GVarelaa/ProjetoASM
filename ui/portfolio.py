import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *


class PortfolioPage:   
    def __init__(self):
        self.root = ttk.Window(themename="vapor")
        self.root.title("Settings")
        self.root.geometry("800x600")
        self.current_page = 1
        self.rows_per_page = 10
        
        #vou assumir que a wallet seja assim
        self.wallet = {
            "Bitcoin": (10.0, 5.0),
            "Ethereum": (5, 3.0),
            "Litecoin": (10, 2.0),
            "Ripple": (10, 1.5),
            "Bitcoin Cash": (15, 6.0),
            "Cardano": (8, 1.2),
            "Polkadot": (12, 4.5),
            "Stellar": (20, 0.8),
            "Chainlink": (6, 5.2),
            "USD Coin": (100, 1.0),
            "Binance Coin": (3, 20.0),
            "Tether": (200, 1.0),
            "Dogecoin": (50, 0.3),
            "Wrapped Bitcoin": (7, 40000.0),
            "Uniswap": (25, 30.0),
            "Bitcoin SV": (4, 180.0),
            "Aave": (2, 400.0),
            "EOS": (30, 3.5),
            "Monero": (3, 150.0),
            "TRON": (500, 0.05),
            "NEO": (12, 20.0)
        }


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
        MainPage()

if __name__ == "__main__":
    app = PortfolioPage()
    app.root.mainloop()
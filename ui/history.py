import ttkbootstrap as ttk

class HistoryPage:
    def __init__(self):
        self.root = ttk.Window(themename="vapor")
        self.root.title("History")
        self.root.geometry("600x500")
        self.history_data = ["JohnDoe : selling 7 of Ethereum at 13974.87",
    "JohnDoe : buying 3 of Litecoin at 23150.47",
    "JohnDoe : buying 2 of Bitcoin at 35298.93",
    "JohnDoe : buying 1 of Litecoin at 28477.35",
    "JohnDoe : buying 10 of Ethereum at 36615.44",
    "JohnDoe : buying 4 of Bitcoin at 30194.38",
    "JohnDoe : buying 3 of Ripple at 14872.55",
    "JohnDoe : selling 10 of Litecoin at 17177.79",
    "JohnDoe : buying 5 of Ripple at 28326.31",
    "JohnDoe : selling 3 of Ripple at 26331.95",
    "JohnDoe : selling 7 of Ethereum at 13974.87",
    "JohnDoe : buying 3 of Litecoin at 23150.47",
    "JohnDoe : buying 2 of Bitcoin at 35298.93",
    "JohnDoe : buying 1 of Litecoin at 28477.35",
    "JohnDoe : buying 10 of Ethereum at 36615.44",
    "JohnDoe : buying 4 of Bitcoin at 30194.38",
    "JohnDoe : buying 3 of Ripple at 14872.55",
    "JohnDoe : selling 10 of Litecoin at 17177.79",
    "JohnDoe : buying 5 of Ripple at 28326.31",
    "JohnDoe : selling 3 of Ripple at 26331.95",
    "JohnDoe : buying 8 of Ethereum at 22937.68",
    "JohnDoe : selling 6 of Bitcoin at 41544.73",
    "JohnDoe : selling 2 of Litecoin at 42613.39",
    "JohnDoe : buying 7 of Bitcoin at 17697.01",
    "JohnDoe : buying 9 of Ethereum at 43480.67",
    "JohnDoe : selling 5 of Ethereum at 29412.56",
    "JohnDoe : buying 10 of Bitcoin at 42602.23",
    "JohnDoe : selling 4 of Ripple at 20268.89",
    "JohnDoe : buying 6 of Litecoin at 41815.12",
    "JohnDoe : selling 1 of Bitcoin at 38518.26",
    "JohnDoe : selling 9 of Litecoin at 20814.61",
    "JohnDoe : selling 8 of Ripple at 22707.09",
    "JohnDoe : buying 2 of Ethereum at 24352.03",
    "JohnDoe : selling 5 of Litecoin at 19364.14",
    "JohnDoe : buying 4 of Ripple at 14123.99",
    "JohnDoe : selling 7 of Bitcoin at 43621.89",
    "JohnDoe : buying 1 of Ethereum at 47983.38",
    "JohnDoe : buying 6 of Ripple at 33601.81",
    "JohnDoe : buying 3 of Litecoin at 37792.76",
    "JohnDoe : selling 10 of Ethereum at 48928.17"]
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
        MainPage()
    
        
if __name__ == "__main__":
    app = HistoryPage()
    app.root.mainloop()

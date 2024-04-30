import ttkbootstrap as ttk

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
    
        
if __name__ == "__main__":
    app = HistoryPage()
    app.root.mainloop()

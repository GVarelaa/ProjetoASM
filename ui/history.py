import ttkbootstrap as ttk

class HistoryPage:
    def __init__(self):
        self.root = ttk.Window(themename="vapor")
        self.root.title("History")
        self.root.geometry("600x500")
        

        self.create_widgets()

    def create_widgets(self):
        
        # Label for the page title
        title_label = ttk.Label(self.root, text="History", font=('Lato', 30), bootstyle="light")
        title_label.pack(pady=10)
        
    
        
        # Button to go back to the previous page
        return_button = ttk.Button(self.root, text="Back", command=self.return_to_main, bootstyle="light-outline")
        return_button.pack(pady=100)
    
    
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

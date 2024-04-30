import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification

class SettingsPage:
    def __init__(self):
        self.root = ttk.Window(themename="vapor")
        self.root.title("Settings")
        self.root.geometry("600x500")
        self.threshold_value = 0
        self.loss_value = 0

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
        MainPage()
    
        
if __name__ == "__main__":
    app = SettingsPage()
    app.root.mainloop()

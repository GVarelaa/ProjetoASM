import ttkbootstrap as ttk

class InfluencersPage:
    def __init__(self, manager):
        self.root = ttk.Window(themename="vapor")
        self.manager = manager
        self.influencers =  self.manager.get_influencers()
        self.root.title("Influencers")
        self.root.geometry("600x500")

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
        add_button = ttk.Button(add_frame, width=10,text="Add", command=self.add_influencer, bootstyle="light-outline")
        add_button.pack(side='left', padx=(15, 0))  # Add padding to the left side of the button


        # Frame to contain the list of influencers
        self.influencers_frame = ttk.Frame(self.root, bootstyle="dark")
        self.influencers_frame.pack(expand=True, fill='both', pady=10)

        # List of influencers
        self.influencer_widgets = []
        for influencer in self.influencers:
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
            self.manager.add_influencer(influencer_name)  # Add the influencer to the manager
            self.update_widgets()  # Update the widgets to reflect the changes
        else:
            # You may want to display a message or handle empty input differently
            print("Please enter a valid influencer name.")

    def remove_influencer(self, influencer):
        self.manager.remove_influencer(influencer)
        self.update_widgets()

    def update_widgets(self):

        # Clear the influencers frame
        for widget_tuple in self.influencer_widgets:
            widget_tuple[0].destroy()

        # Recreate the widgets for each updated influencer
        self.influencer_widgets.clear()
        for influencer in self.influencers:
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
        



if __name__ == "__main__":
    app = InfluencersPage()
    app.root.mainloop()
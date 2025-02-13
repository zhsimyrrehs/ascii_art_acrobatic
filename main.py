import customtkinter as ctk
from art import text2art

# App Configuration
ctk.set_appearance_mode("light")

class AsciiArtApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Color Palette
        self.bg_color = "#eaf6f6"  
        self.card_color = "#ffffff"  
        self.button_color = "#397c7c"  
        self.button_hover = "#2f6565"  
        self.footer_color = "#2f6565"
        self.text_color = "#333333"  # Darker for better contrast

        # Window Configuration
        self.title("Acrobatic ASCII Art Generator")
        self.geometry("900x700")  # Increased window size
        self.minsize(700, 500)
        self.configure(fg_color=self.bg_color)

        # Grid Configuration
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Header
        self.header = ctk.CTkLabel(
            self, 
            text="Acrobatic ASCII Art Generator", 
            font=("Courier", 28, "bold"),  # Monospaced font for better alignment
            text_color=self.text_color
        )
        self.header.grid(row=0, column=0, pady=20)

        # Input Area
        self.input_field = ctk.CTkEntry(
            self,
            placeholder_text="Type your text here...",
            width=500,
            height=40,
            fg_color=self.card_color,
            text_color=self.text_color,
            border_width=2,
            corner_radius=10
        )
        self.input_field.grid(row=1, column=0, pady=10)
        self.input_field.bind("<KeyRelease>", self.generate_ascii)  # Event Binding

        # # Generate Button
        # self.generate_button = ctk.CTkButton(
        #     self,
        #     text="Generate ASCII Art",
        #     fg_color=self.button_color,
        #     hover_color=self.button_hover,
        #     text_color="white",
        #     command=self.generate_ascii,
        #     height=40,
        #     width=200
        # )
        # self.generate_button.grid(row=2, column=0, pady=10)

        # Output Area (Bigger and Monospaced Font)
        self.output_area = ctk.CTkTextbox(
            self,
            width=1000,  # Increased width
            height=800,  # Increased height
            fg_color=self.card_color,
            text_color=self.text_color,
            corner_radius=10,
            font=("Courier", 14)  # Monospaced for cleaner ASCII display
        )
        self.output_area.grid(row=3, column=0, pady=20)
        self.output_area.configure(state="disabled")

        # Footer with GWiST Branding
        self.footer = ctk.CTkLabel(
            self,
            text="GWiST",
            font=("Helvetica", 14, "italic"),
            text_color="white",
            fg_color=self.footer_color,
            height=30,
            corner_radius=0
        )
        self.footer.grid(row=4, column=0, sticky="we")

    def generate_ascii(self, event=None):
        user_input = self.input_field.get()
        if user_input.strip():  # Check for non-empty input
            ascii_art = text2art(user_input, font="acrobatic")
        else:
            ascii_art = ""  # Clear output if input is empty
        self.output_area.configure(state="normal")
        self.output_area.delete("1.0", "end")
        self.output_area.insert("1.0", ascii_art)
        self.output_area.configure(state="disabled")

if __name__ == "__main__":
    app = AsciiArtApp()
    app.mainloop()

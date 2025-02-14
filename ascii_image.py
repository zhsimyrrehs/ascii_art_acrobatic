import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageEnhance, ImageOps, ImageFilter, ImageStat

# Optimized ASCII character set, ordered from darkest to lightest
ASCII_CHARS = "@%#*+=-:. "

class AsciiArtApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Ultra-Detailed ASCII Art Generator")
        self.geometry("1400x900")  # Bigger window for more visibility
        
        # Create widgets
        self.header = ctk.CTkLabel(self, text="High-Detail ASCII Art Generator", font=("Courier", 24))
        self.header.pack(pady=10)

        # Control panel frame
        self.control_frame = ctk.CTkFrame(self)
        self.control_frame.pack(pady=5, padx=10, fill="x")

        # Width control
        self.width_label = ctk.CTkLabel(self.control_frame, text="Width:")
        self.width_label.pack(side="left", padx=5)
        self.width_var = tk.StringVar(value="250")  # Increased default width for more detail
        self.width_entry = ctk.CTkEntry(self.control_frame, width=60, textvariable=self.width_var)
        self.width_entry.pack(side="left", padx=5)

        # Upload button
        self.upload_button = ctk.CTkButton(self.control_frame, text="Upload Image", command=self.convert_image)
        self.upload_button.pack(side="left", padx=20)

        # Output area with monospace font for precise character alignment
        self.output_area = ctk.CTkTextbox(self, width=100, height=40, font=("Courier New", 6))
        self.output_area.pack(pady=10, padx=20, fill="both", expand=True)
    
    def convert_image(self):
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
            )
            if not file_path:
                return

            # Get width from UI
            new_width = int(self.width_var.get())

            with Image.open(file_path) as img:
                # Convert to grayscale
                img = img.convert('L')

                # Apply auto-contrast to balance brightness
                img = ImageOps.autocontrast(img)

                # Dynamically adjust contrast based on image brightness
                stat = ImageStat.Stat(img)
                mean_brightness = stat.mean[0] / 255
                contrast_factor = 1.5 + (0.7 * (0.5 - mean_brightness))
                enhancer = ImageEnhance.Contrast(img)
                img = enhancer.enhance(contrast_factor)

                # Apply sharpening & edge enhancement to highlight facial details
                img = img.filter(ImageFilter.SHARPEN).filter(ImageFilter.EDGE_ENHANCE_MORE)

                # Compute new dimensions while maintaining aspect ratio
                width, height = img.size
                aspect_ratio = height / width
                new_height = int(aspect_ratio * new_width * 0.55)  # Adjusted for better accuracy
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                # Convert to ASCII
                pixels = list(img.getdata())
                ascii_str = []
                for y in range(new_height):
                    line = []
                    for x in range(new_width):
                        pixel_value = pixels[y * new_width + x]
                        # Map pixel value to ASCII character
                        char_idx = int((pixel_value * (len(ASCII_CHARS) - 1)) / 255)
                        line.append(ASCII_CHARS[char_idx])
                    ascii_str.append(''.join(line))

                # Display result
                self.output_area.delete('1.0', tk.END)
                self.output_area.insert('1.0', '\n'.join(ascii_str))

        except Exception as e:
            self.output_area.delete('1.0', tk.END)
            self.output_area.insert('1.0', f"Error: {str(e)}")

if __name__ == "__main__":
    app = AsciiArtApp()
    app.mainloop()

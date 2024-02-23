import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Image Popup")

# Load the image
image_path = "path_to_your_image.jpg"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Display the image in a label
label = tk.Label(root, image=photo)
label.pack()

# Function to close the popup
def close_popup():
    root.destroy()

# Button to close the popup
close_button = tk.Button(root, text="Close", command=close_popup)
close_button.pack()

# Run the main event loop
root.mainloop()

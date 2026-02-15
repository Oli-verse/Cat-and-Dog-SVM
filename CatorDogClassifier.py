from flask import Flask, render_template, request, redirect, url_for, jsonify
import customtkinter as ctk
from PIL import Image, ImageTk
from myclassifier import detect_pet

# Initialize the main window
ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("green") 

window = ctk.CTk()
window.geometry("600x700")
window.title("Cat or Dog Classifier")

window.configure(foreground_color="#90ee90")

border_frame = ctk.CTkFrame(window, width=410, height=210, corner_radius=20, fg_color="#660735")  
border_frame.place(x=95, y=15)

# Inner Frame (Content)
header_frame = ctk.CTkFrame(border_frame, width=400, height=200, corner_radius=15, fg_color="#d3d3d3")
header_frame.place(x=5, y=5)  # Positioned with a margin inside the border
# Header Label
label = ctk.CTkLabel(window, text="Cat or Dog Classifier", font=('Helvetica', 32,'bold'), bg_color="#d3d3d3", text_color="black")
label.place(x=310, y=50, anchor="center")

# Cat and Dog Images
cat_image = Image.open("melvin.png").resize((120, 120))
cat_photo = ctk.CTkImage(cat_image, size=(120, 120)) 
ctk.CTkLabel(window, image=cat_photo, text= "").place(x=150, y=80)

dog_image = Image.open("cheeems.png").resize((120, 120))
dog_photo = ctk.CTkImage(dog_image, size=(120, 120)) 
ctk.CTkLabel(window, image=dog_photo, text = "",bg_color="#d3d3d3").place(x=350, y=80)


# Labels for results
image_preview_label = ctk.CTkLabel(window, text="")
image_preview_label.place(x=160, y=320)

accuracy_label = ctk.CTkLabel(window, text="", font=('Helvetica', 24))
accuracy_label.place(x=300, y=640, anchor="center")

prediction_label = ctk.CTkLabel(window, text="", font=('Helvetica', 24))
prediction_label.place(x=300, y=670, anchor="center")

# Detect Button Function
def on_detect_click():
    try:
        prediction_image, accuracy, prediction = detect_pet()

        img = Image.fromarray(prediction_image)
        img = img.resize((280, 280))
        img_tk = ctk.CTkImage(img, size=(280, 280))  # Convert to CTkImage
        image_preview_label.configure(image=img_tk)
        image_preview_label.image = img_tk
        

        accuracy_label.configure(text=f"Accuracy: {accuracy:.2%}")
        prediction_label.configure(text=f"Prediction: {prediction}")
    except Exception as e:
        prediction_label.configure(text=f"Error: {e}")

# Detect Button
detect_button = ctk.CTkButton(window, text="Detect", font=('Helvetica', 16), command=on_detect_click, fg_color = "#b51fae")
detect_button.place(x=240, y=260)

# Run the main GUI loop
window.mainloop()

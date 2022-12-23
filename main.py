import os
import cv2
import tkinter as tk
from tkinter import filedialog
import tkinter as ttk
import PIL
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("Face Detection and Cropping")

# Create the thumbnail label
thumbnail_label = tk.Label(window)

# Place the thumbnail label in the GUI
thumbnail_label.pack()


# Function to select the input folder
def select_input_folder():
    global input_folder
    input_folder = filedialog.askdirectory()


# Function to select the output folder
def select_output_folder():
    global output_folder
    output_folder = filedialog.askdirectory()


def detect_and_crop_faces():
    # Load the cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    # Get the list of images in the input folder
    images = os.listdir(input_folder)

    # Update the progress bar value
    # progress_bar.set((i + 1) / len(images) * 100)

    # Loop through the images
    for i, image in enumerate(images):

        # Update the progress bar value
        progress_bar.set((i + 1) / len(images) * 100)
        progress_bar.update()

        # Read the image
        img = cv2.imread(os.path.join(input_folder, image))

        # Skip the image if it is invalid
        if img is None:
            continue

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        # Loop through the detected faces
        for (x, y, w, h) in faces:
            # Calculate the size of the face bounding box and the size of the square to be cropped
            size = min(w, h)

            # Calculate the top-left corner of the square to be cropped
            x = x + (w - size) // 2
            y = y + (h - size) // 2

            # Crop the face from the image
            face = img[y:y + size, x:x + size]
            face = cv2.resize(face, (512, 512))
            # Save the cropped face to the output folder
            cv2.imwrite(os.path.join(output_folder, image), face)

            # Try to display the thumbnail of the image
            #try:
                # Open the image file
                #img = Image.open(os.path.join(input_folder, image))

                # Resize the image to a thumbnail
                #img = img.resize((128, 228))

                # Convert the image to a PhotoImage object
                #img = ImageTk.PhotoImage(img)

                # Display the thumbnail in the thumbnail label
                #thumbnail_label.configure(image=img)
            #except IOError as e:
                # If there is an error opening the image file, print an error message
                #print("Error opening image file:", e)
            #except ValueError as e:
                # If there is an error converting the image to a PhotoImage object, print an error message
                #print("Error converting image to PhotoImage object:", e)


# Create the input folder button
input_button = tk.Button(window, text="Select Input Folder", command=select_input_folder)
input_button.pack()

# Create the output folder button
output_button = tk.Button(window, text="Select Output Folder", command=select_output_folder)
output_button.pack()

# Create the detect and crop button
detect_button = tk.Button(window, text="Detect and Crop Faces", command=detect_and_crop_faces)
detect_button.pack()

# Create the progress bar
progress_bar = tk.Scale(window, from_=0, to=100, orient="horizontal", length=200)
progress_bar.pack()

# Run the main loop
window.mainloop()

import cv2
import tkinter as tk
from tkinter import Label, StringVar, OptionMenu
from PIL import Image, ImageTk
import threading
import time

# Initialize camera
cap = None
out = None
is_recording = False
start_time = 0

# Available resolutions
RESOLUTIONS = {
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "480p": (640, 480)
}
selected_resolution = "720p"

# Create GUI window
root = tk.Tk()
root.title("Video Recorder")

# Video display area
video_frame = tk.Frame(root)
video_frame.pack(pady=10)
label = Label(video_frame)
label.pack()

# Button text control
btn_text = StringVar()
btn_text.set("Start Recording")

# Recording timer
timer_text = StringVar()
timer_text.set("Recording Time: 00:00")

def change_resolution(res):
    """Change camera resolution"""
    global cap, selected_resolution
    selected_resolution = res
    if cap:
        cap.set(3, RESOLUTIONS[res][0])  # Width
        cap.set(4, RESOLUTIONS[res][1])  # Height

def toggle_recording():
    """Start or stop recording"""
    global is_recording, out, start_time
    is_recording = not is_recording

    if is_recording:
        btn_text.set("Stop Recording")
        start_time = time.time()
        width, height = RESOLUTIONS[selected_resolution]
        fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Use XVID for better compatibility
        out = cv2.VideoWriter('output.avi', fourcc, 30.0, (width, height))  # Save as .avi
        update_timer()
    else:
        btn_text.set("Start Recording")
        if out:
            out.release()
            out = None

def update_timer():
    """Update the recording timer"""
    if is_recording:
        elapsed_time = int(time.time() - start_time)
        mins, secs = divmod(elapsed_time, 60)
        timer_text.set(f"Recording Time: {mins:02d}:{secs:02d}")
        root.after(1000, update_timer)

def close_program():
    """Stops recording and closes the program"""
    global is_recording, out, cap
    is_recording = False
    if out:
        out.release()
    if cap:
        cap.release()
    root.destroy()

def show_frame():
    """Capture video frame and update in Tkinter window"""
    global cap
    if cap is None:
        cap = cv2.VideoCapture(0)
        change_resolution(selected_resolution)

    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 1)  # Flip for natural view

        if is_recording and out:
            out.write(frame)  # Save frame to video

        # Convert frame for Tkinter display
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        label.imgtk = imgtk
        label.configure(image=imgtk)

    # Keep updating
    label.after(10, show_frame)

# Resolution selection
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

res_label = Label(control_frame, text="Select Resolution:", font=("Arial", 12))
res_label.grid(row=0, column=0, padx=5)

res_dropdown = OptionMenu(control_frame, StringVar(value=selected_resolution), *RESOLUTIONS.keys(), command=change_resolution)
res_dropdown.grid(row=0, column=1, padx=5)

# Timer label
timer_label = Label(control_frame, textvariable=timer_text, font=("Arial", 14))
timer_label.grid(row=0, column=2, padx=10)

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

btn_record = tk.Button(btn_frame, textvariable=btn_text, command=toggle_recording, font=("Arial", 14), bg="lightblue", width=15)
btn_record.grid(row=0, column=0, padx=10)

btn_exit = tk.Button(btn_frame, text="Exit", command=close_program, font=("Arial", 14), bg="red", fg="white", width=10)
btn_exit.grid(row=0, column=1, padx=10)

# Start video stream in Tkinter
show_frame()
root.mainloop()

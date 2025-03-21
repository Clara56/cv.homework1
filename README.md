# cv.homework1
My simple video recorder using OpenCV(python)

# Video Recorder using OpenCV and Tkinter

This is a simple video recorder application built using OpenCV and Tkinter. It allows users to record videos with different resolutions and saves the recorded video as an `.avi` file.

## Features
- Live video preview
- Start/stop video recording
- Resolution selection (720p, 1080p, 480p)
- Recording timer display
- Saves recorded videos in `.avi` format
- Simple GUI using Tkinter
- Supports external cameras, including iPhone cameras when running on Mac

## Requirements
Make sure you have the following dependencies installed before running the program:

```sh
pip install opencv-python
pip install opencv-python-headless
pip install pillow
```

## How to Use
1. Run the script using Python:
   ```sh
   python video_recorder.py
   ```
2. The GUI window will appear with the live video feed.
3. Select the desired resolution from the dropdown menu.
4. Click the **Start Recording** button to begin recording.
5. The recording timer will update in real-time.
6. Click the **Stop Recording** button to stop and save the recording.
7. Click the **Exit** button to close the application.

## File Output
- The recorded video is saved as `output.avi` in the same directory as the script.
- The video format used is `.avi` with the `XVID` codec.

## Camera Compatibility
- The application uses the default webcam by default.
- If you are using a Mac, you may be able to connect and use your iPhone camera as the video source.

## Testing 

<img width="1440" alt="Screenshot 2025-03-18 at 11 37 23" src="https://github.com/user-attachments/assets/43d90d32-1450-4242-811f-83deda6241f6" />

## Code Overview
- Uses OpenCV (`cv2`) for video capturing and processing.
- Uses Tkinter for the graphical user interface.
- Utilizes `PIL` (Pillow) for displaying frames in the Tkinter window.
- Captures frames from the webcam and writes them to an output file during recording.



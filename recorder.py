# importing the required packages
import pyautogui
import cv2
import numpy as np
import json
import time
import threading



#open settings json
jOpen = open("config.json")

settings = json.load(jOpen)
vidDimSplit = settings["resolution"].split("*")
# Specify resolution
resolution = ((int(vidDimSplit[0]), int(vidDimSplit[1])))
# Specify video codec
codec = cv2.VideoWriter_fourcc(*"mp4v")

# Specify name of Output file
filename = settings["fileName"] 
print(filename)

# Specify frames rate. We can choose any
# value and experiment with it
fps = int(settings["frameRate"])
print(fps)

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)

# Resize this window
cv2.resizeWindow("Live", 1280, 720)
while True:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write it to the output file
    out.write(frame)

    # Optional: Display the recording screen
    cv2.imshow('Live', frame)
    # Stop recording when we press 'q'
    if cv2.waitKey(10) == ord('q'):
        break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()


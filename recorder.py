# importing the required packages
import cv2
import numpy as np
import json
import time
import threading

import mss

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

# Specify frames rate. We can choose any
# value and experiment with it
fps = int(settings["frameRate"])

# Creating a VideoWriter object
out = cv2.VideoWriter(filename, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
# Resize this window
cv2.resizeWindow("Live", 480, 240)
while True:
    # Take screenshot using PyAutoGUI
    with mss.mss() as mss_instance:  # Create a new mss.mss instance
        monitor_1 = mss_instance.monitors[1]  # Identify the display to capture

   #100ms so capp    # Convert the screenshot to a numpy array
        img = mss_instance.grab(monitor_1)  # Take the screenshot
        frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to
    # RGB(Red, Green, Blue)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)

    # Write it to the output file
        out.write(frame)

    # Optional: Display the recording screen
    #cv2.imshow('Live', frame)
    # Stop recording when we press 'q'
    if cv2.waitKey(10) == ord('q'):
        break

# Release the Video writer
out.release()

# Destroy all windows
cv2.destroyAllWindows()


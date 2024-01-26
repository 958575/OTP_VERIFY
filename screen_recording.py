import cv2
import pyautogui
import numpy as np
#cv2 packages(open cv) ,pyautogui for recording our screen.
#numpy packages for numerical type packages .
# Screen resolution.
screen_width, screen_height = pyautogui.size()

# Set the codec and create VideoWriter object.
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("screen_recording.avi", fourcc, 20.0, (screen_width, screen_height))

try:
    while True:
        # Capture the screen.
        screenshot = pyautogui.screenshot()
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Write the frame to the output video.
        output.write(frame)

except KeyboardInterrupt:
    # Release the VideoWriter object on keyboard interrupt.
    output.release()

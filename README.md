How It Works
The system uses MediaPipe's hand tracking capabilities to detect your hand in real-time through your webcam. It identifies specific finger positions and translates them into game commands:

Index finger up (✌️): Jump (triggers UP key)

Thumb and index finger up (👍✌️): Roll (triggers DOWN key)

Index and middle fingers up (✌️🖕): Move Right (triggers RIGHT key)

Thumb only up (👍): Move Left (triggers LEFT key)

All fingers up (🖐️): Activate Hoverboard (triggers SPACE key)

Technical Details
The project consists of two main Python files:

Gesture_Recognition.py: Contains the handDetector class that handles:

Hand detection and tracking using MediaPipe

Landmark identification for finger positions

Finger state detection (up or down)

Hand type identification (left or right)

Subway.py: The main application that:

Captures webcam input

Processes hand gestures using the handDetector

Translates gestures into keyboard commands using PyAutoGUI

Displays real-time feedback with an overlay showing the detected gesture

Requirements
Python 3.11 (MediaPipe is not yet compatible with Python 3.13)

OpenCV (cv2)

MediaPipe

PyAutoGUI

A webcam

Usage
Start Subway Surfers on your device

Run the Python script: py -3.11 Subway.py

Position your hand in front of the webcam

Make the appropriate gestures to control the game

Press 'Q' to quit the application

The application includes a cooldown mechanism to prevent rapid-fire commands, making the gameplay smoother and more responsive.

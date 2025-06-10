import cv2
import mediapipe as mp
import time
import pyautogui
import numpy as np

def detectGesture(fingers):
    """
    Returns a string and triggers a keypress based on the finger pattern.
    Also provides visual feedback through PyAutoGUI.
    """
    # Define gesture mappings with more descriptive names
    gesture_map = {
        (0, 1, 0, 0, 0): {"name": "Jump", "key": "up", "description": "Index finger up"},
        (1, 1, 0, 0, 0): {"name": "Roll", "key": "down", "description": "Thumb & Index up"},
        (0, 1, 1, 0, 0): {"name": "Move Right", "key": "right", "description": "Index & Middle up"},
        (1, 0, 0, 0, 0): {"name": "Move Left", "key": "left", "description": "Thumb up"},
        (1, 1, 1, 1, 1): {"name": "Hoverboard", "key": "space", "description": "All fingers up"}
    }
    
    # Convert fingers list to tuple for dictionary lookup
    finger_tuple = tuple(fingers)
    
    # Check if the gesture exists in our mapping
    if finger_tuple in gesture_map:
        gesture_info = gesture_map[finger_tuple]
        pyautogui.press(gesture_info["key"])
        return gesture_info["name"]
    else:
        return "No Action"

def main():
    pTime = 0
    cap = cv2.VideoCapture(0)  # Use 0 for default webcam
    from Gesture_Recognition import handDetector
    detector = handDetector()
    gesture = "No Action"
    lastGestureTime = 0  # To track time between gestures
    gestureCooldown = 0.5  # Cooldown in seconds
    
    # Set camera properties for better quality if supported
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    
    # Create window with custom properties
    cv2.namedWindow("Gesture Control - Subway Surfers", cv2.WINDOW_NORMAL)

    if not cap.isOpened():
        print("❌ Cannot open webcam")
        return

    while True:
        success, img = cap.read()
        if not success or img is None:
            print("❌ Failed to grab frame")
            continue

        img = detector.findHands(img)
        lmList = detector.findPosition(img)

        currentTime = time.time()
        if len(lmList) != 0 and (currentTime - lastGestureTime) > gestureCooldown:
            try:
                fingers = detector.fingersUp()
                gesture = detectGesture(fingers)
                print("Gesture:", gesture)
                lastGestureTime = currentTime  # Reset cooldown
            except Exception as e:
                print("⚠️ Error in gesture detection:", e)
                gesture = "Error"
        # Create a stylish UI overlay
        h, w, c = img.shape
        overlay = img.copy()
        
        # Create gradient background for UI elements
        gradient = np.zeros((140, 320, 3), dtype=np.uint8)
        for i in range(140):
            gradient[i, :] = (40 + i//2, 0, 80 - i//3)
        
        # Add rounded rectangle for gesture display
        cv2.rectangle(gradient, (10, 10), (310, 70), (60, 20, 120), -1)
        cv2.rectangle(gradient, (10, 10), (310, 70), (120, 40, 180), 2)
        
        # Add game controls info box
        cv2.rectangle(gradient, (10, 80), (310, 130), (30, 10, 70), -1)
        cv2.rectangle(gradient, (10, 80), (310, 130), (80, 30, 140), 2)
        
        # Add gradient overlay to bottom left of frame
        roi = img[h-140:h, 0:320]
        cv2.addWeighted(gradient, 0.7, roi, 0.3, 0, roi)
        img[h-140:h, 0:320] = roi
        
        # Add gesture icon based on detected gesture
        icon_position = (w-80, 80)
        icon_size = 60
        icon_color = (0, 255, 255)
        if gesture == "Jump":
            cv2.arrowedLine(img, (icon_position[0], icon_position[1]+icon_size), 
                           (icon_position[0], icon_position[1]), icon_color, 3, tipLength=0.3)
        elif gesture == "Roll":
            cv2.arrowedLine(img, (icon_position[0], icon_position[1]), 
                           (icon_position[0], icon_position[1]+icon_size), icon_color, 3, tipLength=0.3)
        elif gesture == "Move Right":
            cv2.arrowedLine(img, (icon_position[0], icon_position[1]+icon_size//2), 
                           (icon_position[0]+icon_size, icon_position[1]+icon_size//2), icon_color, 3, tipLength=0.3)
        elif gesture == "Move Left":
            cv2.arrowedLine(img, (icon_position[0]+icon_size, icon_position[1]+icon_size//2), 
                           (icon_position[0], icon_position[1]+icon_size//2), icon_color, 3, tipLength=0.3)
        elif gesture == "Hoverboard":
            cv2.circle(img, (icon_position[0]+icon_size//2, icon_position[1]+icon_size//2), 
                      icon_size//2, icon_color, 2)
            cv2.line(img, (icon_position[0]+20, icon_position[1]+icon_size//2), 
                    (icon_position[0]+icon_size-20, icon_position[1]+icon_size//2), icon_color, 2)
        
        # Add stylish text with glow effect
        gesture_text = f'GESTURE: {gesture.upper()}'
        # Text glow/shadow
        cv2.putText(img, gesture_text, (w-315, h-95), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 4, cv2.LINE_AA)
        # Main text
        cv2.putText(img, gesture_text, (w-315, h-95), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2, cv2.LINE_AA)
        
        # Controls text
        cv2.putText(img, "PRESS 'Q' TO QUIT", (w-315, h-55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Add FPS counter
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f"FPS: {int(fps)}", (w-100, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Add title bar
        title_bar = np.zeros((50, img.shape[1], 3), dtype=np.uint8)
        for i in range(title_bar.shape[1]):
            title_bar[:, i] = (40 + i % 50, 0, 100 - i % 30)
            
        cv2.putText(title_bar, "SUBWAY SURFERS GESTURE CONTROL", (img.shape[1]//2 - 230, 35), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Combine title bar with main image
        display = np.vstack((title_bar, img))
        
        # Show the final image
        cv2.imshow("Gesture Control - Subway Surfers", display)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



if __name__ == '__main__':
    main()

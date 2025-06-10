# 🎮 Gesture-Controlled Subway Surfers

![Subway Surfers](https://img.shields.io/badge/Game-Subway%20Surfers-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.x-red?style=for-the-badge)

Play Subway Surfers using just your hand gestures! This application uses computer vision to detect your hand movements and translates them into game controls in real-time.

## ✨ Features

- **Real-time hand tracking** with MediaPipe
- **Intuitive gesture controls** for game actions
- **Visual feedback** with on-screen indicators
- **Smooth performance** with gesture cooldown system
- **Stylish UI** with gesture visualization

## 🖐️ Gesture Controls

| Gesture | Action | Game Control |
|---------|--------|--------------|
| ☝️ Index finger up | Jump | UP key |
| 👍☝️ Thumb & Index up | Roll | DOWN key |
| ✌️ Index & Middle up | Move Right | RIGHT key |
| 👍 Thumb up | Move Left | LEFT key |
| 🖐️ All fingers up | Hoverboard | SPACE key |

## 🛠️ Requirements

- Python 3.11
- OpenCV
- MediaPipe
- PyAutoGUI
- Webcam

## 📋 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/Gesture-Controlled-Subway-Surfers.git
cd Gesture-Controlled-Subway-Surfers

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage

1. Start Subway Surfers on your device
2. Run the Python script:
   ```bash
   python -3.11 Subway.py
   ```
3. Position your hand in front of the webcam
4. Make gestures to control the game
5. Press 'Q' to quit

## 📷 Screenshots

[Add screenshots of your application here]

## 🧠 How It Works

The system uses MediaPipe's hand tracking to detect 21 landmarks on your hand. Based on the positions of these landmarks, the application determines which fingers are up or down. Each gesture pattern is mapped to a specific game control, which is then triggered using PyAutoGUI.

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
# 📸 RiddleCam: The Interactive Object-Guessing Game

Welcome to RiddleCam! This fun and interactive game challenges you to solve riddles and then prove your answer by showing the object to your webcam. Using the power of real-time object detection with YOLOv8, RiddleCam brings a classic guessing game into the modern world.

---

## 🎮 How It Works

The game flow is simple but engaging:

1.  **Get a Riddle**: The game presents you with a random riddle from its collection.
2.  **Make a Guess**: You type your answer into the terminal. If you're wrong, you can try again!
3.  **Show the Object**: Once you guess correctly, the real challenge begins! Your webcam will activate.
4.  **Prove It!**: You must find the physical object and show it to the camera.
5.  **Win the Round**: The YOLOv8 model will scan the video feed. If it detects the correct object, you win the round and move on to the next riddle!

---

## ✨ Features

* **Interactive CLI**: A simple and clean command-line interface to guide you through the game.
* **Real-Time Object Detection**: Uses your webcam and the powerful **YOLOv8** model to identify objects in real-time.
* **Fun Riddles**: A diverse collection of riddles to keep you guessing.
* **Engaging Gameplay**: Combines brainpower with a scavenger hunt-like experience.

---

## 🛠️ Setup & Installation

To get started, you'll need Python and a few libraries. A webcam is also required to play the game.

1.  **Clone the repository** (or download the script).

2.  **Install the required Python libraries**:
    Open your terminal and run the following command to install `ultralytics` (which includes PyTorch) and `OpenCV`.

    ```bash
    pip install ultralytics opencv-python
    ```

---

## 🚀 How to Run

1.  Navigate to the project directory in your terminal.
2.  Run the script with Python:

    ```bash
    python riddlecam.py 
    ```
    *(Assuming you name the file `riddlecam.py`)*

3.  Follow the on-screen instructions, solve the riddles, and have fun!
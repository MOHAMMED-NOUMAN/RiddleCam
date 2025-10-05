# 🧩 RiddleCam

**RiddleCam** is an interactive computer vision game built with **Python** and **YOLOv8** that challenges you with riddles — and asks you to prove your answer using your webcam!
It combines fun logic puzzles with real-time object detection using **OpenCV** and **Ultralytics YOLO**.

---

## 🎮 How It Works

1. The program asks you a random riddle (e.g. *“I have keys but open no doors. What am I?”*).
2. You type your guess in the terminal.
3. If your guess is correct, the camera opens — now you must **show the object** in front of your webcam.
4. The YOLOv8 model detects if the correct object appears in the frame.
5. If found, you win that round! If not, try another riddle.

---

## 🧠 Example Gameplay

```
--- Welcome to RiddleCam! ---
I will ask you a riddle. Guess the object, then show it to the camera!
Type 'quit' at any time to exit.

==============================
Here is your riddle:
> I have keys but open no doors. I have space but no room. What am I?
What is your guess? > keyboard

CORRECT! The answer is 'keyboard'.
Now, prove it! Show the object to the camera.
```

The webcam window opens, and if YOLO detects a **keyboard**, you’ll see:

```
I see a keyboard! Well done!
```

---

## ⚙️ Requirements

Make sure you have the following installed:

* **Python 3.8+**
* **pip** (Python package manager)
* A working **webcam**

### 🧩 Install Dependencies

Run this command in your terminal:

```bash
pip install ultralytics opencv-python
```

> 💡 *If `ultralytics` doesn’t install YOLOv8 properly, try updating pip first:*

```bash
pip install --upgrade pip
```

---

## 🚀 How to Run

1. Clone or download this repository.
2. Open your terminal in the project folder.
3. Run the script:

   ```bash
   python riddlecam.py
   ```
4. Follow the on-screen instructions and enjoy the game!

---

## 🧰 How It Works (Under the Hood)

* The **YOLOv8n** model (`yolov8n.pt`) is loaded using the Ultralytics library.
* Each round has three states:

  1. **ASK_RIDDLE** – A random riddle is chosen.
  2. **WAITING_FOR_GUESS** – The player types an answer.
  3. **DETECTING_OBJECT** – The camera opens, and YOLO searches for the correct object.
* If the YOLO model detects the correct object class (like “keyboard”, “tv”, or “bottle”), it displays a success message.

---

## 🧩 Supported Riddles

| Riddle                                                               | Answer   |
| -------------------------------------------------------------------- | -------- |
| I have a screen but no face. I bring the world to your living space. | tv       |
| I have keys but open no doors. I have space but no room.             | keyboard |
| I have a neck but no head, and I wear a cap.                         | bottle   |
| I have ribs but no spine. I’m your best friend when it rains.        | umbrella |
| I’m a fruit that’s long and yellow. Monkeys think I’m a fine fellow. | banana   |

---

## 🪄 Tips

* Make sure your webcam has a clear view of the object.
* Good lighting helps YOLO detect objects more accurately.
* You can add more riddles and answers by updating the `riddles` dictionary in the code.

---

## 🧑‍💻 Author

**Mohammed Nouman**
Made with ❤️ using Python, OpenCV, and YOLOv8.

---

## 🐍 License

This project is open-source and free to use for educational or personal projects.

---



# 7301-PetCasso
Orbital25 project

MyMelody is an interactive, animated desktop companion built with Python and PyQt5. It walks, idles, and reacts to screen boundaries in real time — bringing your workspace to life!

# ✨Interactive Features

- 🧭 **Real-Time Movement**: Walks left or right and flips direction when hitting screen edges.
- 🖼 **Dynamic Animations**: Easily extend behaviors by adding PNG sequences into folders.
- 🖱 **Context Menu Controls**: Right-click the pet to switch between Idle, Walk, and Sleep modes.
- 👻 **Transparent & Frameless**: Always-on-top window with a clean transparent background.
- 🪄 **Modular Design**: New actions (e.g. cleaning, feeding) can be added with ease.
- 🧹 **Upcoming Features**: Feeding, cleaning, magic tricks, and a customizable room page!

---

## 📁 Project Structure
Deskpet/
├── main.py # Main application script
├── Deskpet/ # Animation assets and folders
│ ├── walk/
│ │ ├── left/
│ │ └── right/
│ ├── nothing/
│ └── sleep/
├── icon.ico # App icon


---

## 🧑‍💻 How It Works

- **UI Setup**: Built using `QLabel` with `FramelessWindowHint` and `WA_TranslucentBackground` for transparency.
- **Animation**: Loads image sequences with `QPixmap` and cycles them using a `QTimer`.
- **Movement Logic**: Moves across the screen using direction variables and adjusts when hitting edges.
- **Interactivity**: Right-click to control modes via a `QMenu`.

---

## ✅ Requirements

- Python 3.7+
- PyQt5
- Pygame (later use for magic tricks)

Install dependencies:

```bash
pip install PyQt5
```

---
## 🧠 Credits
Made with ❤️ by Siyu and Nayoung



# 🐾 PetCasso: Interactive Digital Pet Companion

**PetCasso** is a lightweight digital pet for your desktop, inspired by classic virtual pet toys like Tamagotchi. The pet offers companionship and interaction through simple animations and menus, providing a moment of relaxation and stress relief during busy days.

---

## 🌟 Features in Milestone 1

- **Interactive Animations**:
  - Idle (default), Sleeping, Walking
  - Right-click context menu to trigger actions (sleep, walk, idle, etc.)
  - Stop/start animations and movement

- **Backend Logic**:
  - Core PyQt5 implementation for pet display and animations
  - Modular code design for future expansion

---

## 📚 Project Motivation

In today's fast-paced environment, people often feel overwhelmed with studies, work, and loneliness. As students ourselves, we understand the difficulties and stress people face with busy lifestyles. Inspired by our personal experiences and classic virtual pets, we created **PetCasso** to bring a simple, enjoyable companion to your desktop.

---

## 🏗 Technical Overview

- **Frontend**: Python (PyQt5)
- **Animation Management**: `QTimer` for smooth animations
- **Event Handling**: PyQt5 context menus for interactive controls

### 📁 File Structure
PetCasso/

├── MyMelody.py # Main pet logic with interactive animations

├── Deskpet/ # Animation image assets (idle, walk, sleep, etc.)

├── images/ # (Optional for future room customization)

├── layout.json # (Placeholder for room layout)

├── venv/ # Virtual environment (excluded from Git)

---

## 🛠 Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YourUsername/PetCasso.git
cd PetCasso
```
### 2️⃣ Create & activate virtual environment

#### macOS/Linux
python3 -m venv venv
source venv/bin/activate

#### Windows
python -m venv venv
.\venv\Scripts\activate

### 3️⃣ Install dependencies
pip install PyQt5

### 4️⃣ Run the application
python MyMelody.py

## 📝 User Stories
- As a student, I want to relax and destress by watching my digital pet perform animations.
- As a casual user, I want a simple, stress-relieving interaction with a virtual pet on my desktop.
- As a tech enthusiast, I want to explore how a desktop pet can be programmed with PyQt5.

## 📅 Timeline & Future Plans
- Milestone	Features
  - Milestone 1	Interactive animations (idle, walk, sleep)
  - Milestone 2	Room customization with drag-and-drop furniture
  - Milestone 3	Pet interactions (feeding, cleaning) + effects

## 🔍 Software Engineering Principles
Single Responsibility Principle (SRP): MyMelody class handles pet logic, animation updates, and context menus separately.

Open-Closed Principle (OCP): Designed for easy extension — new animations or features can be added without modifying core classes.

## 🤝 Contributors
Feng Siyu

Kim Nayoung

## 📄 License
For educational use only.

## 🌸 Thank you for using PetCasso!

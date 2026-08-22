# 🪄 MagicMirrorAI

An AI-powered interactive mirror that combines computer vision, hand tracking,
gesture interaction, and real-time visual effects to create an immersive
AR-style experience.

## 🚀 Project Overview

MagicMirrorAI uses a webcam to track hand movements in real time and allows
users to interact with a virtual portal using their fingers.

The project currently supports:

- ✋ Real-time hand tracking
- ☝️ Index-finger controlled portal
- 🤏 Pinch-based portal resizing
- 🪄 Background-based invisibility effect
- 🎨 Multiple visual filters
- 📷 Real-time webcam processing

## 🛠️ Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy
- Computer Vision
- Real-Time Image Processing

## 🏗️ Project Architecture

```text
Webcam
   ↓
Frame Capture
   ↓
Hand Tracking
   ↓
Gesture Detection
   ↓
Virtual Portal
   ↓
Invisibility / Visual Effects
   ↓
Real-Time Display

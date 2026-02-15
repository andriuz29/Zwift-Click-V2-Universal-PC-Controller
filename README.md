# Zwift Click – Universal PC Controller

This Python script allows you to use the **Zwift Click v2** Bluetooth controller as a universal macro pad on Windows or macOS. It bypasses the need for the Zwift Companion app and connects the controller directly to your PC, mapping buttons to keyboard strokes for **Virtual Shifting** and **HUD navigation**.

## Features

* **Auto-Discovery:** Automatically finds and connects to any "Zwift Click" device in pairing mode.
* **Direct Connection:** Uses the native Bluetooth LE stack (no mobile bridge required).
* **Virtual Shifting:** Pre-mapped for standard Zwift virtual shifting keys (`I` and `K`).
* **HUD & Navigation:** Mapped for HUD toggle (`U` key) and standard menu arrows.
* **Software Debouncing:** Built-in logic to prevent accidental multiple shifts from a single physical click.

---

## Prerequisites

### 1. Python Environment
Ensure you have **Python 3.8 or newer** installed. You can download it from [python.org](https://www.python.org/).

### 2. Required Packages
The script requires two main libraries. Install them via terminal or command prompt:

```bash
pip install bleak pyautogui

---

## ⚠️ Legal Disclaimer

**Please read this carefully before using the script:**

1. **Not an Official Product:** This project is a community-driven workaround and is **not** an official product of Zwift, Inc. It has been developed through independent protocol analysis.
2. **Use at Your Own Risk:** By using this script, you acknowledge that you are using an unofficial driver. While it only emulates keyboard presses, the author cannot guarantee that it complies with the latest Zwift Terms of Service.
3. **No Warranty:** This software is provided "as is", without warranty of any kind. The author is not liable for any damages, hardware malfunctions, or account restrictions that may occur.
4. **Trademarks:** All product names, logos, and brands (including "Zwift" and "Zwift Click") are property of their respective owners. 

---

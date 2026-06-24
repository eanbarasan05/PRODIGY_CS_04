# Terminal Key Logger (Educational Project)

## Overview

The **Terminal Key Logger** is a Python-based educational cybersecurity project designed to demonstrate keyboard input handling, event logging, file operations, and session monitoring. Unlike traditional keyloggers, this application operates **only within its own terminal window** and does not monitor or capture keystrokes from other applications, processes, or users.

This project is intended for learning purposes and helps students understand how keyboard events can be processed, logged, and analyzed in a controlled environment.

---

## Features

### Real-Time Key Logging

* Captures keystrokes entered within the application's terminal session.
* Displays live key activity on-screen.

### Timestamped Logs

* Records the exact date and time of each keystroke.
* Maintains a detailed audit trail for analysis.

### Special Key Detection

Recognizes and logs:

* Enter
* Backspace
* Tab
* Escape
* Arrow Keys (Up, Down, Left, Right)

### Session Statistics

Tracks:

* Total keys pressed
* Special keys pressed
* Session runtime

### Automatic Log File Management

* Creates a dedicated logs directory.
* Generates uniquely named log files based on the current timestamp.

### Cross-Platform Support

Compatible with:

* Linux
* Windows
* macOS

---

## Project Structure

```text
Terminal-KeyLogger/
│
├── keylogger.py
│
├── logs/
│   ├── keylog_20260624_120000.txt
│   └── ...
│
└── README.md
```

---

## Requirements

### Python Version

```text
Python 3.8+
```

### External Libraries

No third-party packages are required.

Uses only Python standard libraries:

```python
os
sys
time
datetime
tty
termios
msvcrt
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/eanbarasan05/PRODIGY_CS_04.git keylogger
```

### 2️⃣ Navigate to Project Folder

```bash
cd keylogger
```

### Run the Program

Linux/macOS:

```bash
python3 keylogger.py
```

Windows:

```bash
python keylogger.py
```



### Verify Python Installation

```bash
python3 --version
```

or

```bash
python --version
```

---

## Example Execution

```text
============================================================
 TERMINAL KEY LOGGER (EDUCATIONAL)
============================================================
Log File : logs/keylog_20260624_120000.txt
Press ESC to stop logging.
============================================================

Last Key: a                    Total: 1
Last Key: b                    Total: 2
Last Key: [ENTER]              Total: 3
```

---

## Example Log File

```text
[2026-06-24 12:00:01] a
[2026-06-24 12:00:02] b
[2026-06-24 12:00:03] [ENTER]
[2026-06-24 12:00:04] [UP]
```

---

## Session Summary

When the program exits, a summary report is displayed:

```text
============================================================
SESSION SUMMARY
============================================================
Runtime      : 0:02:35
Total Keys   : 124
Special Keys : 18
Log File     : logs/keylog_20260624_120000.txt
============================================================
```

---

## Educational Objectives

This project demonstrates:

* Keyboard input handling
* Event-driven programming
* File management
* Timestamp generation
* Logging systems
* Terminal-based user interfaces
* Cross-platform Python development

---

## Security & Ethical Considerations

This project is designed solely for educational and authorized testing purposes.

### Important

* The application logs keystrokes only within its own terminal window.
* It does not capture system-wide keyboard activity.
* It does not monitor other applications.
* It does not bypass operating system security controls.
* It should never be modified or used to collect data from users without their explicit consent.

Always follow applicable laws, regulations, and organizational policies when conducting cybersecurity research or testing.

---

## Future Enhancements

Potential improvements include:

* Encrypted log storage
* Password-protected log viewer
* Search and filtering functionality
* Session export (CSV/JSON)
* Real-time analytics dashboard
* User authentication
* Log integrity verification
* Keyboard heatmap generation

---

## 👨‍💻 Author

## ANBARASAN E

### Cyber Security Intern Prodegy Infotech

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

🔐 Secure Passwords • 🛡️ Strong Security • 🚀 Better Protection

</div>

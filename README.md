# Smart AI Facial & Voice Attendance System

SnapClass is an intelligent, automated attendance management application powered by **AI Facial Recognition** and **Voice Biometrics**. Designed for modern educational institutions, SnapClass empowers teachers to log classroom attendance in seconds using multi-face photo scanning or audio verification, while providing students with an effortless Face ID portal and real-time attendance analytics.

---

## ✨ Key Features

### 👨‍🏫 Faculty Portal
- **AI Classroom Photo Scanning**: Snap or upload high-resolution classroom photos to automatically detect, recognize, and mark multiple enrolled students in seconds.
- **Voice Attendance Processing**: Analyze classroom audio clips to match student voice embeddings.
- **Subject & Course Management**: Create subjects, assign course codes, and view total enrolled students and class sessions.
- **Instant QR Code & Link Sharing**: Generate join links and dynamic QR codes using `segno` for quick student self-enrollment.
- **Attendance Records & Export**: View comprehensive attendance logs with present/absent counts and timestamps.

### 🎓 Student Portal
- **Face ID Instant Login**: Log into the portal using real-time facial scanning.
- **Biometric Profile Registration**: Quick onboarding with facial feature extraction and optional voice recording.
- **Course Enrollment**: Join courses using teacher-provided subject codes or one-click QR links.
- **Attendance Analytics**: Track attendance percentage and session totals for every enrolled subject.

---

## 🛠️ Tech Stack

| Domain | Technology |
| :--- | :--- |
| **Web Framework** | [Streamlit](https://streamlit.io/) (Python) |
| **Database & Cloud** | [Supabase](https://supabase.com/) (PostgreSQL & Realtime API) |
| **Computer Vision / AI** | `dlib`, `face_recognition`, `scikit-learn`, `numpy` |
| **Audio Processing** | Voice Embedding Matching |
| **Security & Auth** | `bcrypt` Password Hashing |
| **QR Code Generation** | `segno` |
| **UI Customization** | Custom CSS3 + Glassmorphism & SaaS Design Tokens |

---

## 🚀 Quick Start Guide

Follow these steps to run SnapClass locally on your machine.

### 1. Prerequisites
- **Python**: Version 3.10 or higher recommended.
- **Git**: Installed on your system.

### 2. Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/snapclass-ai-attendance.git
cd snapclass-ai-attendance
```

### 3. Create a Virtual Environment
```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirement.txt
```

> **Note for `dlib` installation**: On Windows, ensure CMake and Visual Studio C++ Build Tools are installed if compiling `dlib` from source.

### 5. Configure Database Credentials
Create a `.streamlit/secrets.toml` file in the root directory (you can copy `.streamlit/secrets.toml.example`):

```toml
# .streamlit/secrets.toml
SUPABASE_URL = "https://your-supabase-project.supabase.co"
SUPABASE_KEY = "your-supabase-anon-key"
```

### 6. Run the Application
```bash
streamlit run app.py
```
Open your browser and navigate to `http://localhost:8501`.

---

## 📁 Project Structure

```
AI attedance/
├── app.py                      # Main Streamlit application entry point
├── requirement.txt             # Python dependencies
├── README.md                   # Project documentation
├── .streamlit/
│   ├── config.toml
│   └── secrets.toml.example    # Supabase credentials template
└── src/
    ├── components/             # Reusable UI components & dialogs
    │   ├── dialog_add_photo.py
    │   ├── dialog_attendance_results.py
    │   ├── dialog_enroll.py
    │   ├── dialog_share_subject.py
    │   ├── dialog_voice_attendance.py
    │   ├── footer.py
    │   ├── header.py
    │   └── subject_card.py
    ├── database/               # Database config & CRUD queries
    │   ├── config.py
    │   └── db.py
    ├── pipelines/              # AI face recognition & voice pipelines
    │   ├── face_pipeline.py
    │   └── voice_pipeline.py
    ├── screens/                # Main application screens
    │   ├── home_screen.py
    │   ├── student_screen.py
    │   └── teacher_screen.py
    └── ui/                     # CSS design tokens & layout styles
        └── base_layout.py
```

---

## 👨‍💻 Author

Developed by **Niranjan**

---
*Built with ❤️ using Streamlit & Supabase*

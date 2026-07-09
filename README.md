# Snap Class

**Making attendance faster using AI.**

Snap Class is a Streamlit web app that automates classroom attendance using **face recognition** and **voice recognition**. Teachers create subjects, share a join code or QR code with students, and take attendance by simply snapping classroom photos or recording audio — no manual roll call needed.

## Features

### For Teachers
- **Account system** — register and log in with a username/password (passwords hashed with `bcrypt`).
- **Subject management** — create subjects with a code, name, and section; share them via a copyable link or a scannable QR code.
- **AI attendance — photos** — upload one or more classroom photos; the app detects faces, matches them against enrolled students, and marks who's present/absent.
- **AI attendance — voice** — record classroom audio; the app segments speech and identifies enrolled students by voice.
- **Attendance records** — view a history of sessions per subject with present/total counts.

### For Students
- **FaceID login** — log in by taking a selfie; the app matches it against your enrolled face.
- **Self-registration** — if your face isn't recognized, register a new profile (with optional voice enrollment) directly from the camera capture.
- **Join subjects** — enroll in a subject by entering a code, or automatically via a shared join link/QR code (`?join-code=...`).
- **Personal dashboard** — see enrolled subjects and your attendance stats per subject, and unenroll if needed.

## How It Works

1. **Face pipeline** (`src/pipelines/face_pipeline.py`) — uses `dlib` + `face_recognition_models` to detect faces and compute 128-d face embeddings, then trains a linear SVM (`scikit-learn`) on all enrolled students' stored embeddings to classify new faces, with a distance threshold to reject uncertain matches.
2. **Voice pipeline** (`src/pipelines/voice_pipeline.py`) — uses `resemblyzer` to compute voice embeddings from short audio clips, and `librosa` to split longer classroom recordings into speech segments for bulk speaker identification via cosine similarity.
3. **Database** (`src/database/`) — all data (teachers, students, subjects, enrollments, attendance logs) is stored in **Supabase** (Postgres), accessed through the `supabase-py` client.
4. **App routing** (`app.py`) — a single Streamlit entry point switches between the home, teacher, and student screens based on session state, and handles auto-enrollment when a student opens a class join link.

## Tech Stack

| Area | Technology |
|---|---|
| UI / App framework | [Streamlit](https://streamlit.io/) |
| Face recognition | `dlib-bin`, `face_recognition_models`, `scikit-learn` |
| Voice recognition | `librosa`, `resemblyzer` |
| Data handling | `numpy`, `pandas` |
| Database / Auth | `supabase`, `bcrypt` |
| QR codes / Images | `segno`, `pillow` |

## Requirements

- Python (3.10–3.12 recommended — some dependencies like `dlib-bin`, `librosa`, and `resemblyzer` may not have prebuilt wheels for very new Python releases such as 3.13/3.14).
- A [Supabase](https://supabase.com/) project with the following tables:
  - `teachers` (`teacher_id`, `username`, `password`, `name`)
  - `students` (`student_id`, `name`, `face_embedding`, `voice_embedding`)
  - `subjects` (`subject_id`, `subject_code`, `name`, `section`, `teacher_id`)
  - `subject_students` (`student_id`, `subject_id`) — enrollment join table
  - `attendance_logs` (`student_id`, `subject_id`, `timestamp`, `is_present`)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/abu-said-mondal/snapcalss-main.git
   cd snapcalss-main
   ```

2. **Create and activate a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Supabase secrets**

   Create `.streamlit/secrets.toml` (this file is gitignored) with:
   ```toml
   SUPABASE_URL = "your-supabase-url"
   SUPABASE_KEY = "your-supabase-key"
   ```

## Usage

Run the app locally with:

```bash
streamlit run app.py
```

This launches the app at `http://localhost:8501`.

### Joining a class via link

Teachers can share a subject's join link or QR code (generated in the "Share Class Link" dialog). Opening it takes the student to the app with a `join-code` in the URL, e.g.:

```
http://localhost:8501/?join-code=CS101
```

If the student is already logged in, a "Quick Enrollment" dialog pops up to confirm joining the subject.

## Project Structure

```
snapcalss-main/
├── app.py                              # App entry point & routing
├── requirements.txt                    # Python dependencies
├── .streamlit/
│   └── config.toml                     # Streamlit theme config
├── src/
│   ├── database/
│   │   ├── config.py                   # Supabase client setup
│   │   └── db.py                       # All database queries (teachers, students, subjects, attendance)
│   ├── pipelines/
│   │   ├── face_pipeline.py            # Face embedding, SVM training, face-based attendance prediction
│   │   └── voice_pipeline.py           # Voice embedding & speaker identification
│   ├── screens/
│   │   ├── home_screen.py              # Landing page (choose Student/Teacher)
│   │   ├── teacher_screen.py           # Teacher login/register + dashboard (attendance, subjects, records)
│   │   └── student_screen.py           # Student FaceID login/registration + dashboard
│   ├── components/
│   │   ├── header.py                   # Header UI components
│   │   ├── subject_card.py             # Subject card UI
│   │   ├── dialog_create_subject.py    # "Create Subject" dialog
│   │   ├── dialog_share_subject.py     # "Share Class Link" dialog (link + QR code)
│   │   ├── dialog_enroll.py            # Student "Enroll in Subject" dialog
│   │   ├── dialog_auto_enroll.py       # Auto-enroll dialog triggered by join links
│   │   ├── dialog_add_photo.py         # Add classroom photos for attendance
│   │   ├── dialog_attendance_results.py# Review & confirm attendance results
│   │   └── dialog_voice_attendance.py  # Voice-based attendance dialog
│   └── ui/
│       └── base_layout.py              # Shared page styling/layout helpers
```

## Roadmap / Ideas

- [ ] Attendance analytics and export (CSV/PDF reports)
- [ ] Class scheduling and calendar integration
- [ ] Improve face/voice recognition accuracy under varied lighting and noise
- [ ] Mobile-friendly UI polish

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with a clear description of your changes.

## License

Specify your project's license here (e.g., MIT, Apache 2.0).

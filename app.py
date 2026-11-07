from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-secret-key")

# Vercel's filesystem is read-only except /tmp, so use /tmp there.
DB_NAME = "/tmp/portfolio.db" if os.environ.get("VERCEL") else "portfolio.db"

PROJECTS = [
    {
        "title": "ALISTO",
        "role": "UI/UX Designer & Front-End Developer",
        "desc": "Offline voice-activated emergency response system. Designed the Figma storyboard, "
                "brand system, and role-based screens for four user roles.",
        "stack": ["Flask", "Figma", "HTML/CSS"],
        "url": "https://github.com/AprilEscuadro/Alisto",
        "cats": "uiux web",
        "img": "cottage.jpg",
        "alt": "",
    },
    {
        "title": "CCS Sit-in Monitoring System",
        "role": "UI/UX Designer & Developer",
        "desc": "Lab sit-in tracking and reservation system with a claymorphism interface, "
                "admin dashboard, and leaderboard.",
        "stack": ["Flask", "SQLite", "Jinja2", "JavaScript"],
        "url": "https://github.com/AprilEscuadro/SitinMonitoringSystem",
        "cats": "uiux web",
        "img": "green-door.jpg",
        "alt": "",
    },
    {
        "title": "Library Management System",
        "role": "",
        "desc": "CRUD and search across books, members, and borrowing records.",
        "stack": ["Flask", "SQLite"],
        "url": "",
        "cats": "web school",
        "img": "castle.jpg",
        "alt": "",
    },
    {
        "title": "Clinic Consultations Logging",
        "role": "",
        "desc": "Tracks student clinic visits and consultation records.",
        "stack": ["Flask", "SQLite"],
        "url": "",
        "cats": "web school",
        "img": "boat.jpg",
        "alt": "",
    },
    {
        "title": "UC ICT Congress Registration",
        "role": "",
        "desc": "Event registration platform for a university-wide ICT congress.",
        "stack": ["Flask", "Jinja2"],
        "url": "",
        "cats": "web school",
        "img": "fox.jpg",
        "alt": "",
    },
    {
        "title": "Events Registration System",
        "role": "",
        "desc": "General-purpose event sign-up with attendee management.",
        "stack": ["Flask", "SQLite"],
        "url": "",
        "cats": "web school",
        "img": "meadow.jpg",
        "alt": "",
    },
    {
        "title": "Auth System with JWT & RBAC",
        "role": "",
        "desc": "Authentication with refresh token rotation, role-based access, and email verification.",
        "stack": ["Node.js", "Angular", "MySQL"],
        "url": "",
        "cats": "web school",
        "img": "castle.jpg",
        "alt": "",
    },
]

ACHIEVEMENTS = [
    {
        "icon": "\U0001F3C5",
        "title": "TOPCIT Level 2 Certification",
        "desc": "Test of Practical Competency in IT, Level 2.",
        "meta": "2027",
    },
    {
        "icon": "\U0001F3A8",
        "title": "ALISTO Capstone Design",
        "desc": "Designed a 10-screen Figma storyboard and brand system, and an 8-screen prototype tested across four user roles.",
        "meta": "Capstone, 2026",
    },
    {
        "icon": "\U0001F9EA",
        "title": "Usability Fixes on CCS Sit-in",
        "desc": "Resolved notification panel scrolling and leaderboard filter issues to improve usability and data accuracy.",
        "meta": "2026",
    },
]


def init_db():
    """Create the contact_messages table if it doesn't exist."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contact_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TEXT DEFAULT (datetime('now', 'localtime'))
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html", projects=PROJECTS, achievements=ACHIEVEMENTS)


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Please fill in all fields.", "error")
        return redirect(url_for("home") + "#contact")

    try:
        init_db()
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO contact_messages (name, email, message) VALUES (?, ?, ?)",
            (name, email, message),
        )
        conn.commit()
        conn.close()
        flash("Thank you! Your message was sent.", "success")
    except sqlite3.Error:
        flash("Sorry, something went wrong. Please email aprilescuadro2004@gmail.com instead.", "error")

    return redirect(url_for("home") + "#contact")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
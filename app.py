from flask import Flask, render_template, request, flash, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "change-this-secret-key"  # pwede ni imo ilisan ug bisan unsa

DB_NAME = "portfolio.db"


def init_db():
    """Create the contact_messages table kung wala pa siya."""
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
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not email or not message:
        flash("Palihug i-fill up ang tanan nga fields, sir/ma'am!", "error")
        return redirect(url_for("home") + "#contact")

    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO contact_messages (name, email, message) VALUES (?, ?, ?)",
        (name, email, message),
    )
    conn.commit()
    conn.close()

    flash("Salamat! Na-send na imong message. Mubalik ko sa imo soon!", "success")
    return redirect(url_for("home") + "#contact")


if __name__ == "__main__":
    init_db()
    app.run(debug=True)

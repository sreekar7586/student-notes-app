from flask import Flask, render_template, request, redirect, url_for
import json
from datetime import datetime
import os

app = Flask(__name__)

NOTES_FILE = "notes.json"


def load_notes():
    # If file doesn't exist, create empty list
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            json.dump([], f)
    with open(NOTES_FILE, "r") as f:
        return json.load(f)


def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=4)


@app.route("/", methods=["GET"])
def index():
    """Display all notes with search functionality"""
    search = request.args.get("search", "")
    notes = load_notes()

    if search:
        search_lower = search.lower()
        notes = [
            n for n in notes
            if search_lower in n["name"].lower()
            or search_lower in n["note"].lower()
        ]

    return render_template("index.html", notes=notes, search=search)


@app.route("/add", methods=["GET", "POST"])
def add_note():
    if request.method == "POST":
        name = request.form["name"]
        note = request.form["note"]

        notes = load_notes()

        new_id = (max([n["id"] for n in notes]) + 1) if notes else 1

        notes.append({
            "id": new_id,
            "name": name,
            "note": note,
            "timestamp": datetime.now().strftime("%d-%b-%Y %H:%M")
        })

        save_notes(notes)
        return redirect(url_for("index"))

    return render_template("add_edit.html", note=None)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit_note(id):
    notes = load_notes()
    note_to_edit = next((n for n in notes if n["id"] == id), None)

    if note_to_edit is None:
        return "Note not found", 404

    if request.method == "POST":
        note_to_edit["name"] = request.form["name"]
        note_to_edit["note"] = request.form["note"]
        note_to_edit["timestamp"] = datetime.now().strftime("%d-%b-%Y %H:%M")
        save_notes(notes)
        return redirect(url_for("index"))

    return render_template("add_edit.html", note=note_to_edit)


@app.route("/delete/<int:id>")
def delete_note(id):
    notes = load_notes()
    notes = [n for n in notes if n["id"] != id]
    save_notes(notes)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

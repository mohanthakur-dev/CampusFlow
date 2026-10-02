from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


# ================= DATABASE =================

def get_db():
    conn = sqlite3.connect("campusflow.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():

    conn = get_db()

    # ---------- ASSIGNMENTS ----------

    conn.execute("""
        CREATE TABLE IF NOT EXISTS assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            title TEXT NOT NULL,
            deadline TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)

    # ---------- LAB RECORDS ----------

    conn.execute("""
        CREATE TABLE IF NOT EXISTS lab_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            experiment TEXT NOT NULL,
            deadline TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)

    # ---------- RESOURCES ----------

    conn.execute("""
        CREATE TABLE IF NOT EXISTS resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            title TEXT NOT NULL,
            resource_type TEXT NOT NULL,
            link TEXT
        )
    """)

    # ---------- CLASS UPDATES ----------

    conn.execute("""
        CREATE TABLE IF NOT EXISTS class_updates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            message TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)

    # ---------- PREVIOUS PAPERS ----------

    conn.execute("""
        CREATE TABLE IF NOT EXISTS previous_papers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            year TEXT NOT NULL,
            semester TEXT NOT NULL,
            exam_type TEXT NOT NULL,
            title TEXT NOT NULL,
            link TEXT
        )
    """)

    conn.commit()
    conn.close()


# Initialize database when the app starts
# This is required for both local Flask and Gunicorn/Render.
init_db()


# ================= HOME =================

@app.route("/")
def home():
    return render_template("index.html")


# ================= ASSIGNMENTS =================

@app.route("/assignments")
def assignments():

    conn = get_db()

    assignments = conn.execute(
        "SELECT * FROM assignments ORDER BY deadline"
    ).fetchall()

    conn.close()

    return render_template(
        "assignments.html",
        assignments=assignments
    )


@app.route("/add_assignment", methods=["POST"])
def add_assignment():

    subject = request.form["subject"]
    title = request.form["title"]
    deadline = request.form["deadline"]

    conn = get_db()

    conn.execute(
        """
        INSERT INTO assignments
        (subject, title, deadline)
        VALUES (?, ?, ?)
        """,
        (subject, title, deadline)
    )

    conn.commit()
    conn.close()

    return redirect("/assignments")


@app.route("/toggle_assignment/<int:id>", methods=["POST"])
def toggle_assignment(id):

    conn = get_db()

    assignment = conn.execute(
        "SELECT status FROM assignments WHERE id = ?",
        (id,)
    ).fetchone()

    if assignment["status"] == "Pending":
        new_status = "Completed"
    else:
        new_status = "Pending"

    conn.execute(
        """
        UPDATE assignments
        SET status = ?
        WHERE id = ?
        """,
        (new_status, id)
    )

    conn.commit()
    conn.close()

    return redirect("/assignments")


@app.route("/delete_assignment/<int:id>", methods=["POST"])
def delete_assignment(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM assignments WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/assignments")


# ================= LAB RECORDS =================

@app.route("/lab-records")
def lab_records():

    conn = get_db()

    lab_records = conn.execute(
        "SELECT * FROM lab_records ORDER BY deadline"
    ).fetchall()

    conn.close()

    return render_template(
        "lab-records.html",
        lab_records=lab_records
    )


@app.route("/add_lab_record", methods=["POST"])
def add_lab_record():

    subject = request.form["subject"]
    experiment = request.form["experiment"]
    deadline = request.form["deadline"]

    conn = get_db()

    conn.execute(
        """
        INSERT INTO lab_records
        (subject, experiment, deadline)
        VALUES (?, ?, ?)
        """,
        (subject, experiment, deadline)
    )

    conn.commit()
    conn.close()

    return redirect("/lab-records")


@app.route("/toggle_lab_record/<int:id>", methods=["POST"])
def toggle_lab_record(id):

    conn = get_db()

    lab = conn.execute(
        "SELECT status FROM lab_records WHERE id = ?",
        (id,)
    ).fetchone()

    if lab["status"] == "Pending":
        new_status = "Completed"
    else:
        new_status = "Pending"

    conn.execute(
        """
        UPDATE lab_records
        SET status = ?
        WHERE id = ?
        """,
        (new_status, id)
    )

    conn.commit()
    conn.close()

    return redirect("/lab-records")


@app.route("/delete_lab_record/<int:id>", methods=["POST"])
def delete_lab_record(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM lab_records WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/lab-records")


# ================= RESOURCES =================

@app.route("/resources")
@app.route("/notes")
def resources():

    conn = get_db()

    resources = conn.execute(
        """
        SELECT * FROM resources
        ORDER BY subject, title
        """
    ).fetchall()

    conn.close()

    return render_template(
        "resources.html",
        resources=resources
    )


@app.route("/add_resource", methods=["POST"])
def add_resource():

    subject = request.form["subject"]
    title = request.form["title"]
    resource_type = request.form["resource_type"]
    link = request.form["link"]

    conn = get_db()

    conn.execute(
        """
        INSERT INTO resources
        (subject, title, resource_type, link)
        VALUES (?, ?, ?, ?)
        """,
        (subject, title, resource_type, link)
    )

    conn.commit()
    conn.close()

    return redirect("/resources")


@app.route("/delete_resource/<int:id>", methods=["POST"])
def delete_resource(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM resources WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/resources")


# ================= CLASS UPDATES =================

@app.route("/class-updates")
def class_updates():

    conn = get_db()

    updates = conn.execute(
        """
        SELECT * FROM class_updates
        ORDER BY date DESC, id DESC
        """
    ).fetchall()

    conn.close()

    return render_template(
        "class-updates.html",
        updates=updates
    )


@app.route("/add_class_update", methods=["POST"])
def add_class_update():

    title = request.form["title"]
    message = request.form["message"]
    date = request.form["date"]

    conn = get_db()

    conn.execute(
        """
        INSERT INTO class_updates
        (title, message, date)
        VALUES (?, ?, ?)
        """,
        (title, message, date)
    )

    conn.commit()
    conn.close()

    return redirect("/class-updates")


@app.route("/delete_class_update/<int:id>", methods=["POST"])
def delete_class_update(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM class_updates WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/class-updates")


# ================= DEADLINES =================

@app.route("/deadlines")
def deadlines():

    conn = get_db()

    assignments = conn.execute(
        """
        SELECT
            id,
            subject,
            title,
            deadline,
            status,
            'Assignment' AS type
        FROM assignments
        """
    ).fetchall()

    labs = conn.execute(
        """
        SELECT
            id,
            subject,
            experiment AS title,
            deadline,
            status,
            'Lab Record' AS type
        FROM lab_records
        """
    ).fetchall()

    conn.close()

    all_deadlines = list(assignments) + list(labs)

    all_deadlines.sort(
        key=lambda x: x["deadline"]
    )

    return render_template(
        "deadlines.html",
        deadlines=all_deadlines
    )


# ================= PREVIOUS PAPERS =================

@app.route("/previous-papers")
def previous_papers():

    conn = get_db()

    papers = conn.execute(
        """
        SELECT *
        FROM previous_papers
        ORDER BY year DESC, subject, semester
        """
    ).fetchall()

    conn.close()

    return render_template(
        "previous-papers.html",
        papers=papers
    )


@app.route("/add_previous_paper", methods=["POST"])
def add_previous_paper():

    subject = request.form["subject"]
    year = request.form["year"]
    semester = request.form["semester"]
    exam_type = request.form["exam_type"]
    title = request.form["title"]
    link = request.form["link"]

    conn = get_db()

    conn.execute(
        """
        INSERT INTO previous_papers
        (subject, year, semester, exam_type, title, link)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            subject,
            year,
            semester,
            exam_type,
            title,
            link
        )
    )

    conn.commit()
    conn.close()

    return redirect("/previous-papers")


@app.route("/delete_previous_paper/<int:id>", methods=["POST"])
def delete_previous_paper(id):

    conn = get_db()

    conn.execute(
        "DELETE FROM previous_papers WHERE id = ?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/previous-papers")


# ================= DASHBOARD =================

@app.route("/dashboard")
def dashboard():

    conn = get_db()

    # ---------- ASSIGNMENT STATS ----------

    total_assignments = conn.execute(
        "SELECT COUNT(*) FROM assignments"
    ).fetchone()[0]

    pending_assignments = conn.execute(
        """
        SELECT COUNT(*)
        FROM assignments
        WHERE status = 'Pending'
        """
    ).fetchone()[0]

    completed_assignments = conn.execute(
        """
        SELECT COUNT(*)
        FROM assignments
        WHERE status = 'Completed'
        """
    ).fetchone()[0]

    # ---------- LAB STATS ----------

    total_labs = conn.execute(
        "SELECT COUNT(*) FROM lab_records"
    ).fetchone()[0]

    pending_labs = conn.execute(
        """
        SELECT COUNT(*)
        FROM lab_records
        WHERE status = 'Pending'
        """
    ).fetchone()[0]

    # ---------- TOTAL PENDING DEADLINES ----------

    total_deadlines = conn.execute(
        """
        SELECT COUNT(*)
        FROM assignments
        WHERE status = 'Pending'
        """
    ).fetchone()[0]

    total_deadlines += conn.execute(
        """
        SELECT COUNT(*)
        FROM lab_records
        WHERE status = 'Pending'
        """
    ).fetchone()[0]

    # ---------- UPCOMING WORK ----------

    upcoming_assignments = conn.execute(
        """
        SELECT
            id,
            subject,
            title,
            deadline,
            status,
            'Assignment' AS type
        FROM assignments
        WHERE status = 'Pending'
        """
    ).fetchall()

    upcoming_labs = conn.execute(
        """
        SELECT
            id,
            subject,
            experiment AS title,
            deadline,
            status,
            'Lab Record' AS type
        FROM lab_records
        WHERE status = 'Pending'
        """
    ).fetchall()

    upcoming = list(upcoming_assignments) + list(upcoming_labs)

    upcoming.sort(
        key=lambda item: item["deadline"]
    )

    upcoming = upcoming[:5]

    # ---------- LATEST CLASS UPDATE ----------

    latest_update = conn.execute(
        """
        SELECT *
        FROM class_updates
        ORDER BY date DESC, id DESC
        LIMIT 1
        """
    ).fetchone()

    conn.close()

    return render_template(
        "dashboard.html",
        total_assignments=total_assignments,
        pending_assignments=pending_assignments,
        completed_assignments=completed_assignments,
        total_labs=total_labs,
        pending_labs=pending_labs,
        total_deadlines=total_deadlines,
        upcoming=upcoming,
        latest_update=latest_update
    )


# ================= START APP =================

if __name__ == "__main__":

    app.run(debug=True)
import os
from datetime import datetime
from zoneinfo import ZoneInfo

from flask import Flask, render_template, redirect, url_for, send_from_directory, abort
# from waitress import serve
app = Flask(__name__)
app.jinja_env.globals.update(zip=zip)

COLLEGE_PARK_TZ = ZoneInfo("America/New_York")
RELEASE_HOUR = 14
RELEASE_MINUTE = 30

DOWNLOADS_DIR = os.path.join(app.root_path, "protected_downloads")

# Starter-code release datetimes, in College Park (America/New_York) local time.
# Each project unlocks at RELEASE_HOUR:RELEASE_MINUTE on its assigned date.
PROJECT_RELEASE_DATES = {
    "p1": datetime(2026, 9, 4, RELEASE_HOUR, RELEASE_MINUTE, tzinfo=COLLEGE_PARK_TZ),
    "p2": datetime(2026, 9, 11, RELEASE_HOUR, RELEASE_MINUTE, tzinfo=COLLEGE_PARK_TZ),
    "p3": datetime(2026, 10, 2, RELEASE_HOUR, RELEASE_MINUTE, tzinfo=COLLEGE_PARK_TZ),
    "p4": datetime(2026, 10, 23, RELEASE_HOUR, RELEASE_MINUTE, tzinfo=COLLEGE_PARK_TZ),
}

@app.route('/')
def index():
    return redirect(url_for("homepage"))

@app.route('/388j')
def homepage():
    return render_template('home.html')

@app.route('/388j/projects')
def projects():
    return render_template('projects.html')

@app.route('/388j/download/<project_id>')
def download_project(project_id):
    release_at = PROJECT_RELEASE_DATES.get(project_id)
    if release_at is None:
        abort(404)

    if datetime.now(COLLEGE_PARK_TZ) < release_at:
        abort(404)

    return send_from_directory(DOWNLOADS_DIR, f"{project_id}.zip", as_attachment=True)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)  # local dev only

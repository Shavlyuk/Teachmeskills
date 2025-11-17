from flask import Flask, render_template_string, request, redirect
import sqlite3

app = Flask(__name__)

DB_PATH = "wishes.db"


def init_db():

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS wishes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")

        if name and message:
            conn = sqlite3.connect(DB_PATH)
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO wishes (name, message) VALUES (?, ?)",
                (name, message)
            )
            conn.commit()
            conn.close()

        return redirect("/")

    wishes = []

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT name, message FROM wishes ORDER BY id DESC")
    wishes = cur.fetchall()
    conn.close()

    # HTML шаблон
    TEMPLATE = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Книга пожеланий</title>
    </head>
    <body>
        <h1>Книга пожеланий 💌</h1>

        <form method="post">
            <p><input type="text" name="name" placeholder="Ваше имя" required></p>
            <p><textarea name="message" placeholder="Ваше пожелание" required></textarea></p>
            <p><button type="submit">Оставить пожелание</button></p>
        </form>

        <h2>Все пожелания:</h2>
        {% for name, message in wishes %}
            <div style="border:1px solid #ccc; margin:10px; padding:10px;">
                <strong>{{ name }}</strong><br>
                <em>{{ message }}</em>
            </div>
        {% endfor %}
    </body>
    </html>
    """

    return render_template_string(TEMPLATE, wishes=wishes)


if __name__ == "__main__":
    app.run(debug=True)
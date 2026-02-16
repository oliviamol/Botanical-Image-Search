from flask import Flask, render_template, request
import os

app = Flask(__name__, static_folder="static", template_folder="templates")

# Folder unde sunt imaginile cu flori
Folder_baza = "static/flori_proiect/"

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    message = None

    if request.method == "POST":
        floare = request.form.get("floare").lower()
        floare_file = floare.replace(" ", "_")
        extensii = [".jpg", ".jpeg", ".png"]

        # Căutăm imaginea
        for ext in extensii:
            nume_complet = floare_file + ext
            file_path = os.path.join(Folder_baza, nume_complet)
            if os.path.exists(file_path):
                image_url = f"flori_proiect/{nume_complet}"
                break

        if not image_url:
            message = f"Nu am găsit nicio poză pentru floarea '{floare}'."

    return render_template("index.html", image_url=image_url, message=message)

if __name__ == "__main__":
    app.run(debug=True)
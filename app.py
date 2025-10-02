from flask import Flask, render_template, request, send_file
from docxtpl import DocxTemplate
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        plantilla = DocxTemplate("plantilla.docx")

        diccionario = {
            "nombre": request.form["nombre"],
            "apodo": request.form["apodo"],
            "edad": request.form["edad"],
            "gen": request.form["genero"],
            "alto": request.form["altura"],
            "peso": request.form["peso"],
            "color_cabello": request.form["color_cabello"],
            "color_ojos": request.form["color_ojos"],
            "complexion": request.form["complexion"],
            "ocupacion": request.form["ocupacion"],
            "lugar_nac": request.form["lugar_nac"],
            "fecha_nac": request.form["fecha_nac"]
        }

        plantilla.render(diccionario)

        output = io.BytesIO()
        plantilla.save(output)
        output.seek(0)

        return send_file(
            output,
            as_attachment=True,
            download_name=f"{diccionario['nombre']}.docx"
        )

    return render_template("formulario.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

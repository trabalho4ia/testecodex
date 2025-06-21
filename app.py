import os
from flask import (
    Flask,
    request,
    render_template,
    redirect,
    url_for,
    send_from_directory,
)
from werkzeug.utils import secure_filename
import pdfplumber
from transformers import pipeline

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Armazena o texto do PDF carregado
pdf_text = ""
pdf_filename = None
qa_model = None


def carregar_modelo():
    """Carrega o modelo de QA apenas uma vez."""
    global qa_model
    if qa_model is None:
        qa_model = pipeline(
            "question-answering",
            model="pierreguillou/bert-base-cased-squad-v1.1-portuguese",
        )


@app.route("/", methods=["GET"])
def index():
    url = None
    if pdf_filename:
        url = url_for("uploaded_file", filename=pdf_filename)
    return render_template(
        "index.html",
        pdf_carregado=bool(pdf_text),
        resposta=None,
        pdf_url=url,
    )


@app.route("/upload", methods=["POST"])
def upload_pdf():
    global pdf_text, pdf_filename
    arquivo = request.files.get("pdf")
    if not arquivo:
        return redirect(url_for("index"))

    filename = secure_filename(arquivo.filename)
    if not filename:
        filename = "uploaded.pdf"
    caminho = os.path.join(UPLOAD_FOLDER, filename)
    arquivo.save(caminho)
    pdf_filename = filename

    with pdfplumber.open(caminho) as pdf:
        texto = "\n".join(pagina.extract_text() or "" for pagina in pdf.pages)
    pdf_text = texto
    return redirect(url_for("index"))


@app.route("/perguntar", methods=["POST"])
def perguntar():
    pergunta = request.form.get("pergunta")
    if not pergunta or not pdf_text:
        return redirect(url_for("index"))

    carregar_modelo()
    resposta = qa_model(question=pergunta, context=pdf_text)
    texto_resposta = resposta.get("answer")
    return render_template(
        "index.html", pdf_carregado=True, resposta=texto_resposta
    )


@app.route("/uploads/<path:filename>")
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)

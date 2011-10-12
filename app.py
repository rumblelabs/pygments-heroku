import os
from flask import Flask, request, logging

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

import markdown

app = Flask(__name__)

def pygmentize(lang, code):
  lexer = get_lexer_by_name(lang)
  formatter = HtmlFormatter()
  return highlight(code, lexer, formatter)


@app.route('/', methods=['GET'])
def index():
  src = open('README.md', 'r').read()
  html = markdown.markdown(src)
  return html


@app.route('/', methods=['POST'])
def pygments():
  lang = request.form["lang"]
  code = request.form["code"]
  return pygmentize(lang, code)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # For debugging & automatic relaoding of flask apps, set debug=True
    app.run(host='0.0.0.0', port=port)
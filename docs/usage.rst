========
Usage
========

Setup is done using the following environment variables:

+========================+======================================+=======================+
| Variable               | Notes                                | Default               |
+========================+======================================+=======================+
| LATEXRENDER_OUTPUT_DIR | Directory where image files will     | ``/tmp/latexrender/`` |
|                        | be saved and served from             |                       |
+------------------------+--------------------------------------+-----------------------+
| LATEXRENDER_TEMPLATE   | Jinja2 template to use for rendering | ``template.tex`` in   |
|                        | the LaTeX snippet.                   | installation          |
|                        |                                      | directory             |
+------------------------+--------------------------------------+-----------------------+
| LATEXRENDER_XELATEX    | Location of xelatex executable.      | (Auto)                |
+------------------------+--------------------------------------+-----------------------+
| LATEXRENDER_PDFTOPS    | Location of pdftops executable.      | (Auto)                |
+------------------------+--------------------------------------+-----------------------+
| USE_X_SENDFILE         | Whether to use X-Senfile or serve    | ``True``              |
|                        | the generated image directly.        |                       |
+------------------------+--------------------------------------+-----------------------+


Run using your favourite WSGI server::

    chausette latexrender.app
    gunicorn latexrender.app

Pass base64 encoded LaTeX snippets as the URL in one of the following forms::

    http://localhost:8080/<b64latex>/
    http://localhost:8080/<b64latex>.png

========
Usage
========

Configuration
-------------

Setup is done using the following environment variables:

+------------------------+--------------------------------------+-----------------------+
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
| LATEXRENDER_DVIPNG     | Location of dvipng executable.       | (Auto)                |
+------------------------+--------------------------------------+-----------------------+
| USE_X_SENDFILE         | Whether to use X-Sendfile or serve   | ``True``              |
|                        | the generated image directly.        |                       |
+------------------------+--------------------------------------+-----------------------+

If not specified your path will be inspected to find ``latex`` and ``dvipng``.

The default template, in Jinja2 format, is

.. literalinclude:: ../latexrender/template.tex

Deploying
---------

Run using your favourite WSGI server::

    chausette latexrender.app
    gunicorn latexrender:app

It is recommended that you run this behind a frontend proxy such as nginx and
use X-Sendfile to have that serve the image files.

Pass base64 encoded LaTeX snippets as the URL in one of the following forms::

    http://localhost:8080/<b64latex>/
    http://localhost:8080/<b64latex>.png


In the default template the surrounding math environment is not specified so 
you can, for example, use input of the form::

    $$ e^{i\pi} + 1 = 0 $$

or::

    \begin{equation*}
        e^{i\pi} + 1 = 0
    \end{equation}


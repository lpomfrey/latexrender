===============================
latexrender
===============================

.. image:: https://badge.fury.io/py/latexrender.png
    :target: http://badge.fury.io/py/latexrender
    
.. image:: https://travis-ci.org/lpomfrey/latexrender.png?branch=master
    :target: https://travis-ci.org/lpomfrey/latexrender

.. image:: https://coveralls.io/repos/lpomfrey/latexrender/badge.png 
    :target: https://coveralls.io/r/lpomfrey/latexrender 

.. image:: https://pypip.in/d/latexrender/badge.png
    :target: https://crate.io/packages/latexrender?version=latest


A simple Flask app for rendering LaTeX snippets into images.

* Free software: BSD license
* Documentation: http://latexrender.rtfd.org.

Installation and Usage
----------------------

Install using pip::
    pip install latexrender

Run using your favourite WSGI server::
    chausette latexrender.app
    gunicorn latexrender.app

Pass base64 encoded LaTeX snippets as the URL in one of the following forms::
    http://localhost:8080/<b64latex>/
    http://localhost:8080/<b64latex>.png

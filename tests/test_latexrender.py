#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_latexrender
----------------------------------

Tests for `latexrender` module.
"""

import base64
import hashlib
import os
import shutil
import unittest

from PIL import Image
from six import StringIO
from webtest import TestApp

from latexrender import app


ILLEGAL_TAGS = [
    '\\afterassignment',
    '\\aftergroup',
    '\\errhelp',
    '\\errorstopmode',
    '\\every',
    '\\expandafter',
    '\\lowercase',
    '\\newhelp',
    '\\noexpand',
    '\\nonstopmode',
    '\\read',
    '\\relax',
    '\\scrollmode',
    '\\special'
    '\\uppercase',
    '\\write',
    '\\batchmode',
    '^^',
    'catcode',
    'command',
    'csname',
    'def',
    'include',
    'input',
    'loop',
    'name',
    'open',
    'output',
    'repeat',
    'toks',
]


class TestLatexrender(unittest.TestCase):

    def setUp(self):
        app.config['USE_X_SENDFILE'] = True
        self.output_dir = app.config.get('OUTPUT_DIR')
        self.application = TestApp(app)
        self.application.debug = True

    def test_illegal_tags(self):
        for tag in ILLEGAL_TAGS:
            latex = '$$ a + x = 1 {0} $$'.format(tag)
            latex = base64.b64encode(latex)
            self.application.get('/{0}/'.format(latex), status=400)

    def test_invalid_latex(self):
        latex = r'$$ a + x = 1 $ \begin{a} \/\/'
        latex = base64.b64encode(latex)
        self.application.get('/{0}/'.format(latex), status=400)

    def test_creates_file_with_md5(self):
        latex = r'$$ a + x = 1 $$'
        latex = base64.b64encode(latex)
        ltx_hash = hashlib.md5(latex).hexdigest()
        self.application.get('/{0}/'.format(latex), status=200)
        self.assertTrue(os.path.exists(
            os.path.join(self.output_dir, '{0}.png'.format(ltx_hash))
        ))

    def test_uses_sendfile(self):
        self.application.app.use_x_sendfile = True
        latex = r'$$ a + x = 3 $$'
        latex = base64.b64encode(latex)
        ltx_hash = hashlib.md5(latex).hexdigest()
        file_path = os.path.join(self.output_dir, '{0}.png'.format(ltx_hash))
        resp = self.application.get('/{0}/'.format(latex), status=200)
        self.assertEqual(resp.headers['X-Sendfile'], file_path)

    def test_uses_previously_generated_file(self):
        self.application.app.config['USE_X_SENDFILE'] = False
        latex = r'$$ a + x = 2 $$'
        latex = base64.b64encode(latex)
        ltx_hash = hashlib.md5(latex).hexdigest()
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        file_path = os.path.join(self.output_dir, '{0}.png'.format(ltx_hash))
        img = Image.new('RGB', (5, 5))
        with open(file_path, 'w') as f:
            img.save(f, 'PNG')
        buffer = StringIO()
        img.save(buffer, 'PNG')
        resp = self.application.get('/{0}/'.format(latex), status=200)
        self.assertEqual(resp.body, buffer.getvalue())

    def tearDown(self):
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)


if __name__ == '__main__':
    unittest.main()

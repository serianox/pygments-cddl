# -*- coding: utf-8 -*-
"""
    pygments.lexers.cddl
    ~~~~~~~~~~~~~~~~~~~~

    Lexer for Concise data definition language (CDDL).

    :copyright: Copyright 2019 by Thomas Duboucher.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, words
from pygments.token import *

__all__ = ['CddlLexer']

class CddlLexer(RegexLexer):
    name = 'CDDL'
    aliases = ['cddl']
    filenames = ['*.cddl']
    mimetypes = []

    tokens = {
        'root': [
            (r'\s+', Text),
            (r';.*?$', Comment),
            ('"', String, 'string'),
            (r'(h|b64)?\'', String.Hex, 'hstring'),
            (words(('any', 'uint', 'nint', 'int', 'bstr', 'bytes', 'tstr', 'text', 'tdate', 'time', 'number', 'biguint', 'bignint', 'bigint', 'integer', 'unsigned', 'decfrac', 'bigfloat', 'eb64url', 'eb64legacy', 'eb16', 'encoded-cbor', 'uri', 'b64url', 'b64legacy', 'regexp', 'mime-message', 'cbor-any', 'float16', 'float32', 'float64', 'float16-32', 'float32-64', 'float', ), suffix=r'\b'), Keyword.Type),
            (r'#([0-7](.\d+)?)?', Keyword.Type),
            (words(('false', 'true', 'bool', 'nil', 'null', 'undefined', ), suffix=r'\b'), Keyword.Reserved),
            (words(('.size', '.bits', '.regexp', '.cbor', '.cborseq', '.within', '.and', '.lt', '.le', '.gt', '.ge', '.eq', '.ne', '.default', ), suffix=r'\b'), Keyword),
            (r'[a-zA-Z@_$][a-zA-Z0-9@_$]*([-\.][a-zA-Z0-9@_$]+)*', Name),
            (r'(\d+\.\d+|\d+)([eE][+-]?\d+)?', Number.Float),
            (r'0x[0-9a-fA-F]+(.[0-9a-fA-F]+)*([pP][+-]?\d+)?', Number.Float),
            (r'0x[0-9a-fA-F]+', Number.Hex),
            (r'0o[0-7]+', Number.Oct),
            (r'0b[0-1]+', Number.Bin),
            (r'\d+', Number.Integer),
            (r'=>|[/=\?\+\*:~^&]', Operator),
            (r'[()\[\]{}<>,.]', Punctuation),
        ],
        'string': [
            ('[^"]+', String),
            ('"', String, '#pop'),
        ],
        'hstring': [
            ('[^\']+', String),
            ('\'', String, '#pop'),
        ],
    }
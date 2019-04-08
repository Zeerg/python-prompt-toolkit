#!/usr/bin/env python
"""
Simple example of a syntax-highlighted HTML input line.
(This requires Pygments to be installed.)
"""
from __future__ import unicode_literals

from prompt_toolkit import prompt
from prompt_toolkit.lexers import PygmentsLexer
from pygments.lexers.html import HtmlLexer


def main():
    text = prompt('Enter HTML: ', lexer=PygmentsLexer(HtmlLexer))
    print('You said: %s' % text)


if __name__ == '__main__':
    main()

#!/usr/bin/python3
""" validate a markdown file
"""
import sys
import os


args = sys.argv
if len(args) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
    exit(1)

if os.path.exists("./README.md"):
    exit(0)
else:
    sys.stderr.write("Missing {}".format(args[1]))
    exit(1)

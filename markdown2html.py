#!/usr/bin/python3
""" validate a markdown file
"""
import sys
import os


args = sys.argv
if len(args) < 3:
    print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
    exit(1)

if os.path.exists("./README.md"):
    exit(0)
else:
    print("Missing {}".format(args[1]), file=sys.stderr)
    exit(1)

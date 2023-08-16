#!/usr/bin/python3
""" validate a markdown file
"""
import sys
import os


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    if os.path.exists(args[1]):
        sys.exit(0)
    else:
        sys.stderr.write("Missing {}".format(args[1]))
        sys.exit(1)

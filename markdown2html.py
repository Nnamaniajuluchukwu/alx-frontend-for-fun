#!/usr/bin/python3
""" validate a markdown file
"""
import sys
import os
import markdown


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)

    try:
        # Convert the Markdown to HTML
        with open(args[1], 'r') as f:
            html = markdown.markdown(f.read())

        # Write the HTML to the output file
        with open(args[2], 'w') as f:
            f.write(html)

        # Exit successfully
        sys.exit(0)

    except FileNotFoundError:
        sys.stderr.write(f"Missing {args[1]}\n")
        sys.exit(1)

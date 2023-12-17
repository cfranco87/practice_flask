#!/usr/bin/env python3

from website import create_app

app = create_app()
"""simplifying create_app function to 'app'"""

if __name__ == '__main__':
    app.run(debug=True)
    """this tells it that it will only run flask webframe 
    when its the main file and not an import"""

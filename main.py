from website import create_app

app = create_app()
"""simplifying create_app function to 'app'"""

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    """this tells it that it will only run flask webframe 
    when its the main file and not an import"""

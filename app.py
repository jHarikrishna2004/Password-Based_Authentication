from flask import Flask, render_template, request
from password_logic import check_password_strength

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    suggestions = []
    error = None

    if request.method == 'POST':
        password = request.form.get('password')

        if not password:
            error = "Password is required"
        else:
            result, suggestions = check_password_strength(password)

    return render_template('index.html', result=result, suggestions=suggestions, error=error)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
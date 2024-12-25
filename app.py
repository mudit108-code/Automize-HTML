from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Directory to save the modernized HTML
SAVE_DIR = "modernized_html"
os.makedirs(SAVE_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/edit', methods=['POST'])
def edit():
    original_code = request.form['html_code']
    return render_template('edit.html', original_code=original_code)

@app.route('/save', methods=['POST'])
def save():
    modernized_code = request.form['edited_code']
    original_code = request.form['original_code']
    
    # Save modernized code to a file
    file_path = os.path.join(SAVE_DIR, "modernized.html")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(modernized_code)
    
    return render_template('index.html', message="Modernized HTML saved successfully!")

@app.route('/compare', methods=['POST'])
def compare():
    original_code = request.form['original_code']
    modernized_code = request.form['edited_code']
    return render_template('compare.html', original_code=original_code, modernized_code=modernized_code)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template_string, request
import os
import random  
app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <title>Random Number Generator</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f8f9fa;
                    margin: 0;
                    padding: 0;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                }
                .container {
                    text-align: center;
                    background: #ffffff;
                    padding: 20px;
                    border-radius: 8px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                }
                h1 {
                    color: #343a40;
                }
                button {
                    background-color: #007bff;
                    color: white;
                    border: none;
                    padding: 10px 20px;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 16px;
                }
                button:hover {
                    background-color: #0056b3;
                }
                p {
                    margin-top: 20px;
                    color: #6c757d;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Generate Random Number</h1>
                <form action="/random" method="post">
                    <button type="submit">Generate Random Number</button>
                </form>
                <p>Donratam 1650702549 328A</p>
            </div>
        </body>
        </html>
    ''')

@app.route('/random', methods=['POST'])
def random_number():
    try:
        random_number = random.randint(1, 100)  
        return render_template_string(f'''
            <!doctype html>
            <html lang="en">
            <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <title>Random Number</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f8f9fa;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                    }}
                    .container {{
                        text-align: center;
                        background: #ffffff;
                        padding: 20px;
                        border-radius: 8px;
                        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    }}
                    h1 {{
                        color: #343a40;
                    }}
                    p {{
                        margin-top: 20px;
                        color: #6c757d;
                    }}
                    a {{
                        display: inline-block;
                        margin-top: 20px;
                        text-decoration: none;
                        color: #007bff;
                        font-size: 16px;
                    }}
                    a:hover {{
                        color: #0056b3;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Random Number</h1>
                    <p>Generated Number: {random_number}</p>
                    <a href="/">Go back</a>
                </div>
            </body>
            </html>
        ''')
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    try:
        port = int(os.getenv("PORT", 8000))  
        print(f"Starting server on port {port}...") 
        app.run(host='0.0.0.0', port=port, debug=True) 
    except Exception as e:
        print(f"Error starting the server: {e}")  
        raise  

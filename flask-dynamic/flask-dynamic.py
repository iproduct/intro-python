from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
     return """
    <html>
    <head>
        <title>Flask Hallo World</title>
        <style>
            body {
                font-family: Helvetica, Arial, sans-serif;
                font-variant: small-caps;
            }
            .list {
                list-style-type: none;
            }
            .list li {
                display: inline-block;
                background-color: #2288ff;
                color: white;
                padding: 5px 10px;
                min-width: 100px;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <h2>Hello from Flask!</h2>
        <h3 style="background-color:powderblue;">Things to learn:</h3>
        <p style="color: blue">Things is a paragraph.</h3>
        <ul class="list">
            <li>Add routes</li>
            <li>Create handler</li>
            <li>Start the server</li>
        </ul>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run()

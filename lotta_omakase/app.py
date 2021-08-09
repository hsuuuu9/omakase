from flask import Flask, render_template #追加

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hoge"
    return render_template('index.html')

## おまじない
if __name__ == "__main__":
    app.run(debug=True)

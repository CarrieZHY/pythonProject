from flask import Flask, render_template, request

app = Flask(__name__)

data = [
    {'id': 0, 'name': '中秋节', 'num': 0},
    {'id': 1, 'name': '春节', 'num': 0},
    {'id': 2, 'name': '建军节', 'num': 0}
]
@app.route('/index')
def index():
    return render_template('index.html', data=data)

@app.route('/dianzan')
def dianzan():
    id = request.args.get('id')
    name = data[int(id)]['name']
    print(f'想要给{name}点赞!')
    data[int(id)]['num'] += 1
    return render_template('index.html', data=data)

app.run(debug=True)

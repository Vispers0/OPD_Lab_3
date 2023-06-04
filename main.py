import math

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/figure', methods=['POST'])
def figure():
    selection = str(request.form.get('cmb_figures'))
    match selection:
        case "cube":
            return render_template("cube.html")
        case "prism":
            return render_template("prism.html")
        case "parallel":
            return render_template("parallel.html")
        case "rect_parallel":
            return render_template("rect_parallel.html")
        case "pyramid":
            return render_template("pyramid.html")
        case "tetra":
            return render_template("tetra.html")
        case "cylinder":
            return render_template("cylinder.html")
        case "cone":
            return render_template("cone.html")
        case "ball":
            return render_template("ball.html")


@app.route('/cube', methods=['POST'])
def cube():
    side = float(request.form.get('side'))
    precision = int(request.form.get('precision'))
    sq = round(side ** 3, precision)
    return render_template("cube.html", square="Объём куба = " + str(sq))


@app.route('/prism', methods=['POST'])
def prism():
    base_sq = float(request.form.get('base_sq'))
    height = float(request.form.get('height'))
    precision = int(request.form.get('precision'))

    sq = round(base_sq * height, precision)
    return render_template('prism.html', square="Объём призмы = " + str(sq))


@app.route('/parallel', methods=['POST'])
def parallel():
    base_sq = float(request.form.get('base_sq'))
    height = float(request.form.get('height'))
    precision = int(request.form.get('precision'))

    sq = round(base_sq * height, precision)
    return render_template('parallel.html', square="Объём параллелепипеда = " + str(sq))


@app.route('/rect_parallel', methods=['POST'])
def rect_parallel():
    length = float(request.form.get('length'))
    width = float(request.form.get('width'))
    height = float(request.form.get('height'))
    precision = int(request.form.get('precision'))

    sq = round(length * width * height, precision)
    return render_template('rect_parallel.html', square="Объём прямоугольного параллелепипеда = " + str(sq))


@app.route('/pyramid', methods=['POST'])
def pyramid():
    base_sq = float(request.form.get('base_sq'))
    height = float(request.form.get('height'))
    precision = int(request.form.get('precision'))

    sq = round((1/3) * base_sq * height, precision)
    return render_template('pyramid.html', square="Объём пирамиды = " + str(sq))


@app.route('/tetra', methods=['POST'])
def tetra():
    side = float(request.form.get('side'))
    precision = int(request.form.get('precision'))

    sq = round((side ** 3 * math.sqrt(2)) / 12, precision)
    return render_template('tetra.html', square="Объём правильного тетраэдра = " + str(sq))


@app.route('/cylinder', methods=['POST'])
def cylinder():
    rad = float(request.form.get('rad'))
    height = float(request.form.get('height'))
    precision = int(request.form.get('precision'))

    sq = round(3.14 * rad ** 2 * height, precision)
    return render_template('cylinder.html', square="Объём цилиндра = " + str(sq))


@app.route('/cone', methods=['POST'])
def cone():
    rad = float(request.form.get('rad'))
    height = float(request.form.get('height'))
    precision = int(request.form.get('precision'))

    sq = round((1/3) * 3.14 * rad ** 2 * height, precision)
    return render_template('cone.html', square="Объём конуса = " + str(sq))


@app.route('/ball', methods=['POST'])
def ball():
    rad = float(request.form.get('rad'))
    precision = int(request.form.get('precision'))

    sq = round((4/3) * 3.14 * rad ** 3, precision)
    return render_template('ball.html', square="Объём шара = " + str(sq))


if __name__ == '__main__':
    app.run()

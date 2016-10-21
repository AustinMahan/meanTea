import queries
import json
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Authorization, Origin, Accept, Content-Type, X-Requested-With'
    return response

@app.route("/", methods=['GET'])
def hello():
    items = queries.getAll('items')
    items = queries.getCategories('categories', items)
    out = []
    for item in items:
        print(item[9])
        out.append({'id':item[0], 'name':item[1], 'ingredients': item[2], 'price':item[4], 'caffeinescale': item[3], 'instock': item[5], 'rating': item[6], 'imageurl': item[7], '__v': item[8], 'catergories': item[9]})

    return jsonify({'items': out})


@app.route("/new", methods=['POST'])
def newKitten():
    body = request.json
    queries.addOne(body)
    return ''


app.run(debug=True)

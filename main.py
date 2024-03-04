from flask import Flask, jsonify
# cette ligne emporte Flask du module et jsonify .
app = Flask(__name__)

#Endpoint pour recuperer des données
@app.route('/', methods=['GET'])
def get_data():
    data = {'message': 'Bonjour quelques données pour apprendre à faire..ça'}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)

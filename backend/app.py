from flask import Flask, jsonify
from flask_cors import CORS
from models import User, session

app = Flask(__name__)
CORS(app)

@app.route('/users', methods=['GET'])
def get_users():
    users = session.query(User).all()
    result = [{'name': user.name, 'age': user.age} for user in users]
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

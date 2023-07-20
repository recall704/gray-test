from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/api')
def api():
    headers = dict(request.headers)
    env_var = os.environ.get('SERVER_NAME') 
    data = {
        'headers': headers,
        'env_var': env_var
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8000)

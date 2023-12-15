from flask import Flask, jsonify, request
app = Flask(__name__)
heartrate = [
    {
        "heart_ID": "1",
        "name": "Lance",
        "date": "15/12/2023",
        "heart_rate": "120BPM"
    },
    {
        "heart_ID": "2",
        "name": "Virgo",
        "date": "16/12/2023",
        "heart_rate": "160BPM"
    }
]
@app.route('/heartrate', methods = ['Get'])
def getheartrate():
    return jsonify(heartrate)

@app.route('/heartrate', methods = ['Post'])
def add_heart():
    heart = request.get_json()
    heartrate.append(heart)
    return {'id': len(heartrate)}, 200

@app.route('/heartrate/<int:index>', methods = ['Delete'])
def delete_heart(index):
    heartrate.pop(index)
    return 'The Record has been deleted forever and ever and ever.', 200

if __name__=='__main__':
    app.run()
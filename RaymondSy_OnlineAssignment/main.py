from flask import Flask, jsonify
from flask import request
from flask import abort


app = Flask(__name__)
numberList = []
@app.route('/data', methods=['GET', 'POST', 'PATCH'])
def data():
    global numberList
    if request.method == 'POST':
        data = request.get_json(force=True) #if any format other than JSON is given error 400 is thrown
        values = data.get('values')
        if len(values) != 500:
            abort(400)
        else:
            dataList = []
            for value in values:
                if not isinstance(value, (float, int)):
                    abort(400)
                else:
                    dataList.append(float(value))
            #only overwrite memory with dataList if all the values are valid numbers
            numberList = sorted(dataList, key=float)
            return jsonify(success=True)
    if request.method == 'GET':
        return jsonify(numberList)
    if request.method == 'PATCH':
        if len(numberList) == 0:
            abort(405)
        else:
            data = request.get_json(force=True)
            value = data.get('value')
            if not isinstance(value, (float, int)):
                abort(400)
            else:
                #make space for the new number O(1) //if the number being inserted is the largest value, this will prioritize the new number being in the list, rather than inserting then popping itself out (if we want this behavior then we can pop after we sort instead)
                numberList.pop()
                #add new number 0(1)
                numberList.append(float(value))
                #sort list again O(N log N). Alternatively you can use python bisect module to do an insort(value) to insert value into already sorted list O(N) then pop the largest value.
                numberList = sorted(numberList, key=float)
                return jsonify(success=True)

if __name__ == '__main__':
    app.run(host= 'localhost', port=5000, debug=False)
import json
from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/test', methods=['POST'])
def cut_string():
    if not request.json:
        abort(400)
    i = 1
    input_string = request.json['string_to_cut']
    output_string = ''
    for char in input_string:
        if i % 3 == 0:
            output_string = output_string + char
        i += 1

    return json.dumps({"return_string": output_string})


def main():
    app.run(port=5000)


if __name__ == "__main__":
    main()

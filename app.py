from flask import Flask, request, Response, jsonify
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "BFHL API is running",
        "endpoints": {
            "POST /bfhl": "Send JSON { data: [...] } to categorize values"
        }
    })

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])
        
        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        sum_numbers = 0
        alphabet_chars = []
        
        for item in data:
            if item.isdigit():
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                sum_numbers += num
            elif item.isalpha():
                alphabets.append(item.upper())
                alphabet_chars.extend(list(item))
            else:
                special_characters.append(item)
        
        concat_string = ""
        if alphabet_chars:
            alphabet_chars.reverse()
            for i, char in enumerate(alphabet_chars):
                concat_string += char.upper() if i % 2 == 0 else char.lower()
        
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(sum_numbers),
            "concat_string": concat_string
        }

        return Response(
            json.dumps(response, indent=None, separators=(",", ":"), sort_keys=False),
            mimetype="application/json"
        )

    except Exception:
        return Response(
            json.dumps({"is_success": False, "error": "Invalid request format"}),
            mimetype="application/json",
            status=400
        )

if __name__ == '__main__':
    app.run(debug=True)

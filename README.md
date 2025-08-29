# BFHL REST API

This is a simple REST API built with Flask. It takes in an array of strings and returns a processed response. The response includes classification of numbers into odd and even, uppercased alphabets, extracted special characters, sum of numeric values, and a concatenated alternating-caps string built from the reversed sequence of letters.

The project was originally built for a take-home challenge but is generic enough to use as a reference for similar APIs.

## Using the endpoint:
Example: curl -X POST https://bajaj-finserv-health-nt0c.onrender.com/bfhl -H "Content-Type: application/json" -d "{\"data\": [\"a\", \"1\", \"334\", \"4\", \"R\", \"$\"]}"

URL: https://bajaj-finserv-health-nt0c.onrender.com/bfhl

**NOTE**: A free instance will spin down due to inactivity, which can delay requests by 50 seconds or more. Please consider that while evaluating my submission.
---

## Setup and Running Locally

1. Clone the repository  
git clone <your-repo-url>
cd <repo>

2. Create and activate a virtual environment  
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate

3. Install dependencies  
pip install -r requirements.txt

4. Run the application  
python app.py

5. Access the API at  
http://localhost:5000/bfhl

---

## Deployment Notes

This app can be hosted on Vercel, Render, or Railway. Render and Railway can directly connect to a GitHub repository and detect Python automatically. Vercel is slightly more oriented toward Node.js, but with the right configuration Flask can also be deployed there.

For the assignment, Render is a simple option that works without much extra setup.

---

## API Endpoint

Method: POST  
Route: /bfhl  
Content-Type: application/json

---

### Example Request

{
"data": ["a", "1", "334", "4", "R", "$"]
}

### Example Response

{
"is_success": true,
"user_id": "john_doe_17091999",
"email": "john@xyz.com",
"roll_number": "ABCD123",
"odd_numbers": ["1"],
"even_numbers": ["334", "4"],
"alphabets": ["A", "R"],
"special_characters": ["$"],
"sum": "339",
"concat_string": "Ra"
}

---

## Testing the API

You can use curl to send a test request:

curl -X POST http://localhost:5000/bfhl
-H "Content-Type: application/json"
-d '{"data": ["a", "1", "334", "4", "R", "$"]}'

Alternatively, Postman or Insomnia can be used to send the POST request and view the response.

---

## Important Notes

- All numbers in the response are returned as strings, as required by the specification.  
- Alphabets are uppercased in the response.  
- The concatenated string is built by reversing all alphabetic characters found in the input and applying alternating capitalization starting with uppercase.  
---

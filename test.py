import requests
import json

def test_api(url="http://localhost:5000/bfhl"):
    test_cases = [
        {
            "name": "Example A",
            "data": ["a", "1", "334", "4", "R", "$"]
        },
        {
            "name": "Example B", 
            "data": ["2", "a", "y", "4", "&", "-", "*", "5", "92", "b"]
        },
        {
            "name": "Example C",
            "data": ["A", "ABcD", "DOE"]
        }
    ]
    
    for test in test_cases:
        print(f"\n--- Testing {test['name']} ---")
        print(f"Input: {test['data']}")
        
        try:
            response = requests.post(url, json={"data": test["data"]})
            print(f"Status Code: {response.status_code}")
            print(f"Response: {json.dumps(response.json(), indent=2)}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_api()
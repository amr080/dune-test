import requests

def get_latest_result(query_id):
    url = f"https://api.dune.com/api/v1/query/{query_id}/results"
    headers = {"X-DUNE-API-KEY": "<your-api-key>"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # This will raise an exception for HTTP errors.
        return response.json()  # Return the parsed JSON response.
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

query_ids = [3097416]
results = {query_id: get_latest_result(query_id) for query_id in query_ids}

for query_id, result in results.items():
    print(f"Results for query ID {query_id}: {result}")

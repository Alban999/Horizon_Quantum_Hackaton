import requests

def extract_counts_from_response(response_text):
    # Find the start and end indices of the "meas_outcomes" array
    meas_outcomes_str = response_text.split('meas_outcomes')[1]

    # Count occurrences of '["0"]' and '["1"]' in the substring
    count_0 = meas_outcomes_str.count('0')
    count_1 = meas_outcomes_str.count('1')

    return count_0, count_1

def get_results_from_api(url, api_key, job_id):
    headers = {
        'X-Api-Key': api_key,
        'Content-Type': 'application/json',
    }

    data = {
        'job_id': job_id,
        'inputs': [['a', '1'], ['b', '1']],
    }

    response = requests.post(url, headers=headers, json=data)
    
    count_0, count_1 = extract_counts_from_response(response.text)
    
    return {'0': count_0, '1': count_1}

# Example usage
url = input("url: ")
api_key = input("api_key: ")
job_id = input("job_id: ")


result_counts = get_results_from_api(url, api_key, job_id)
print(result_counts)

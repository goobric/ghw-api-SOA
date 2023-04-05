import requests

# Set up parameters for API request
params = {
    'order': 'desc',
    'sort': 'votes',
    'site': 'stackoverflow'
}

# Make API request to get top questions
response = requests.get('https://api.stackexchange.com/2.3/questions', params=params)

# Check if request was successful
if response.status_code == 200:
    # Get list of questions from response JSON
    questions = response.json()['items']

    # Print titles of top questions
    for question in questions:
        print(question['title'])
else:
    print('Error: API request failed.')
    
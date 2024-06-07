import requests

def lambda_handler(event, context):
<<<<<<< HEAD
    url = "https://api.quotable.io/random"
    response = requests.get(url)

    if response.status_code == 200:
        quote_data = response.json()
        content = quote_data.get("content")
        author = quote_data.get("author")
        print(f"Random Quote: '{content}' - {author}")
        print("v1.1")
    else:
        print(f"Failed to retrieve a random quote. Status code: {response.status_code}")
=======
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World from Lambda and Testing CodeBuild_test!')
    }
>>>>>>> c4a31557db6f9a0bbc0ee0b78b7a77cc9b79d191

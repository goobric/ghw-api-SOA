# ghw-api-SOA

## Retreive data from Stack Overflow API

In this app, library requests are used to make an API request to the Stack Overflow API. We set up parameters to specify the order and sorting of the questions, as well as the site we want to retrieve data from.

We then make the API request using the requests.get() method and check if the request was successful. If it was, we extract the list of questions from the response JSON using the response.json() method and print out the titles of the top questions.

Note that this is just a basic example and you can modify the parameters to retrieve different data from the API. Also, you may need to register for an API key to make requests to the Stack Overflow API.

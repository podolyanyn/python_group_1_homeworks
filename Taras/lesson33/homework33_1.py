import requests

url1 = 'https://uk.wikipedia.org/robots.txt'
url2 = 'https://twitter.com/robots.txt'
response = requests.get(url1)  # perform an HTTP GET request to the URL url1 and save the received response
response2 = requests.get(url2)  # perform an HTTP GET request to the URL url2 and save the received response
if response.status_code == 200:  # check whether the response code status is equal to 200, which means a successful
    # request
    content = response.text  # save the text content of the answer
    with open('robots_wiki.txt', 'wb') as file1:  # open the file in recording mode as a binary file
        file1.write(response.content)  # write down the content of the answer
        print("file downloaded and saved successfully.")
else:  # if the response code status is not equal to 200, then we output the following statement
    print("Failed to download file.")
if response2.status_code == 200:  # check whether the response code status is equal to 200, which means a successful
    # request
    content2 = response2.text  # save the text content of the answer
    with open('robots_twitter.txt', 'wb') as file2:  # open the file in recording mode as a binary file
        file2.write(response2.content)  # write down the content of the answer
        print("file downloaded and saved successfully.")
else:  # if the response code status is not equal to 200, then we output the following statement
    print("Failed to download file.")








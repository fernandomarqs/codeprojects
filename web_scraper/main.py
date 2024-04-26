import requests
from bs4 import BeautifulSoup

#TODO: error handling

def get_information(response):
    # function that gets the contents from the desired URL. returns the title and body of its content as strings

    #status_code = 200 is success; if its anything different, we had an error trying to read the page
    if response.status_code == 200:
        parser = BeautifulSoup(response.content, 'html.parser')

        title = parser.find('h1').get_text() #in html, the title is in the div <h1>

        paragraphs = parser.find_all('p') #gets all the paragraphs that are on the <p> divs

        index = 0

        #in order to ignore disclaimer paragraphs that are not relevant to us, we check the size of the paragraphs and only start on a paragraph that is >= 100 in size
        for i, paragraph in enumerate(paragraphs):
            if len(paragraph.get_text()) >= 100:
                index = i
                break

        #make the paragraphs list only start at the desired index after the disclaimers
        paragraphs = paragraphs[index:]

        #join the text of all paragraphs divided by a '\n'
        body = '\n'.join([paragraph.get_text() for paragraph in paragraphs])

        return title, body
    else:
        print(f"\nFailed to retrieve the data of the page. Error code: {response.status_code}")

        return None, None

    

url = input('Input the URL you wish to get informations from:\n')


response = requests.get(url)

title, body = get_information(response)

if title and body:
    print('\n' + title + '\n')
    print(body)
else:
    print('\nCould not properly access the data of that URL. Try again!')


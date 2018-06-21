from bs4 import BeautifulSoup
import requests

# ***************  Function for Extracting Images  ***************
def extractImg(page_content):
    # extract all img elements from html file
    imageTags = page_content.find_all('img', src=True)
    images = []

    # Img elements example:
    # <img height="1" src="https://www.facebook.com/tr?id=130492214192672&amp;ev=PageView&amp;noscript=1" style="display:none" width="1"/>
    # image url extracted example:
    # https://www.facebook.com/tr?id=130492214192672&ev=PageView&noscript=1

    # extract image url from img elements
    for img in imageTags:
        images.append(img.get('src'))

    # Remove duplicates from list with set
    imagesSet = list(set(images))
    print("The number of images extracted: ", len(imagesSet))

    # put the results into an easily searchable index file
    imgfile = open('images.txt', 'w')
    for img in imagesSet:
        imgfile.write("%s\n" % img)
    imgfile.close()

# ***************  Function for Extracting Links  ***************
def extractLinks(page_content):
    # extract all link elements from html file
    linkTags = page_content.find_all('a', href=True)
    links = []

    # Link elements example:
    # <a class="nav-menu-links__link" data-analytics-header="main-menu_money" href="http://money.cnn.com">Money</a>
    # Link url extracted example:
    # http://money.cnn.com

    # extract link url from img elements
    for link in linkTags:
        links.append(link.get('href'))

    # Remove duplicates from list with set
    linksSet = list(set(links))
    print("The number of links extracted: ", len(linksSet))

    # put the results into an easily searchable index file
    linkfile = open('links.txt', 'w')
    for link in linksSet:
        linkfile.write("%s\n" % link)
    linkfile.close()

def http_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, timeout=5)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)

def log_error(e):
    """
    It is always a good idea to log errors.
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def pageScraper():
    print("************************** Page Scraper **************************")
    print("Welcome to Zhuangzhuang's final project for CISC504LSP18")
    # Input the site you'd like to search content:
    page_link = 'https://www.cnn.com/'
    print("The site you searched is: ", page_link)

    # fetch the content from url
    page_response = requests.get(page_link, timeout=5)
    # parse html with BeautifulSoup
    page_content = BeautifulSoup(page_response.content, "html.parser")

    extractImg(page_content)
    extractLinks(page_content)

pageScraper()
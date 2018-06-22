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

def pageScraper():
    print("************************** Page Scraper **************************")
    print("Welcome to Zhuangzhuang's final project for CISC504LSP18")
    # Input the site you'd like to search content:
    pageLink = 'https://www.cnn.com/'
    # Few other websites for example:
    # pageLink = 'https://www.apple.com/'
    # pageLink = 'https://www.pinterest.com/'
    # pageLink = 'https://www.nytimes.com/'

    print("The site you searched is: ", pageLink)

    # fetch the content from url
    pageResponse = requests.get(pageLink, timeout=5)
    if pageResponse.status_code == requests.codes.ok:
        print("Extract content success!", pageResponse.status_code)
        # parse html with BeautifulSoup
        pageContent = BeautifulSoup(pageResponse.content, "html.parser")
        extractImg(pageContent)
        extractLinks(pageContent)
    else:
        print("Failed to extract content. Error code: " + pageResponse.status_code + ", please contact support for troubleshooting")
        pageResponse.raise_for_status()

pageScraper()
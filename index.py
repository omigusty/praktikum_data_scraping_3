import requests
from bs4 import BeautifulSoup
import function


def mainScraper(url, directory):
    function.createDirectory(directory)
    urlTarget = requests.get(url)
    beautify = BeautifulSoup(urlTarget.content, "html.parser")
    getContent = beautify.find_all("div", class_="box-item")

    for news in getContent:
        getThumbnail = news.find(
            "img", class_="attachment-medium size-medium wp-post-image")
        thumbnail = getThumbnail["src"]
        getCategory = news.find("span", class_="cat-links-content").text
        getDate = news.find("time", class_="entry-date published updated").text
        getTitle = news.find("h2", class_="entry-title").text
        getParentContent = news.find(
            "div", class_="entry-content entry-content-archive")
        getContent = getParentContent.find("p").text
        print()

        articleFormat = "Judul berita: " + getTitle + "\n" + "Thumbnail: " + thumbnail + "\n" + "Kategori: " + getCategory + "\n" + "Tanggal: " + getDate + "\n" + "Isi berita: " + getContent + "\n"

        if function.doesFileExist(directory + "/article.doc") is False:
            function.createNewFile(directory + "/article.doc")

        function.writeToFile(directory + "/article.doc", articleFormat)
        print(articleFormat)


mainScraper("https://www.kabarbanyuwangi.info/", "result")

import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


if __name__  == "__main__":
    url = "https://movie.douban.com/cinema/later/chengdu/"
    res = requests.get(url)
    file = open("douban.html","w")
    file.write(res.content.decode("utf-8"))
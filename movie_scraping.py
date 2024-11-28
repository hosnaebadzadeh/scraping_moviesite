import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from translate import Translator


driver = webdriver.Firefox()
driver.get("https://www.film2movie.asia/")

type = input("Are you looking for a movie or a series? ")


name = input("Enter the name of the movie/series in any language: ")

translator = Translator(to_lang="en")
translated_name = translator.translate(name)


search_box = driver.find_element(By.CSS_SELECTOR, ".search input")
search_box.send_keys(translated_name, Keys.ENTER)


search_url = driver.current_url + "search/" + translated_name
driver.get(search_url)



if type == "movie":
    quality = input("Which quality do you want?: ")
    movie = "فیلم"
    articles = driver.find_elements(By.TAG_NAME, "article")

    for article in articles:
        title = article.find_element(By.CLASS_NAME, "title").text
        if title.casefold().__contains__(translated_name.casefold()) and title.casefold().__contains__(movie.casefold()) :
            print(f"Found: {title}")

    finalres = input("Which one is your choice? ").casefold()

    for article in articles:
        title = article.find_element(By.CLASS_NAME, "title").text
        if title.casefold() == finalres:
            article.find_element(By.TAG_NAME, "a").click()
            break



    movie_article = driver.find_element(By.TAG_NAME, "article")
    movie_all_links = movie_article.find_elements(By.LINK_TEXT, "لینک مستقیم")
    print(f"Available links for {translated_name} with quality {quality}:")
    for link in movie_all_links:
        href = link.get_attribute("href")
        if translated_name.casefold() in href.casefold() and quality.casefold() in href.casefold():
            print(href)

elif type == "series":

    articles = driver.find_elements(By.TAG_NAME, "article")
    series = "سریال"
    for article in articles:
        title = article.find_element(By.CLASS_NAME, "title").text
        if title.casefold().__contains__(translated_name.casefold()) and title.casefold().__contains__(series.casefold()):
            print(f"Found: {title}")

    finalres = input("Which one is your choice? ").casefold()

    for article in articles:
        title = article.find_element(By.CLASS_NAME, "title").text
        if title.casefold() == finalres:
            article.find_element(By.TAG_NAME, "a").click()



    series_article = driver.find_element(By.TAG_NAME,"article")
    series_all_links = series_article.find_elements(By.LINK_TEXT, "لینک مستقیم")
    print(f"Available links for{finalres}:")
    for link in series_all_links:
        href = link.get_attribute("href")
        print(href)


else:
    print("try another!")


time.sleep(120)
driver.quit()
# translate movie or series name to english
# just show the results for the type you want
# you can choose between results
# you can choose quality only for movies


#https://github.com/hosnaebadzadeh
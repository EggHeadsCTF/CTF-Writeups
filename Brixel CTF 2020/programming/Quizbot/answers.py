import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  

url = 'http://timesink.be/quizbot/index.php'
path = 'chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(url)

num = 0
while num < 1000 :
    num = num + 1
    searchbar = driver.find_element_by_xpath('//*[@type="text"]')
    searchbar.send_keys("junk")
    searchbar.send_keys(Keys.RETURN)
    answer = driver.find_element_by_xpath('//*[@id="answer"]')
    fd = open('answers.txt',"a+")
    fd.write(str(answer.text) + "\n" )
    fd.close()
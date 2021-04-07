import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  

f = open('answers.txt')
l = [f.readline()]
while len(l) < 1000:
    l.append(f.readline())

l = [s.strip('\n') for s in l]
print(l)


url = 'http://timesink.be/quizbot/index.php'
path = 'chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(url)

num = 0
while num < 1000 :
    searchbar = driver.find_element_by_xpath('//*[@id="insert_answer"]')
    searchbar.send_keys("{}".format(l[num]))
    searchbar.send_keys(Keys.RETURN)
    num = num + 1

fd.close()
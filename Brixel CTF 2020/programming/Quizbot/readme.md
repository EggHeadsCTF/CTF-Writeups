# Quizbot

Brixel CTF 2020

>Legend has it there's a flag at the end when you have a perfect score
>
>http://timesink.be/quizbot

I tried to beat the timer, but I was always at 1 second. So lets make a script to get all of the answers automatically. I used a selenium base from a source I found online. 

> <https://www.guru99.com/selenium-python.html>

Once we got all of the answers, its time to modify the script to post all of the answers. Get all the answers into an array with a variable and then push it into the input field and press enter.

```python
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
```

This is our flag.

> brixelCTF{kn0wl3dg3}
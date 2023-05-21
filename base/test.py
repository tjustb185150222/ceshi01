from selenium import webdriver
from selenium.webdriver.common.by import By


class Baset():

    def url(self):
        driver = webdriver.Chrome()
        driver.get('http://localhost:8090')
        self.t1 = driver.find_element(By.XPATH,'/html/body/div[1]/h2').text
        return self.t1
if __name__ == '__main__':
    x = Baset()
    t = x.url()
    print(t)




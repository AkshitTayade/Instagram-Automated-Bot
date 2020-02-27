from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class Instabot :
    def __init__(self, username, password) :
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome("./chromedriver")
        self.login()

    def login(self) :
        self.driver.get('https://instagram.com/accounts/login')
        sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password )
        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
        sleep(3) 
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()
        sleep(1)
        

# navigates the user and then follows them
    def user_navigate(self,user_to_find) :
        sleep(2)
        self.driver.get('https://instagram.com/' + user_to_find)
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(),'Follow')]").click()
        sleep(3)
        


    def like_user_post(self, user):
        self.user_navigate(user)
        
        post = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[1]/span/span').text
        
        self.driver.find_elements_by_class_name('eLAPa')[0].click()
        sleep(2)

        for i in range(1,int(post)):

            
            #if(self.driver.find_elements_by_tag_name('aria-label') == 'Like')[2]:
            self.driver.find_elements_by_class_name('wpO6b')[1].click()
            sleep(1)
            self.driver.find_element_by_xpath("//a[contains(text(),'Next')]").click()
            sleep(1)

        self.driver.find_elements_by_xpath("/html/body/div[4]/div[3]/button")[0].click()
        sleep(2)

    def unfollow_user(self):
        self.driver.find_elements_by_xpath("//button[contains(text(),'Following')]")[0].click()
        sleep(2)
        abc = self.driver.find_elements_by_xpath("//button[contains(text(),'Unfollow')]")[0]
        abc.click()
        sleep(5)
       


    def close_selenium(self):
        self.driver.close()



bot = Instabot('abcd','xyz')

#bot.user_navigate('nature_climax')
bot.like_user_post('nature_climax')
bot.unfollow_user()
bot.close_selenium()

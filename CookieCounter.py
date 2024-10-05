

from selenium import webdriver

PATH = "chromedriver.exe"  # Ensure this is the correct path
driver = webdriver.Chrome(PATH)
driver.get("https://demo.automationtesting.in/Register.html")

cookie=driver.find_element_by_id("bigCookie")
cookie_count=driver.find_element_by_id("cookies")
items=[driver.find_element_by_id("productPrice"+str(i)) for i in range(1,-1,-1)]

actions=webdriver.ActionChains(driver)
actions.click(cookie)


for i in range(5000):
    actions.perform()
    count= int(cookie_count.text.split("")[0])
    print(count)
    
    for item in items:
        value=int(item.text)
        if value <=count:
            upgrade_actions=webdriver.ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
    
    
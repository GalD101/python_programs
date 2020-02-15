from selenium import webdriver
driver_path = r'C:\GD\python_programs\Selenium_driver\chromedriver'
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
mobile_emulation = {"deviceName": "Nexus 5"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
chrome_options.add_argument("--headless")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=driver_path, options=options, chrome_options=chrome_options)
driver.get('http://avivitagamdali.co.il/')
driver.get_screenshot_as_file(r'C:\Users\User\Desktop\n.png')
driver.close()

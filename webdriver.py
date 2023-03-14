from selenium import webdriver 
# selenium 4.4.3, chrome Version 111.0.5563.64 (Official Build) (arm64), 
# webdriver ETag ad0af4333c36933b984a7edeb2647d46 mac_arm64 version of the chrome driver

# set the path of your executable here
chrome_driver_executable_path = '/Users/yameen/Projects/python/chess bot/chromedriver'

our_options = webdriver.ChromeOptions()
our_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options = our_options, executable_path=chrome_driver_executable_path)
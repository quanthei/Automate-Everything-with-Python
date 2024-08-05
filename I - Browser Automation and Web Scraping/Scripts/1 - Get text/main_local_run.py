from selenium import webdriver
from selenium.webdriver.chrome.service import Service

DRIVER_LOCAL_PATH = "C:\\Users\\Thomas\\Desktop\\Formation Python\\Web scraping\\chromedriver.exe"
service = Service(DRIVER_LOCAL_PATH)

#----------------------------FUNCTIONS----------------------------  
def get_driver(url_to_get: str, run_locally: bool = True, keep_alive_browser: bool = False):
    while True:
        # Handle empty URL
        if url_to_get == "": 
            handle_url_error(url_to_get)
            break # we break the loop

        # Parametrization of the Webdriver
    
        # Options
        driver_options = webdriver.ChromeOptions()

        # General options
        driver_options.add_argument("start-maximized") # start the browser as FS
        driver_options.add_argument("disable-infobars") # disable infobars
        driver_options.add_argument("disable-dev-shm-usage") # avoid issues when running script on linux (replit machines are linux)
        driver_options.add_argument("no-sandbox") # provide more priviledges for scrapping
        driver_options.add_argument("disable-blink-features=AutomationControlled") # help bypass script detection and blocking from the webservice

        # Experimental options
        driver_options.add_experimental_option("excludeSwitches", ["enable-automation"]) # help bypass script detection and blocking from the webservice

        # Attribute args to Webdriver
        if not run_locally: # run on an online IDE (replit for example)
            driver = webdriver.Chrome(options=driver_options, keep_alive=keep_alive_browser)
        else: # run a local IDE
             driver = webdriver.Chrome(service=service, options=driver_options, keep_alive=keep_alive_browser)   
        # Run Webriver
        driver.get(url_to_get)

        return driver # return the driver

def handle_url_error(url_error: str) -> str:
    if url_error == "":
        return "ERROR: The URL is empty!"
    return f"ERROR: '{url_error}' is an invalid URL!"

#----------------------------MAIN----------------------------
def main():
    # URLs to scrape
    URL_to_scrape = ["https://www.scrapethissite.com/pages/simple/"]

    # Get driver
    for url in URL_to_scrape:
        driver = get_driver(url, keep_alive_browser= True)
        element = driver.find_element(by="xpath", value="/html/body/div/section/div/div[1]/div/h1")
    print(element.text)

#----------------------------EXE----------------------------
main()

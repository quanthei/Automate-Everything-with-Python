from selenium import webdriver

#----------------------------FUNCTIONS----------------------------
def get_driver(url_to_get: str, to_keep_alive: bool = False):
    while True:
        # Handle empty URL
        if url_to_get == "": 
            handle_url_error(url_to_get)
            break # we break the loop

        # Parametrization of the Webdriver

        #Options
        driver_options = webdriver.ChromeOptions()

        # General options
        driver_options.add_argument("start-maximized") # start the browser as FS
        driver_options.add_argument("disable-infobars") # disable infobars
        driver_options.add_argument("disable-dev-shm-usage") # avoid issues when running script on linux (replit machines are linux)
        driver_options.add_argument("no-sandbox") # provide more priviledges for scrapping
        driver_options.add_argument("disable-blink-features=AutomationControlled") # help bypass script detection and blocking from the webservice

        # Experimental options
        driver_options.add_experimental_option("excludeSwitches", ["enable-automation"]) # help bypass script detection and blocking from the webservice

        # Services // None for now
        driver_services = webdriver.ChromeService()

        # Attribute args to Webdriver
        driver = webdriver.Chrome(driver_options, driver_services, to_keep_alive)

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
        driver = get_driver(url, True)
        element = driver.find_element(by="xpath", value="/html/body/div/section/div/div[1]/div/h1")
    print(element.text)

#----------------------------EXE----------------------------
main()
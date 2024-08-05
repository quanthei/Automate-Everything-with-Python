from selenium import webdriver

def set_webdriver(to_keep_alive: bool = False):
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

    # Run Webdriver
    driver = webdriver.Chrome(driver_options, driver_services, to_keep_alive)



from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

WEBDRIVER_EXE_PATH = "./assets/chromedriver.exe"
RESULT_PAGE_URL = "https://www.doenets.lk/examresults"


def launch_result_page(index_no: int):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(RESULT_PAGE_URL)

    exam_select = Select(
        driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[3]/div[1]/div/div[1]/div/select",
        )
    )

    exam_query_string = "(O/L)"
    exam_year = "2021"

    for option in exam_select.options:
        if exam_query_string in option.text:
            exam_select.select_by_visible_text(option.text)
            break

    exam_year_select = Select(
        driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[3]/div[1]/div/div[2]/div/select",
        )
    )

    for option in exam_year_select.options:
        if exam_year in option.text:
            exam_year_select.select_by_visible_text(option.text)
            break

    index_input = driver.find_element(
        By.XPATH,
        "/html/body/app-root/div/app-layout-horizontal-sidenav/div/div/div/div/div/app-exam-results-container/app-exam-results/div[1]/div/div[2]/div[3]/div[2]/div/div/input",
    )
    index_input.send_keys(index_no)

    # sleep(100)

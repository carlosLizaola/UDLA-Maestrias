import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UdlaTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_newLeadApplication(self):
        driver = self.driver
        driver.get("https://aplatamqa.com/portal-alumno/login?schoolId=24")
        driver.maximize_window()

        driver.find_element(By.LINK_TEXT, 'Registrarse').click()

        selectCurrentTypeAccount = driver.find_element(By.CSS_SELECTOR, 'select[formcontrolname="currentTypeAccount"]')
        currentTypeAccount = Select(selectCurrentTypeAccount)
        currentTypeAccount.select_by_visible_text("UDLA MAESTRÍAS")

        email = driver.find_element(By.CSS_SELECTOR, 'input[formcontrolname="email"]')
        email.send_keys("test.2024120102@aplatam.test")

        password = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="password"]')))
        password.send_keys("Test.123")

        confirmPassword = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="confirmPassword"]')))
        confirmPassword.send_keys("Test.123")

        name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="name"]')))
        name.send_keys("Antonio")

        secondName = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="secondName"]')))
        secondName.send_keys("Pedro")

        lastName = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="lastName"]')))
        lastName.send_keys("Ramirez")

        secondlastName = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="secondLastName"]')))
        secondlastName.send_keys("Lopez")

        phone = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[formcontrolname="phone"]')))
        phone.send_keys("5578451245")

        selectCountry = driver.find_element(By.CSS_SELECTOR, 'select[formcontrolname="country"]')
        country = Select(selectCountry)
        country.select_by_visible_text("Ecuador")

        selectProgram = driver.find_element(By.CSS_SELECTOR, 'select[formcontrolname="program"]')
        program = Select(selectProgram)
        program.select_by_visible_text("Maestría en Inteligencia de Negocios y Ciencia de Datos")

        selectDegree = driver.find_element(By.CSS_SELECTOR, 'select[formcontrolname="degree"]')
        degree = Select(selectDegree)
        degree.select_by_visible_text("Profesional Tercer Nivel")

        driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary btn-block"]').click()

        driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-md btn-primary btn-round"]').click()

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//iframe")))
        driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe"))

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//select[@id='PERSONAL_DATA_countryDoc']")))
        selectCountryDoc = driver.find_element(By.XPATH, "//select[@id='PERSONAL_DATA_countryDoc']")
        countryDoc = Select(selectCountryDoc)
        countryDoc.select_by_visible_text("México")

        documentNumber = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="PERSONAL_DATA_documentNumber"]')))
        documentNumber.send_keys("2024110705")

        selectBirthCountry = driver.find_element(By.CSS_SELECTOR, 'select[id="PERSONAL_DATA_birthCountry"]')
        birthCountry = Select(selectBirthCountry)
        birthCountry.select_by_visible_text("México")

        driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-outline-secondary fa fa-calendar"]').click()

        selectYear = driver.find_element(By.CSS_SELECTOR, 'select[title="Select year"]')
        year = Select(selectYear)
        year.select_by_visible_text("2000")

        driver.find_element(By.CSS_SELECTOR, 'div[class="btn-light ng-star-inserted"]').click()

        selectHandicap = driver.find_element(By.CSS_SELECTOR, 'select[id="PERSONAL_DATA_hasHandicap"]')
        handicap = Select(selectHandicap)
        handicap.select_by_visible_text("No")

        driver.find_element(By.CSS_SELECTOR, 'button[class="mat-stepper-next btn btn-info float-right"]').click()

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="CONTACT_DATA_street"]')))
        street = driver.find_element(By.CSS_SELECTOR, 'input[id="CONTACT_DATA_street"]')
        street.send_keys("Prueba")

        addressNumber = driver.find_element(By.CSS_SELECTOR, 'input[id="CONTACT_DATA_noExt"]')
        addressNumber.send_keys("1")

        secondStreet = driver.find_element(By.CSS_SELECTOR, 'input[id="CONTACT_DATA_noInt"]')
        secondStreet.send_keys("Prueba")

        homePhone = driver.find_element(By.CSS_SELECTOR, 'input[id="CONTACT_DATA_phone"]')
        homePhone.send_keys("5578451245")

        driver.find_element(By.XPATH, "(//button[@type='button'])[4]").click()

        selectTaxRegimeType = driver.find_element(By.CSS_SELECTOR, 'select[id="BILLING_DATA_taxRegimeType"]')
        taxRegimeType = Select(selectTaxRegimeType)
        time.sleep(1)
        taxRegimeType.select_by_visible_text("Persona natural")

        documentNumber2 = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="BILLING_DATA_documentNumber"]')))
        documentNumber2.send_keys("2024110705")

        name = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="BILLING_DATA_firstName"]')))
        name.send_keys("Antonio")

        lastName = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="BILLING_DATA_firstLastName"]')))
        lastName.send_keys("Ramirez")

        secondLastName = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="BILLING_DATA_secondLastName"]')))
        secondLastName.send_keys("Lopez")

        phone = driver.find_element(By.CSS_SELECTOR, 'input[id="BILLING_DATA_phone"]')
        phone.send_keys("5578451245")

        email = driver.find_element(By.CSS_SELECTOR, 'input[id="BILLING_DATA_email"]')
        email.send_keys("prueba@prueba.com")

        street2 = driver.find_element(By.CSS_SELECTOR, 'input[id="BILLING_DATA_street"]')
        street2.send_keys("Prueba")

        addressNumber2 = driver.find_element(By.CSS_SELECTOR, 'input[id="BILLING_DATA_noExt"]')
        addressNumber2.send_keys("1")

        secondStreet2 = driver.find_element(By.CSS_SELECTOR, 'input[id="BILLING_DATA_noInt"]')
        secondStreet2.send_keys("Prueba")

        selectBillingCountry = driver.find_element(By.CSS_SELECTOR, 'select[id="BILLING_DATA_country"]')
        billingCountry = Select(selectBillingCountry)
        billingCountry.select_by_visible_text("México")

        driver.find_element(By.XPATH, "(//button[@type='button'])[6]").click()

        highSchool = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="ACADEMIC_DATA_highSchool"]')))
        highSchool.send_keys("Colegio")
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[id="ngb-typeahead-0-0"]').click()

        driver.find_element(By.XPATH, "(//button[@type='button'])[7]").click()

        selectYear2 = driver.find_element(By.CSS_SELECTOR, 'select[title="Select year"]')
        year2 = Select(selectYear2)
        year2.select_by_visible_text("2016")

        driver.find_element(By.CSS_SELECTOR, 'div[class="btn-light ng-star-inserted"]').click()

        college = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="ACADEMIC_DATA_university"]')))
        college.send_keys("Universidad")
        time.sleep(1)

        driver.find_element(By.CSS_SELECTOR, 'button[class="dropdown-item ng-star-inserted"]').click()

        driver.find_element(By.XPATH, "(//button[@type='button'])[8]").click()

        selectYear3 = driver.find_element(By.CSS_SELECTOR, 'select[title="Select year"]')
        year3 = Select(selectYear3)
        year3.select_by_visible_text("2024")

        selectMonth3 = driver.find_element(By.XPATH, "//select[contains(@aria-label,'Select month')]")
        month3 = Select(selectMonth3)
        month3.select_by_visible_text("Octubre")

        driver.find_element(By.XPATH, "(//div[contains(.,'1')])[31]").click()

        otherStudy = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[id="ACADEMIC_DATA_otherStudy"]')))
        otherStudy.send_keys("No")

        driver.find_element(By.XPATH, "(//button[@type='button'])[10]").click()
        time.sleep(1)

        selectHasJob = driver.find_element(By.CSS_SELECTOR, 'select[id="JOB_DATA_hasJob"]')
        hasJob = Select(selectHasJob)
        hasJob.select_by_visible_text("No")

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//label[@for='acceptTerms0']")))
        driver.find_element(By.XPATH, "//label[@for='acceptTerms0']").click()

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='button'][contains(.,'Guardar Solicitud')]")))
        driver.find_element(By.XPATH, "//button[@type='button'][contains(.,'Guardar Solicitud')]").click()

        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "(//button[@type='button'])[15]")))
        driver.find_element(By.XPATH, "(//button[@type='button'])[15]").click()
        time.sleep(2)

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[14]")))
        driver.find_element(By.XPATH, "(//button[@type='button'])[14]").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__=="__main__":
    unittest.main()

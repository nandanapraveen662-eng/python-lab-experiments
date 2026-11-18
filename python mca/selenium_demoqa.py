
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create Chrome browser
driver = webdriver.Chrome()

try:
    # Open DemoQA Text Box webpage
    driver.get("https://demoqa.com/text-box")

    # Maximize browser window
    driver.maximize_window()

    # Wait for webpage elements
    wait = WebDriverWait(driver, 15)

    # User details
    name = "Nandana A P"
    email = "nandanaap12@gmail.com"
    current_address = "Thrissur, Kerala"
    permanent_address = "Thrissur, Kerala"

    # Enter Full Name
    name_box = wait.until(
        EC.visibility_of_element_located((By.ID, "userName"))
    )
    name_box.send_keys(name)

    # Enter Email
    email_box = driver.find_element(By.ID, "userEmail")
    email_box.send_keys(email)

    # Enter Current Address
    current_box = driver.find_element(By.ID, "currentAddress")
    current_box.send_keys(current_address)

    # Enter Permanent Address
    permanent_box = driver.find_element(By.ID, "permanentAddress")
    permanent_box.send_keys(permanent_address)

    # Click Submit button
    submit_button = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].click();", submit_button)

    # Wait for output section
    output = wait.until(
        EC.visibility_of_element_located((By.ID, "output"))
    )

    # Retrieve submitted details
    output_name = output.find_element(
        By.ID, "name"
    ).text

    output_email = output.find_element(
        By.ID, "email"
    ).text

    output_current = output.find_element(
        By.ID, "currentAddress"
    ).text

    output_permanent = output.find_element(
        By.ID, "permanentAddress"
    ).text

    # Display submitted details
    print("\nSubmitted Details:")
    print(output_name)
    print(output_email)
    print("Current Address:", output_current)
    print("Permanent Address:", output_permanent)

    # Verify entered details
    if (output_name == "Name:" + name and
        output_email == "Email:" + email and
        output_current == "Current Address :" + current_address and
        output_permanent == "Permananet Address :" + permanent_address):

        print("\nForm submitted successfully!")
        print("All details verified correctly.")

    else:
        print("\nVerification failed!")

finally:
    # Close browser
    driver.quit()

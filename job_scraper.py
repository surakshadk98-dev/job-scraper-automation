from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Start browser
driver = webdriver.Chrome()

# Open Indeed
driver.get("https://www.indeed.com")

time.sleep(3)

# Enter job title
job_box = driver.find_element(By.ID, "text-input-what")
job_box.send_keys("Java Developer")

# Enter location
location_box = driver.find_element(By.ID, "text-input-where")
location_box.clear()
location_box.send_keys("India")
location_box.send_keys(Keys.RETURN)

time.sleep(5)

jobs = []

# Get job cards
job_cards = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")

for job in job_cards:
    try:
        title = job.find_element(By.TAG_NAME, "h2").text
        company = job.find_element(By.CLASS_NAME, "companyName").text
        location = job.find_element(By.CLASS_NAME, "companyLocation").text

        jobs.append({
            "Title": title,
            "Company": company,
            "Location": location
        })
    except:
        continue

# Save results
df = pd.DataFrame(jobs)
df.to_csv("jobs.csv", index=False)

print("✅ Jobs saved to jobs.csv")

driver.quit()

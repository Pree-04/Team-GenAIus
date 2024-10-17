from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Step 1: Setup WebDriver options (optional - for headless mode)
options = Options()
options.headless = True

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Step 2: Ask the user for multiple URLs
urls = input("Enter the URLs separated by commas: ").split(',')

# Step 3: Loop through each URL and extract the HTML content
for idx, url in enumerate(urls):
    url = url.strip()  # Clean any extra spaces
    driver.get(url)
    
    # Extract the HTML content
    html_content = driver.page_source
    
    # Create a filename based on the index or URL
    filename = f"C:/Users/mahan/OneDrive/Desktop/GenAIus/Files/HTMLtext/html_{idx+1}.txt"
    
    # Save the HTML content to a file
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    
    print(f"Extraction of HTML content for {url} is done and saved as {filename}")

# Step 4: Close the driver
driver.quit()
print("All URLs processed and extraction is complete.")

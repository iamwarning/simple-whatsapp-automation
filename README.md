# Whatsapp Automation


### Installation

To run the script, you must first have [Selenium](https://pypi.org/project/selenium/)  installed.

Open the terminal and run the following command:

```bash
pip install selenium
```
### Plugins
After installing Selenium, a webdriver is required to be able to perform the automation tests in our preferred browser. Once the driver corresponding to the browser that we will use is downloaded, we proceed to save it in the path where our python script is located. Before executing the script, we must first change the target that would be the name of the contact to whom we want to send a message, then we modify the string that is the message we will send.

```python
#Path where the webdriver is located
browser = webdriver.Chrome("/home/baos/Documents/Python/WhatsApp Automation/./chromedriver")

target = '" _user_ "' #Contact name
string = " _message_ " #Custom message  
x_arg = '//span[contains(@title, ' + target + ')]'
target = wait.until(ec.presence_of_element_located((By.XPATH, x_arg)))
target.click()
```

PD: The script is made to work with Chrome in version 81. The links of the browsers with which automation can be performed are attached.

| Browser | Driver |
| ------ | ------ |
| Chrome | [Webdriver](https://chromedriver.chromium.org/downloads) |
| Mozilla | [Webdriver](https://developer.mozilla.org/en-US/docs/Web/WebDriver) |
| Safari | [Webdriver](https://developer.apple.com/documentation/webkit/testing_with_webdriver_in_safari) |

Made the changes, we simply have to execute in the terminal the command:
```bash
python3 Whatsapp.py 
```
It will open a browser window and show the WhatsApp page. We scan the qr code with our mobile device to be able to access the messages and we simply observe the magic.

License
----

MIT


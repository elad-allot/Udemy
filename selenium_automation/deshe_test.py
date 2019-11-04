from selenium import webdriver


manage_url = "https://deshe.matrix.co.il/deshe/Pages/HoursReportManagement.aspx"
base_url = "https://desheTwingo90.matrix.co.il/deshe/Pages/invisibleDeleteFrame.aspx?AutoID=%d"
user = 'eladlevy'
pwd = 'Cyp4life'


chrome = webdriver.Chrome(executable_path="""C:\Program Files\ChromeDriver\chromedriver78.exe""")
chrome.get("http://deshe.matrix.co.il/deshe/Pages/HoursReportManagement.aspx")


# chrome.find_element_by_link_text("Sign in").find_element("Username", user)
# chrome.find_element_by_link_text("Sign in").find_element("Password", pwd)
#
# el = chrome.find_element("Sing in")
# el.text

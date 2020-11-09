# Import Python Packages
import smtplib
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()
driver.get("https://ourauckland.aucklandcouncil.govt.nz/news/")

latestLinks = []
todayLinks = []
relatedLinks = []
relatedWords = ['Real Estate', 'Property', 'Investment', 'Home']


for i in range(1, 11):
    elems = driver.find_element_by_css_selector("#ns-dynamic-grid > div:nth-child(" + str(i) + ') > div > h3 > a')
    # elems = driver.find_element_by_css_selector("#ns-dynamic-grid > div:nth-child(1) > div > h3 > a")
    print(elems.get_attribute('href'))
    latestLinks.append(elems.get_attribute('href'))


for latestLink in latestLinks:
    subDriver = webdriver.PhantomJS()
    subDriver.get(latestLink)

    time.sleep(3)
    date = subDriver.find_element_by_css_selector("body > div > div.uk-container.uk-container-center.ns-single-page-wrapper.ns-single-page-news > div > div.ns-single-page.uk-width-large-3-4 > div:nth-child(2) > div > span")
    if date.text.split(':')[1] != " 9 November 2020":
        break
    content = subDriver.find_element_by_css_selector("#content")
    print(content.text)

    for relatedWord in relatedWords:
        if relatedWord.lower() in content.text or relatedWord in content.text:
            relatedLinks.append(latestLink)
            break
    subDriver.close()

    # menu = driver.find_elements_by_css_selector("body > div > div.uk-clearfix.ns-clear.uk-container.uk-container-center.ns-nav-wrap.ns-nav-article-page > nav > ul > li:nth-child(2) > a")
    # menu.click()


print(relatedLinks)

# Set Global Variables
gmail_user = 'xinruakatony@gmail.com'
gmail_password = 'Guttentag0124'
# Create Email
mail_from = gmail_user
mail_to = 'xinchen3@publicisgroupe.net'
mail_subject = 'Hello'
mail_message_body = 'Hello World!' # I can add news related to Real Estate, Property, Investment, Home to the message

mail_message = '''\
From: %s
To: %s
Subject: %s
%s
''' % (mail_from, mail_to, mail_subject, mail_message_body)
# Sent Email
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(gmail_user, gmail_password)
# server.sendmail(mail_from, mail_to, mail_message)
server.close()

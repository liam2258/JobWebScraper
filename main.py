from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

#Function searches job description and returns an array of all mentioned programming languages
def filter_languages(desc):
    lang = [0] * 16

    if 'JavaScript' in desc:
        lang[0] = 1
    if 'HTML' in desc:
        lang[1] = 1
    if 'CSS' in desc:
        lang[2] = 1
    if 'Python' in desc:
        lang[3] = 1
    if 'SQL' in desc:
        lang[4] = 1
    if 'Java' in desc:
        lang[5] = 1
    if 'C#' in desc:
        lang[6] = 1
    if 'Bash' in desc:
        lang[7] = 1
    if 'C++' in desc:
        lang[8] = 1
    if 'PHP' in desc:
        lang[9] = 1
    if 'Kotlin' in desc:
        lang[10] = 1
    if 'Rust' in desc:
        lang[11] = 1
    if 'Ruby' in desc:
        lang[12] = 1
    if 'Dart' in desc:
        lang[13] = 1
    if 'Swift' in desc:
        lang[14] = 1
    if 'Golang' in desc:
        lang[15] = 1

    return lang

#Selects the next page of jobs and gives time for it to load
def next_page():
    firefox.find_element(By.CLASS_NAME, "nextButton").click()
    time.sleep(7)

#Create initial csv file
with open('job_data.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file, lineterminator = '\n')
    csv_writer.writerow([
        'company',
        'title',
        'location',
        'javascript',
        'html',
        'css',
        'python',
        'sql',
        'java',
        'c#',
        'bash',
        'c++',
        'php',
        'kotlin',
        'rust',
        'ruby',
        'dart',
        'swift',
        'golang'
    ])

#Requires the installation of Geckodriver, can be swapped out with any other browser driver
firefox = webdriver.Firefox()

#Can be replaced with any other glassdoor /Job/ search url
url = 'https://www.glassdoor.com/Job/software-engineer-jobs-SRCH_KO0,17.htm'
firefox.get(url)
time.sleep(2)

#Click first job listing to trigger pop-up
firefox.find_element(By.CLASS_NAME, "react-job-listing").click()
time.sleep(4)
#Click close on pop-up
firefox.find_element(By.CLASS_NAME, "modal_closeIcon-svg").click()
time.sleep(4)
#Click show more button to get full job description
firefox.find_element(By.CLASS_NAME, "css-t3xrds.e856ufb4").click()

#Loop over the desired amount of job pages
for x in range(30):
    #Fetch all data on current page and store them in lists
    jobList = firefox.find_elements(By.CLASS_NAME, "react-job-listing")
    companies = firefox.find_elements(By.CLASS_NAME, 'd-flex.justify-content-between.align-items-start')
    titles = firefox.find_elements(By.CLASS_NAME, 'jobLink.css-1rd3saf.eigr9kq3')
    locations = firefox.find_elements(By.CLASS_NAME, 'css-3g3psg.pr-xxsm.css-iii9i8.e1rrn5ka0')
    
    #Fetch description of each job on the page and then instert data into csv file
    for idx, item in enumerate(jobList):
        jobList[idx].click()
        time.sleep(7)
        firefox.find_element(By.CLASS_NAME, "css-t3xrds.e856ufb4").click()
        time.sleep(7)
        company = companies[idx].text
        title = titles[idx].text
        location = locations[idx].text
        desc = firefox.find_element(By.CLASS_NAME, 'jobDescriptionContent.desc').text
        lang = filter_languages(desc)
        
        #Insert data into file
        with open('job_data.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file, lineterminator = '\n')
            csv_writer.writerow([
                company,
                title,
                location,
                lang[0],
                lang[1],
                lang[2],
                lang[3],
                lang[4],
                lang[5],
                lang[6],
                lang[7],
                lang[8],
                lang[9],
                lang[10],
                lang[11],
                lang[12],
                lang[13],
                lang[14],
                lang[15]
            ])

    #Glassdoor allows a maximum of 30 pages of results in one search
    if x == 29:
        break

    next_page()

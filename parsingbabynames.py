from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from copy import deepcopy
import csv
from selenium.webdriver.firefox.options import Options

class BabyNames:

    start_url = 'http://www.babynames.com'
    driver = None
    # session_id = None
    
   
    def __init__(self):
        self.csv_file = open('F:/babylinksatoz.csv', mode='w', newline = '')
        self.fieldnames = ['Name', 'Gender', 'Origin', 'Meaning', 'Description' , 'Source_url']
        self.writer = csv.DictWriter(self.csv_file, fieldnames= self.fieldnames)
        self.writer.writeheader()

    def start_request(self):
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--headless')
        self.driver = webdriver.Chrome()
        self.driver.get(self.start_url)
        self.parse()

    def parse(self):
        # self.session_id = self.driver.session_id
        baby_names_urls = self.driver.find_elements_by_css_selector(".browsebyletter a")
        # print('parent session id: ', self.session_id)
        for letter_url in self.get_urls(baby_names_urls):
            print('Now requesting to {}'.format(letter_url))
            self.driver.get(letter_url)
            self.parse_letters()
           
    def parse_letters(self):
        try:
            new_list = self.driver.find_elements_by_css_selector(".searchresults a")
            for next_urls in self.get_urls(new_list):
                # print('parent session id: ', self.session_id)
                # self.driver.session_id = self.session_id
                print("Now requesting to {}".format(next_urls))
                self.driver.get(next_urls)
                self.export_items(next_urls)
        except Exception as err:
            print(dir(err))
            print('exception is coming err={}'.format(err.args))
            pass

    def export_items(self, url):
        name = self.driver.find_element_by_css_selector(".baby-name")
        print(name)
        gender = self.driver.find_element_by_xpath(".//div[contains(text(), 'Gender:')]/*")
        origin = self.driver.find_element_by_xpath(".//div[contains(text(), 'Origin:')]/*")
        meaning = self.driver.find_element_by_xpath(".//div[contains(text(), 'Meaning:')]/*")
        description = self.driver.find_element_by_css_selector(".nameitem p")
        print("Now Writing")
        self.writer.writerow({'Name': name.text, 'Gender' : gender.text, 'Origin' : origin.text, 'Meaning' : meaning.text, 'Description' : description.text, 'Source_url' : url })
     
        # self.driver.close()
        # csv_file.close() 





        

    def get_urls(self, obj_list):
        return  [
        url.get_attribute("href") for url in obj_list
    ]

    def __del__ (self):
        self.driver.close()
        self.csv_file.close()
        self.driver.quit()



    
   

a = BabyNames()
a.start_request()
        
             
            
               
            
            

        


    
    


    




    
   


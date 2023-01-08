import webbrowser
import re
import codecs # встроенная бибилотека по чтению фалов 
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
import pandas as pd
# нужен модуль для создания excel файла 
#df = pd.DataFrame({'ASK': ['test'], 'ANS': ['test']})


driver = webdriver.Chrome('C:\\Users\\Дмитрий\\Desktop\\VS_Code\\creative_project\\search_google\\chromedriver.exe')



def search(name_ask):
    df = pd.DataFrame({'ASK': ['test'], 'ANS': ['test']})    
    #call = input('Введите ссылку или запрос: ')
    for i in range(len(name_ask)):
        
        if re.search(r'\ ', name_ask[i]):

            #webbrowser.open_new_tab('https://' + name_ask[0] )
            driver.get("http://www.google.com"+'/search?q='+ name_ask[i] )
            try:

                elem= driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/span[1]')
                print(elem.text)
                new_row = {'ASK':name_ask[i], 'ANS':elem.text }
                df = df.append(new_row, ignore_index=True)
                
                
            except: #
                try:
                    elem= driver.find_element(By.XPATH, '//*[@id="Odp5De"]/div[1]/div/div[1]/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[1]/div/span/span')
                    print(elem.text)
                    new_row = {'ASK':name_ask[i], 'ANS':elem.text }
                    df = df.append(new_row, ignore_index=True)
                    
                    
                except:
                    new_row = {'ASK':name_ask[i], 'ANS':'Ищи сам епта' }
                    df = df.append(new_row, ignore_index=True)
                    
                pass
        time.sleep(6)
    df.to_excel('teams.xlsx')
            

#//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/span[1]    

def open_file():

    

    fileObj = codecs.open( "C:\\Users\Дмитрий\\Desktop\\VS_Code\\creative_project\\search_google\\qwerst.txt", "r", "utf_8_sig" )
    text = fileObj.read() # или читайте по строке
    fileObj.close()

   
    new_text= text.split('\r\n')
    print(new_text[0])
    search(new_text)
    
    pass



open_file()



"""
elif re.search(r'\ ', name_ask[0] ):

        #webbrowser.open_new_tab('https://google.com/search?q='+ name_ask[0] )
        driver.get("http://www.google.com"+'/search?q='+ name_ask[0] )
        elem= driver.find_element(By.XPATH, '//*[@id="kp-wp-tab-overview"]/div[1]/div/div/div/div/div/div/div[1]/div/div/div/span[1]')
        print(elem.text)

        new_row = {'ASK':name_ask[0], 'ANS':elem.text }
        df = df.append(new_row, ignore_index=True)
        print(df)
        print('ДВА')
        time.sleep(10)

"""
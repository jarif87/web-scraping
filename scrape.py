from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

col=["World Rank","National Rank","Name","Image URLs","Affiliation","Country","H-Index","#DBLP","Citations"]

def get_scholar_details(row):
   
    details=row.text.split("\n")
    
    contents={}
    contents["World Rank"]=details[0]
    contents["National Rank"]=details[1]
    contents["Name"]=details[2]
    contents["Affiliation"]=details[3].split(",")[0]
    contents["Country"]=details[3].split(",")[1].strip()
    contents["H-Index"]=details[4]
    contents["Citations"]=details[5].replace(",","")
    contents["#DBLP"]=details[6].replace(",","")
   
    contents["Image URLs"]=row.find_element(By.CLASS_NAME,"lazyload").get_attribute("src")
    return contents
    
    
    
    

def main():
    webdriver_path="C:/Users/user/Music/chromedriver-win64/chromedriver-win64/chromedriver.exe"
   
    
    scholar_data=[]
    for page_id in range(1,11):
        
        driver=webdriver.Chrome()
        
        url=f"https://research.com/scientists-rankings/computer-science?page={page_id}"
   
        
        
       
        driver.get(url)
        rankings=driver.find_element(By.ID,"rankingItems")
        rows=rankings.find_elements(By.CLASS_NAME,"cols")
        
    
        for id,row in enumerate(rows):
            if id%4==0:
                
                scholar_data.append(get_scholar_details(row))
            
        driver.close()
    df=pd.DataFrame(data=scholar_data,columns=col)
    df.to_csv("my_data.csv",index=False)
    return

if __name__=="__main__":
    main()



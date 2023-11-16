from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

column=["Position","Player","Match","Inns","NO","Runs","High_Score","Avg","Bf","SR","Hundreds","Fifty","Fours","Sixs"]

def main():
    url="https://www.iplt20.com/stats/2022"
    driver=webdriver.Chrome()
    driver.get(url)
    table=driver.find_element(By.CLASS_NAME,"st-table")
    
    rows=table.find_elements(By.TAG_NAME,"tr")
   
    data=[]
    for row in rows[1:]:
        cel=row.find_elements(By.TAG_NAME,"td")
        row_data=[cell.text for cell in cel]
        
        if row_data:
            data.append(row_data)
    
    df=pd.DataFrame(data,columns=column)
    # print(df.head())
    print(df.shape)
    df.to_csv("IPL_2022.csv",index=False)
   
    time.sleep(10)
    driver.close()
    return

if __name__=="__main__":
    main()
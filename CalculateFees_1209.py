from selenium import webdriver
from SeleniumLibrary import SeleniumLibrary
from datetime import datetime
from DateTime import DateTime
import time
import random

# 定義變數
url = "https://istockapp.cathaysec.com.tw/Marketing/DCA/?initMessage=%E5%AE%9A%E6%9C%9F%E6%8A%95%E8%B3%87%E6%89%8B%E7%BA%8C%E8%B2%BB&initShowType=4#calculator"
activity_end_date = "2024-12-31"

# 初始化 SeleniumLibrary 和 dateTime
selenium_lib = SeleniumLibrary()
date_time_lib = DateTime()

# 計算手續費
def calculate_fees():
    selenium_lib.open_browser(url, "chrome")
    selenium_lib.set_selenium_implicit_wait(5)

    
    current_date = datetime.today().strftime("%Y-%m-%d")
    print(f"Current Date: {current_date}")
    
    # 計算美股定期定額買進手續費
    usa_fee = selenium_lib.get_text("id=calc-total")
    #2024/12/31前，手續費皆為0.1元
    if current_date <= activity_end_date:
        check_us_fees_for_buying(usa_fee)
    else:
        ask_a_fa()
    
    # 計算美股定期定額賣出手續費
    #手續費皆為3元
    check_us_fees_for_selling(usa_fee)
    
    # 計算台股定期定額手續費
    fee_text = selenium_lib.get_text("xpath=//*[@id='calculator']/div/div[7]/div[1]/div/b")
    print(f"Fee Text: {fee_text}")
    #2024/12/31前，手續費皆為1元
    if current_date <= activity_end_date:
        check_taiwan_fees(fee_text)
    else:
        ask_a_fa()
    
    selenium_lib.close_browser()

# 檢查台股手續費
def check_taiwan_fees(fee_text):
    selenium_lib.click_element("xpath=//*[@id='calculator']/div/div[6]/div[1]/a")
    selenium_lib.wait_until_element_is_visible("id=regular_price")
    time.sleep(4)
    
    my_list = [1, 2, 3]
    for index in my_list:
        tw_random_amount = random.randint(100, 1000)
        print(f"Index: {index}")
        selenium_lib.input_text("id=regular_price", tw_random_amount)
        print(f"Random Amount: {tw_random_amount}")
        time.sleep(3)
        selenium_lib.click_element("id=calculator_finish")
        print("Calculate finish")
        time.sleep(3)
        new_fee_text = selenium_lib.get_text("xpath=//*[@id='calculator']/div/div[7]/div[1]/div/b")
        print(f"New Fee Text: {new_fee_text}")
        assert new_fee_text == '1', f"Expected Fee: 1"
        print(f"台股定期定額手續費皆為1元")
        print(f"台股定期定額買進，隨機輸入金額檢查手續費完成")
        time.sleep(3)
        

# 檢查美股買進手續費
def check_us_fees_for_buying(usa_fee):
    selenium_lib.click_element("xpath=//*[@id='calculator']/div/div[6]/div[2]/a/i")
    selenium_lib.wait_until_element_is_visible("xpath=//*[@id='calculator']/div/div[8]/div[8]/a")
    selenium_lib.click_element("//*[@id='calculator']/div/div[8]/div[3]/div[2]/div[1]/span")
    selenium_lib.wait_until_element_is_visible("//*[@id='calculator']/div/div[8]/div[3]/div[2]/div[1]/ul/li[3]")
    selenium_lib.click_element("//*[@id='calculator']/div/div[8]/div[3]/div[2]/div[1]/ul/li[3]")
    time.sleep(2)
    selenium_lib.click_element("xpath=//*[@id='calculator']/div/div[8]/div[4]/div[2]/div/span")
    time.sleep(3)
    selenium_lib.wait_until_element_is_visible("//*[@id='calculator']/div/div[8]/div[4]/div[2]/div/ul/li[1]")
    selenium_lib.click_element("//*[@id='calculator']/div/div[8]/div[4]/div[2]/div/ul/li[1]")
    time.sleep(3)
    print("Wait")
    selenium_lib.wait_until_element_is_visible("//*[@id='stock_price_c']")
    
    my_list = [1, 2, 3]
    for index in my_list:
        us_random_amount = random.randint(100, 1000)
        print(f"Index: {index}")
        selenium_lib.click_element("//*[@id='stock_price_c']")
        time.sleep(2)
        selenium_lib.input_text("//*[@id='stock_price_c']", us_random_amount)
        print(f"Random Amount: {us_random_amount}")
        selenium_lib.click_element("xpath=//*[@id='calculator']/div/div[8]/div[8]/a")
        time.sleep(3)
        new_usa_fee = selenium_lib.get_text("id=calc-total")
        assert new_usa_fee == '0.10', f"Expected Fee: 0.10"
        print(f"美股定期定額買進手續費皆為0.1元")
        print(f"美股定期定額買進，隨機輸入金額檢查手續費完成")
        selenium_lib.input_text("//*[@id='stock_price_c']", us_random_amount)
        selenium_lib.press_keys("//*[@id='stock_price_c']", "\\")
        time.sleep(3)
        
# 檢查美股賣出手續費
def check_us_fees_for_selling(usa_fee):
    selenium_lib.click_element("xpath=//*[@id='calculator']/div/div[8]/div[4]/div[2]/div/span")
    selenium_lib.click_element("//*[@id='calculator']/div/div[8]/div[4]/div[2]/div/ul/li[2]")
    
    my_list = [1, 2, 3]
    for index in my_list:
        us_random_amount = random.randint(10, 1000)
        print(f"Index: {index}")
        selenium_lib.click_element("//*[@id='stock_price_c']")
        time.sleep(2)
        selenium_lib.input_text("//*[@id='stock_price_c']", us_random_amount)
        print(f"Random Amount: {us_random_amount}")
        selenium_lib.click_element("xpath=//*[@id='calculator']/div/div[8]/div[8]/a")
        time.sleep(3)
        new_usa_fee = selenium_lib.get_text("id=calc-total")
        assert new_usa_fee == '3.00', f"Expected Fee: 3.00"
        print(f"美股定期定額賣出手續費皆為3元")
        print(f"美股定期定額賣出，隨機輸入金額檢查手續費完成")
        selenium_lib.input_text("//*[@id='stock_price_c']", us_random_amount)
        selenium_lib.press_keys("//*[@id='stock_price_c']", "\\")
        time.sleep(3)
        

# 2024/12/31之後問顧問有沒有新活動算法
def ask_a_fa():
    print("Ask A FA")

# 執行計算
calculate_fees()

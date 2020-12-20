# 使用cookie登录
import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCookie():
    # 获取cookie，序列化后存入yaml文件内
    def test_get_cookie(self):
        opt = webdriver.ChromeOptions()
        # 设置debug地址
        opt.debugger_address = "127.0.0.1:9222"
        driver = webdriver.Chrome(options=opt)
        driver.implicitly_wait(5)
        driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        cookie = driver.get_cookies()
        print(cookie)
        with open("./data.yaml", "w", encoding="UTF-8") as f:
            yaml.dump(cookie, f)

    # 使用序列化cookie的方法进行登录
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        with open("./data.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element_by_id("menu_contacts").click()
        self.driver.find_element_by_link_text("添加成员").click()
        self.driver.find_element(By.XPATH, "//*[@id='username']").send_keys("小何没有头16")
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_english_name']").send_keys("是小16何啊")
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_acctid']").send_keys("xiaohenotouya16")
        self.driver.find_element(By.XPATH, "//*[@id='memberAdd_phone']").send_keys("15255555516")
        self.driver.find_element_by_link_text("保存").click()
        assert self.driver.find_elements_by_xpath('//*[@data-name="contacts"]//span[contains(text(),"15255555516")]')
        self.driver.quit()

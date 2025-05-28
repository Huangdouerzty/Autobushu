from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

# 浏览器配置（无头）
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# 创建浏览器驱动
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# 打开网页
url = "https://cqpp-8gevrjwmd8c11305-1329246163.tcloudbaseapp.com/index.html"
driver.get(url)

# 等待页面加载
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "xmphone")))

# 输入内容
driver.find_element(By.ID, "xmphone").send_keys("15037114942@163.com")
driver.find_element(By.ID, "xmpwd").send_keys("zty20011129")
driver.find_element(By.ID, "steps").clear()
steps = str(random.randint(8000, 9000))
print("提交步数：", steps)
driver.find_element(By.ID, "steps").send_keys(steps)

# 提交表单
submit_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "subButton")))
submit_btn.click()

# 保存截图
time.sleep(5)
driver.save_screenshot("result.png")

# 关闭浏览器
driver.quit()

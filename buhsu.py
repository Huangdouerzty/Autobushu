from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time
import random

# 浏览器配置
options = Options()
options.add_argument('--headless')  # 可选：开启无头模式
options.add_argument('--disable-gpu')

# 使用 Service 指定驱动路径
service = Service(EdgeChromiumDriverManager().install())

#print("启动 Edge 浏览器...")
driver = webdriver.Edge(service=service, options=options)

# 打开网页
url = "https://cqpp-8gevrjwmd8c11305-1329246163.tcloudbaseapp.com/index.html"
#print(f"打开网址: {url}")
driver.get(url)

# 等待页面加载
#print("正在等待页面加载...")
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "xmphone")))
#print("页面加载完成")

# 输入内容
driver.find_element(By.ID, "xmphone").send_keys("15037114942@163.com")
driver.find_element(By.ID, "xmpwd").send_keys("zty20011129")
driver.find_element(By.ID, "steps").clear()
steps = str(random.randint(8000, 9000))
print(steps)
driver.find_element(By.ID, "steps").send_keys(steps)

# 提交
submit_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, "subButton")))
submit_btn.click()

# 可截图保存结果
time.sleep(5)
driver.save_screenshot("result.png")
#print("步数已提交，截图已保存。")

# 关闭浏览器
driver.quit()

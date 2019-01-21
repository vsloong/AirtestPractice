# -*- encoding=utf8 -*-
__author__ = "CooLoongWu"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

num = 0

## 找到J_barrier_free节点下所有子节点（包含了能量球以及其他元素）
list_node = poco("android:id/content").offspring("com.alipay.mobile.nebula:id/h5_fragment").offspring("J_barrier_free").children()

## 遍历出所有可以收取的能量球节点，点击节点实现收集能量
for node in list_node:
    name = node.get_name()
    if  name.find("收集能量") >= 0:
        node.click()
        
poco("com.alipay.mobile.nebula:id/h5_tv_nav_back").click()



# # 获取所有蚂蚁森林上半部分元素信息
# title_list = poco("android:id/content").offspring("com.alipay.mobile.nebula:id/h5_fragment").offspring("J_barrier_free")

# print("=====打印结果=====")
# print(type(title_list))




## 向上滚动屏幕
# poco.swipe(起点坐标，终点坐标)，屏幕左上角为(0, 0)，屏幕右下角为(1, 1)
# poco.swipe([0.5, 0.8], [0.5, 0.2])


## 找到可以偷取的人







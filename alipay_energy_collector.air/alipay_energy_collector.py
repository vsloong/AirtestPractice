# -*- encoding=utf8 -*-
__author__ = "CooLoongWu"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

auto_setup(__file__)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

# =========================偷取能量=========================
def steal():
    # 睡眠，否则获取不到当前页面节点
    sleep(2)
    
    ## 找到J_barrier_free节点下所有子节点（包含了能量球以及其他元素）
#     list_node = poco("android:id/content").offspring("com.alipay.mobile.nebula:id/h5_fragment").offspring("J_barrier_free").wait(5).children()
    list_node = poco("J_barrier_free").wait(5).children()

    ## 遍历出所有可以收取的能量球节点，点击节点实现收集能量
    for node in list_node:
        name = node.get_name()
        if  name.find("收集能量") >= 0:
            node.click()

    # 返回上一页
    back_btn = poco("com.alipay.mobile.nebula:id/h5_tv_nav_back")
    if back_btn.exists():
        back_btn.click()
# =========================偷取能量=========================


# =========================获取列表item高度=========================
def height_item(list_friend):
#     list_friend = poco("J_rank_list").children()
    h = list_friend[1].get_position()[1] - list_friend[0].get_position()[1]
    return round(h,3)
# =========================获取列表item高度=========================

# =========================获取我的排名=========================
def index_my():
    node_my = poco("android:id/content").offspring("com.alipay.mobile.nebula:id/h5_fragment").offspring("J_rank_list_self").child("android.view.View").children()
    for node in node_my:
        index_my = node.get_name()
        if index_my.isdigit():
            print("我的排名是："+ str(int(index_my)))
            return int(index_my)
# =========================获取我的排名=========================


list_friend = poco("J_rank_list").children()
index = 4
index_my = index_my()
height_item = height_item(list_friend)

while True:
    # 如果当前索引是5的倍数，那么需要向上滚动屏幕
    print("当前索引"+str(index))
    if  index%5 == 0:
        if index == 5:
            print("滚动屏幕5 -> 1")
#             position_start = poco(str(index)).get_position()
#             position_end = list_friend[0].get_position()
#             print(position_start)
#             print(position_end)
#             poco.swipe([0.5,position_start[1]], position_end) 
            end = list_friend[1]
            start = poco(str(index))
            
            start.drag_to(end)
        else:
            print("滚动屏幕>5")
#             position_start = poco(str(index)).get_position()
#             position_end = poco(str(index-5)).get_position()
#             print(position_start)
#             print(position_end)
#             poco.swipe(position_start, position_end)   
            end = poco(str(index-5))
            start = poco(str(index))
            start.drag_to(end)
    # 如果是我的索引跳过本次循环
    if index == index_my:
        index += 1
        continue
    # 如果是小于三的按当前页面的列表的索引去算
    if index < 4:
        list_friend[index-1].click()
        steal()
        index += 1
    else:
        friend = poco(str(index))
        friend.click()
        steal()
        index += 1
            
        

    
# list_can = poco("可收取")
# if list_can.exists():
#     for can in list_can:
#         can.click()
#         # 睡眠，否则获取不到下个页面节点
#         sleep(5)poco("com.alipay.mobile.nebula:id/h5_tv_nav_back")

#         steal()
# else:
#     poco.swipe([0.5,0.8],[0.5,0.3])
        
# more = poco("查看更多好友")
# if more.exists():
#     print("点击->查看更多好友")
#     more.click()

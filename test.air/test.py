# -*- encoding=utf8 -*-
__author__ = "CooLoongWu"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

auto_setup(__file__)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

index = 1

screen_size = poco.get_screen_size()
print(screen_size)

# touch(Template(r"tpl1548212565602.png", record_pos=(0.476, -0.769), resolution=(1080, 2220)))


#[1080, 2220]

while index<10 :
    poco.swipe([0.5,0.8], [0.5,0.6])
    index += 1
        
        
        



# poco("android:id/content").offspring("com.alipay.mobile.nebula:id/h5_fragment").offspring("J_rank_list").child("android.view.View")[2]

# poco("android:id/content").offspring("com.alipay.mobile.nebula:id/h5_fragment").offspring("J_rank_list").child("android.view.View")[2].child("android.view.View")[0]


# 第一条好友
# poco("android:id/content").offspring("com.alipay.mobile.nebula:id/h5_fragment").offspring("J_rank_list").child("android.view.View")[0]

# 第4条好友
# poco("4")
        
# for friend in list_friend:
#     node_friend = friend.child(index).existes()
#     friend.click()
#     steal()
#     index++
    
# list_can = poco("可收取")
# if list_can.exists():
#     for can in list_can:
#         can.click()
        
#         steal()
# else:
#     poco.swipe([0.5,0.8],[0.5,0.3])
        
# more = poco("查看更多好友")
# if more.exists():
#     print("点击->查看更多好友")
#     more.click()

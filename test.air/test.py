# -*- encoding=utf8 -*-
__author__ = "CooLoongWu"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

auto_setup(__file__)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

scrollView = poco("android.widget.ListView")
scrollView.focus([0.5, 0.8]).drag_to(scrollView.focus([0.5, 0.2]))
sleep(2)
scrollView.focus([0.5, 0.8]).drag_to(scrollView.focus([0.5, 0.2]))
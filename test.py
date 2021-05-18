from pywinauto import application
from pywinauto.keyboard import send_keys

pc = application.Application(backend='uia').start('notepad.exe') #打开记事本
wind_calc = pc['无标题 - 记事本']
wind_calc.print_control_identifiers()# 打印属性
# edit = wind_calc['Edit']
# edit.type_keys("这是测试文本") #输入文字
# send_keys("^a")
# titleBar = wind_calc['TitleBar']
# titleBar.




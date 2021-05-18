from pywinauto import application
import os
import lackey
import time
from keyboard import mouse

os.environ.update({"__COMPAT_LAYER":"RUnAsInvoker"})
path = r'D:\anyto\iMyFone AnyTo\AnyTo.exe'
app = application.Application().start(path)
time.sleep(5)
#若出现升级弹框，关闭弹框
try:
    lackey.click('photo/livedate.png')
except:
    pass
#若出现消息中心弹框，关闭弹框
try:
    lackey.click('photo/messagecenter.png')
except:
    pass
lackey.click('photo/getstart.png')#点击开始



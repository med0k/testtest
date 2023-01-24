# Cоздать новый репо для этих задач
# Создать проект в виртуальном окружении venv
# создать скрипт, который выводит имя ОС
# опубликовать в репо проект (без venv)


import os
import sys
import platform
import sysconfig
print("os.name                     ", os.name)
print("sys.platform                ", sys.platform)
print("platform.system()           ", platform.system())
print("sysconfig.get_platform()    ", sysconfig.get_platform())
print("platform.machine()          ", platform.machine())
print("platform.architecture()     ", platform.architecture())
print("platform.python_version()   ", platform.python_version())
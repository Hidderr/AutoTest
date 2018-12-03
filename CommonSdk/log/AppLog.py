import subprocess
import time
import os
import re
def log(filename='..\\testFFS.log',logtag='',loglevel='E'):
    global file,pi
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time())) # 获取当前时间
    # filename = "D:/test/logs/" + now + r"log.txt" # 日志文件名添加当前时间
    # file = open(filename, 'w')
    logcmd = "adb logcat"
    # pi = subprocess.popen(logcmd, stdout=filename, stderr=subprocess.PIPE)
    # pi = subprocess.Popen(logcmd,stdout=filename,shell=True)

    # pi = subprocess.Popen(logcmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # print(pi.stdout.read())
    dir = os.path.abspath(os.path.join(os.path.dirname('TestReport3.py'), os.path.pardir)) + "\output"
    testdir = r'' + dir
    # testdir = r"D:\machine_Learning\machine_pycharm\Common\CommonSdk\output"
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    logcatname = testdir + "\\" +filename+ "_"+now + r"_logcat.log"
    cmd = "adb logcat *:"+loglevel+" -s "+logtag+" -f >%s" % (logcatname)
    # cmd = "adb  logcat -v time >%s" % (logcatname)+"  *:W | grep "+logtag+""
    # cmd = "adb logcat  >%s" % (logcatname)
    os.popen(cmd)



def closeLog():
    os.system('adb kill-server')


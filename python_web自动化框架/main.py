import pytest
from Common.dir_config import *
import time

if __name__ == '__main__':
    now=time.strftime('%Y-%m-%d_%H_%M_%S')
    html_path = htmlreport_dir + '\\test'+now+"report.html"
    xml_path = htmlreport_dir+ '\\test' + now+"report.xml"
    pytest.main(['-m','smoke',"--html="+html_path,"--junitxml="+xml_path])
    # pytest.main(["-m","test","--reruns","3", "--reruns-delay", "5","--html=" + html_path, "--junitxml=" + xml_path])
    # pytest.main(["--html=" + html_path, "--junitxml=" + xml_path])#执行所有用例

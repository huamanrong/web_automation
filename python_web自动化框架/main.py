#Author: xiaojian
#Time: 2018/8/2 20:56
import pytest
from Common.dir_config import *

if __name__ == '__main__':
    html_path = htmlreport_dir + "\\report.html"
    xml_path = htmlreport_dir + "\\report.xml"
    #pytest.main(["-m","smoke","--html="+html_path,"--junitxml="+xml_path])
    pytest.main(['-m','smoke',"--html=" + html_path, "--junitxml=" + xml_path])
    # pytest.main(["--html=" + html_path, "--junitxml=" + xml_path])#执行所有用例

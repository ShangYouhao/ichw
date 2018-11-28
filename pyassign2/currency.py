def defender(crsf, crst, amtf):
    """确认输入值为正确的形式"""

    if type(crsf) != str or type(crst) != str:
        print("""请输入字符串形式的货币单位符号""")
        return False
    elif len(crsf) != 3 or len(crst) != 3 or crsf.isupper() == False or crst.isupper() == False:
        print("""必须输入三个大写字母代表的货币单位符号""")
        return False
    elif type(amtf) != float and type(amtf) != int:
        print("""请输入数字形式的需兑换货币数值""")
        return False
    else:
        return True


def get_inf(crsf, crst, amtf):
    """根据正确的输入从网站'http://cs1110.cs.cornell.edu/2016fa/a1server.php?'获取字符串形式的信息."""

    site = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from={0}&to={1}&amt={2}'.format(crsf, crst, str(float(amtf)))
    from urllib.request import urlopen
    
    doc = urlopen(site)
    docstr = doc.read()
    doc.close()
    infmt = docstr.decode('ascii')
    return infmt


def analz(infmt):
    """分析获取的字符串信息并返回一个浮点数形式的可兑换数值. 若输入货币种类有误，则返回'请输入正确的货币代码'."""

    infmt_in = infmt.replace('true', 'True')
    infmt_in = infmt_in.replace('false', 'False')
    dic = eval(infmt_in)
    if dic["success"] == False:
        print("错误！请输入正确的货币代码")
        return None
    else:
        str_to = dic["to"]
        list_to = str_to.split()
        val_to = float(list_to[0])
        return val_to


def exchange(crsf, crst, amtf):
    """接受被兑换货币(字符串，三位大写符号)、目标货币(同前一项)、兑换量(浮点数形式)作为参数，返回可兑换目标货币的量"""

    if defender(crsf, crst, amtf) == True:
        return analz(get_inf(crsf, crst, amtf))
    else:
        return None


def test_defender():
    """测试defender()函数的功能"""

    assert(False == defender(1, 2, 2.5))
    assert(False == defender('usd', 'eur', 2.5))
    assert(False == defender('us doller', 'Euro', 3.1))
    assert(False == defender('USD', 'EUR', "2.6"))
    assert(True == defender("USD", "EUR", 3.14))


def test_get_inf():
    """测试get_inf()函数的功能"""

    assert("""{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }""" == get_inf("CHY","EUR",2.5))


def test_analz():
    """测试analz()函数的功能"""

    assert(str(17.13025) == str(analz("""
{ "from" : "2.5 United States Dollars", "to" : "17.13025 Chinese Yuan", "success" : true, "error" : "" }""")))
    assert(None == analz("""
{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }"""))
    assert(float == type(analz("""
{ "from" : "2.5 United States Dollars", "to" : "17.13025 Chinese Yuan", "success" : true, "error" : "" }""")))


def test_exchange():
    """测试exchange()函数的功能"""

    assert(str(17.13025) == str(exchange("USD","CNY", 2.5)))
    assert(None == exchange("USD", "CHN", 2.3))
    assert(float == type(exchange("USD", "CNY", 2.3)))


def test_all():
    """测试所有函数"""

    test_defender()
    test_get_inf()
    test_analz()
    test_exchange()
    print("""
All tests passed""")


if __name__ == '__main__':
    test_all()

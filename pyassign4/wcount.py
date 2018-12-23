
"""wcount.py: 单词计数

__author__ = "Shang Youhao"
__pkuid__  = "1800011714"
__email__  = "Shangyouhao@pku.edu.cn"
"""


import sys
from urllib.request import urlopen


def find_words(lines):
    """将字符串中的单词找出并返回一个由单词组成的列表"""
    words = []
    word = []
    state = 0
    for letter in lines:
        a = ord(letter)
        if 65 <= a <=90 or 97 <= a <= 122 or a == 39:
            word.append(letter)
            state = 1
        elif state == 1:
            words.append("".join(word))
            word[:] = []
            state = 0
    return words


def cot(lines):
    """返回一个单词计数结果的字典，从单词对应到频率"""
    wds = find_words(lines)
    nums = dict()
    for wd in wds:
        wd = wd.lower()
        if wd in nums:
            nums[wd] += 1
        else:
            nums[wd] = 1
    return nums


def wcount(lines, topn = 10):
    """接受一个字符串，统计其中的单词出现频率，
并输出频率最高的n个单词及其频率，若缺省，输出最高的十个"""
    lst = sorted([(a, b) for (b, a) in cot(lines).items()])
    i = -1
    anss_lst = []
    while i >= -topn:
        anss_lst.append((lst[i][1], lst[i][0]))
        i -= 1
    anss_dct = dict(anss_lst)
    return anss_dct


def main():
    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    
    else:
        try:
            doc = urlopen(sys.argv[1])
            txt = doc.read().decode()
            doc.close
            if len(sys.argv) == 3:
                anss = wcount(txt, int(sys.argv[2]))
            else:
                anss = wcount(txt)
            for ans in anss.items():
                print("%-15.15s" % ans[0], ans[1])
            return anss
        except Exception as err:
            print(err)


if __name__ == '__main__':
    anss = main()

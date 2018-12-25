import sys
from urllib.request import urlopen


def find_words(lines):
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
    lst = sorted([(a, b) for (b, a) in cot(lines).items()])
    i = -1
    anss_lst = []
    if topn <= len(lst):
        while i >= -topn:
            anss_lst.append((lst[i][1], lst[i][0]))
            i -= 1
        anss_dct = dict(anss_lst)
    else:
        lst.reverse()
        anss_dct = dict([(b, a) for (a, b) in lst])
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

import argparse
parser = argparse.ArgumentParser(description = 'Process some markdown files so that the style of math equation is capable for the hexo & mathjax.')
parser.add_argument('files', type = argparse.FileType('r+'), nargs = '+',
                    help='files\' directory.')
parse = parser.parse_args()

# print(parse)

def check (t):
    for v in t:
        if v.find("{% raw %}") != -1:
            return True
    return False

for f in parse.files:
    t = f.readlines()
    if check(t):
        continue
    f.seek(0)
    f.truncate()
    # print(t)
    fstDoubleDollar = False
    fstDollar = False
    last_is_Dollar = False
    for eachLine in t:
        currentLine = ""
        for v in eachLine:
            if v == '$':
                if last_is_Dollar: # $$
                    if fstDoubleDollar:
                        currentLine += "$${% endraw %}"
                        fstDoubleDollar = False
                    else:
                        fstDoubleDollar = True
                        currentLine += "{% raw %}$$"
                    last_is_Dollar = False
                elif fstDollar: # $
                    currentLine += "${% endraw %}"
                    fstDollar = False
                else:
                    last_is_Dollar = True
            else:
                if last_is_Dollar:
                    fstDollar = True
                    currentLine += "{% raw %}$"
                currentLine += v
                last_is_Dollar = False
        f.write(currentLine)
    if last_is_Dollar: 
        f.write("{% raw %}$")
    f.close()

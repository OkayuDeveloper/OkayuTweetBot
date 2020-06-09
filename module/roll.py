import time
import math
import re
from random import randint

#代码来自https://github.com/akrisrn/dice
def roll(a, b):
    return sum([randint(1, b) for _ in range(a)]), a, a * b

def roll_comp(r, e, f):
    a, b = True, False
    if r == '∞' and e == '∞':
        return True
    elif r != '∞' and e != '∞':
        a = False
    elif r == '∞':
        b = False
    elif e == '∞':
        b = True

    if f == "<":
        return b if a else r < e
    if f == "<=":
        return b if a else r <= e
    if f == ">":
        return not b if a else r > e
    if f == ">=":
        return not b if a else r >= e
    if f == "==":
        return False if a else r == e
    if f == "!=":
        return False if a else r != e
    return False

def roll_oper(x, c, d):
    for i in range(len(c)):
        cx = c[i]
        if isinstance(c[i], str):
            cx = int(c[i].split(" → ")[1])
        if d[i] == "+":
            x += cx
        elif d[i] == "-":
            x -= cx
        elif d[i] == "*":
            x *= cx
        elif d[i] == "/":
            if cx == 0:
                return '∞'
            x = math.ceil(x / cx)
    return x

def roll_split(x):
    if x:
        sp = re.split('([+-/*])', x)[1:]
        np = []
        for p in sp[1::2]:
            match = re.compile('([1-9][0-9]{0,2})?[d|D]([1-9][0-9]{0,2})').match(p)
            if match:
                rand, rand_min, rand_max = roll(int(match.group(1)) if match.group(1) else 1, int(match.group(2)))
                np.append("(%d-%d) → %s" % (rand_min, rand_max, rand))
            else:
                np.append(int(p))
        return np, sp[::2]
    else:
        return [0], ["+"]

def match_roll(sender, content):
    sm = ""
    for cont in content.split("\n"):
        pattern = re.compile('^([1-9][0-9]{0,2})?[d|D]([1-9][0-9]{0,2})'
                             # 匹配1个xdy、xDy、dy、Dy，x(1-999)，y(1-999)，取x、y
                             '((?:(?:[+-/*](?:[1-9][0-9]{0,2})?[d|D][1-9][0-9]{0,2})|(?:[+-/*][0-9]{1,3}))*)?'
                             # 匹配0或多个+xdy、+xDy、+dy、+Dy、
                             #          -xdy、-xDy、-dy、-Dy、
                             #          /xdy、/xDy、/dy、/Dy、
                             #          *xdy、*xDy、*dy、*Dy、
                             #          +z、-z、/z、*z，x(1-999)，y(1-999)，z(0-999)，取全部
                             '((?:[><=!]=?(?:[1-9][0-9]{0,2})?[d|D][1-9][0-9]{0,2})|(?:[><=!]=?(?:[0-9]{1,3})))?'
                             # 匹配0或1个>xdy、<xdy、=xdy、!xdy、>=xdy、<=xdy、==xdy、!=xdy、
                             #         >xDy、<xDy、=xDy、!xDy、>=xDy、<=xDy、==xDy、!=xDy、
                             #         >dy、<dy、=dy、!dy、>=dy、<=dy、==dy、!=dy、
                             #         >Dy、<Dy、=Dy、!Dy、>=Dy、<=Dy、==Dy、!=Dy、
                             #         >z、<z、=z、!z、>=z、<=z、==z、!=z，x(1-999)，y(1-999)，z(0-999)，取全部
                             '((?:(?:[+-/*](?:[1-9][0-9]{0,2})?[d|D][1-9][0-9]{0,2})|(?:[+-/*][0-9]{1,3}))*)?'
                             # 匹配0或多个+xdy、+xDy、+dy、+Dy、
                             #          -xdy、-xDy、-dy、-Dy、
                             #          /xdy、/xDy、/dy、/Dy、
                             #          *xdy、*xDy、*dy、*Dy、
                             #          +z、-z、/z、*z，x(1-999)，y(1-999)，z(0-999)，取全部
                             '\s*(.*)'
                             # 匹配0或多个空白符以及0或多个任意字符，取任意字符
                             )
        match = pattern.match(cont)
        if match:
            g1 = int(match.group(1)) if match.group(1) else 1
            g2 = int(match.group(2))
            g3, g4 = roll_split(match.group(3))
            rand, rand_min, rand_max = roll(g1, g2)
            rand_true = roll_oper(rand, g3, g4)
            comp = ""
            if match.group(4):
                pattern_comp = re.compile('(?:([><=!]=?)([1-9][0-9]{0,2})?[d|D]([1-9][0-9]{0,2}))|'
                                          '(?:([><=!]=?)([0-9]{1,3}))')
                match_comp = pattern_comp.match(match.group(4))
                if match_comp.group(1):
                    g5, g5_min, g5_max = roll(int(match_comp.group(2)) if match_comp.group(2) else 1,
                                              int(match_comp.group(3)))
                    g5_show = "(%d-%d) → %s" % (g5_min, g5_max, g5)
                    g6_index = 1
                else:
                    g5 = int(match_comp.group(5))
                    g5_show = g5
                    g6_index = 4
                g6 = match_comp.group(g6_index) + ("=" if match_comp.group(g6_index) in ["=", "!"] else "")
                g7, g8 = roll_split(match.group(5))
                g5_true = roll_oper(g5, g7, g8)
                success = "大成功！" if g1 == 1 and g2 == 100 and 1 <= rand <= 5 else "成功"
                failure = "大失败！" if g1 == 1 and g2 == 100 and 96 <= rand <= 100 else "失败"
                if len(g7) == 1 and g7[0] == 0 and g8[0] in "+-":
                    if g6_index == 4:
                        right = "%s" % g5_true
                    else:
                        right = "%s(%s)" % (g5_true, g5_show)
                else:
                    right = "%s(%s%s)" % (g5_true, g5_show,
                                          "".join([" %s %s" % (g8[i], g7[i]) for i in range(len(g7))]))
                comp = " %s %s → %s" % (g6, right, success if roll_comp(rand_true, g5_true, g6) else failure)
            if len(g3) == 1 and g3[0] == 0 and g4[0] in "+-":
                left = "%s" % rand_true
            else:
                left = "%d%s = %s" % (rand, "".join([" %s %s" % (g4[i], g3[i]) for i in range(len(g3))]), rand_true)
            sm += "[%s]: (%d-%d) → %s%s%s\\n" % (sender, rand_min, rand_max, left, comp,
                                                 " (%s)" % match.group(6) if match.group(6) else "")
    return sm[:-2]
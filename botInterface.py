import nonebot
from random import random

#Bot Interface
randomPool = []
matchCode = int(random(1)) * 10000

def matchCodeGenerator(seed):
    matchCode = matchCode * seed % 10000
    return matchCode

#pull notification info into QBot

def pullMessage(matchCode, message):
    pass

#Push notification into
def pushTranslation(matchCode, translation):
    pass

#PATH INITIALIZE
import sys
from os import path

d = path.dirname(__file__)
parent_path = path.dirname(d)
parent_path = path.dirname(parent_path)
parent_path = path.dirname(parent_path)
sys.path.append(parent_path)
print(sys.path)
import plugins.configure.configuration as conf
#sys.path.append(conf.matsuri_translation_path)
#from tweet_process import TweetProcess

from selenium import webdriver



def getImageProcess():
    pass


def translateProcess():
    pass
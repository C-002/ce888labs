from sopel import module
from emo.wdemotions import EmotionDetector
import numpy as np

emo = EmotionDetector()
count = []
ave = 0
iter_messages = 0

@module.rule('')
def hi(bot, trigger):
    print(trigger, trigger.nick)
    global ave
    global iter_messages
    #bot.say('Hi, ' + trigger.nick)
    first = emo.detect_emotion_in_raw(trigger)[0]
    if(ave ==0 ):
        ave = first
    else:
        ave +=first

    iter_messages +=1

    print(ave/iter_messages)

    # count  = count[0] + first
    print((emo.detect_emotion_in_raw_np(trigger)))
    # print(count)

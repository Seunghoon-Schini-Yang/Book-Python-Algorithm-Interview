# laboratory

import re

sentence = "Bob hit a ball, the hit BALL flew far after it was hit."


sentence = re.sub('[^a-z ]', '', sentence.lower())

print(sentence)
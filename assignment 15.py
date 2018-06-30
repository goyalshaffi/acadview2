'''
# q1
import re
emails = '''"zuck26@facebook.com" "page33@google.com"
"jeff42@amazon.com"'''
userid=re.findall('[a-z0-9]+',emails)
print(userid)

# q2
import re
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
words=re.findall('[bB][a-z]*',text)
print(words)

# q3
import re
text=''' "A, very very; irregular_sentence"'''
words=re.sub(r'[,;_\s]',' ',text)
print(words)
'''
# q4
import re
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
words=re.sub(r'[!,;_\s][@ :]',' ',tweet)
print(words)

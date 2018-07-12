from collections import Counter
import nltk
from nltk.corpus import *
nltk.download('stopwords')
text="hello to all i am isha from punjabi university patiala patiala is very nice place"
stop_words=set(stopwords.words('english'))
print(stop_words)
list1=text.split()
print(list1)
for i in list1:
    if i not in stop_words:
        print(i)
count=Counter(list1).most_common(5)
print(count)

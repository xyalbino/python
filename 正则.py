import re
p=re.compile(" (\w+) (\w+)")
result=p.search("I love FishC")
print(result.group())

```import tkinter
# Displays the name of Bing

zeroone_str = ""
n = 7

for i in range(1, n+1):
	zeroone_str += "1"
	for k in range(0, i):
		zeroone_str += "0"
		
zeroone = float("0." + zeroone_str)	
print(zeroone_str)
print(zeroone)```

#! python3
# Aaron Haws
import os

f = open("pythonfile.txt", "w")
f.write("""line 1
line2
line3""")
f.close()

f = open("pythonfile.txt", "r")
print(f.readline())
f.close()

if os.path.exists("pythonfile.txt"):
  os.remove("pythonfile.txt")
else:
  print("The file does not exist")


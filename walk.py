import os

for root, dirs, files in os.walk("."):
#   print(root)
   for dir in files:
     print(dir)
   #for name in files:
      #print(os.path.join(root, name))
   #for name in dirs:
      #print(os.path.join(root, name))

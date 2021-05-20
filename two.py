import hashlib
import sys
import os

checksum = sys.argv[1]
path = sys.argv[2]
checksums = open('checksums', 'r')
lines = checksums.readlines()

for line in lines:
  values = line.split(" ")
  fileName = values[0]
  fileName = os.path.join(path,fileName)
  hashMechanism = values[1]
  checksum = values[2]

  hasher = None

  if hashMechanism == 'md5':
   hasher = hashlib.md5()
  else:
   if hashMechanism == 'sha1':
    hasher = hashlib.sha1()
   else:
    print("Wrong hash mechanism selected.")

  buf = None

  try:
    with open(fileName, 'rb') as afile:
      buf = afile.read()
      hasher.update(buf)
      countedChecksum = hasher.hexdigest()
      result = None
      if countedChecksum == checksum:
       result = "OK"
      else:
       result = "FAIL"

      print(fileName + " " + result)
  except:
    print(fileName + " NOT EXIST")

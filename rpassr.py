import base64, hashlib
# print "Welcome to Restrictions Passcode Recovery\n----------"
# print "H ~ Help\nR ~ Recover Passcode\nV ~ Verbose Recovery\nA ~ Advanced Recovery\nX ~ Exit"

def recover(verbose, min=0, max=1000):
  goal_key = bytes(input("What is RestrictionsPasswordKey? "),'utf8')
  salt = input("What is RestrictionsPasswordSalt? ")
  success = 0
  raw_code = 0
  while raw_code < 10000:
    code = ("0000" + str(raw_code))[-4:]
    trial = base64.b64encode(hashlib.pbkdf2_hmac('sha1', bytes(code,'utf8'), base64.b64decode(salt), 1000))
    if verbose:
      print("Code: %s, Produced: %s" % (code,str(trial,'utf8')))
    if trial == goal_key:
      print("FOUND PASSCODE! %s" % code)
      success = 1
      break
    else:
      raw_code += 1
  if not success:
    print("FAILED. It is recommended that you try again. Check entry.")
    print("Key: %s | Salt: %s" % (str(goal_key,'utf8'),salt))

recover(0)
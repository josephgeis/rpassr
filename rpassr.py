import base64, hashlib
# print "Welcome to Restrictions Passcode Recovery\n----------"
# print "H ~ Help\nR ~ Recover Passcode\nX ~ Exit"

def recover():
  goal_key = bytes(input("What is RestrictionsPasswordKey? "),'utf8')
  salt = input("What is RestrictionsPasswordSalt? ")
  raw_code = 0
  while raw_code < 10000:
    code = ("0000" + str(raw_code))[-4:]
    trial = base64.b64encode(hashlib.pbkdf2_hmac('sha1', bytes(code,'utf8'), base64.b64decode(salt), 1000))
    print("Code: %s, Produced: %s" % (code,trial))
    if trial == goal_key:
      print("FOUND PASSCODE! %s" % code)
      break
    else:
      raw_code += 1

recover()
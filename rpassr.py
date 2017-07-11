import base64, hashlib, sys, os

print("Welcome to Restrictions Passcode Recovery\n----------")

def recover(verbose, sta=0, end=9999):
  goal_key = bytes(input("What is RestrictionsPasswordKey? "),'utf8')
  salt = input("What is RestrictionsPasswordSalt? ")
  success = 0
  raw_code = sta
  while raw_code <= end:
    code = ("0000" + str(raw_code))[-4:]
    trial = base64.b64encode(hashlib.pbkdf2_hmac('sha1', bytes(code,'utf8'), base64.b64decode(salt), 1000))
    if verbose:
      print("Code: %s, Produced: %s" % (code,str(trial,'utf8')))
    if trial == goal_key:
      print("FOUND PASSCODE! %s" % code)
      success = 1
      sys.exit(0)
    else:
      raw_code += 1
  if not success:
    print("FAILED. It is recommended that you try again. Check entry.")
    print("Key: %s | Salt: %s" % (str(goal_key,'utf8'),salt))

def help():
  try:
    open("README.md")
    os.system('less --prompt="LOCAL rpassr HELP | PRESS q TO EXIT" README.md')
  except IOError:
    print("See the README on GitHub. https://github.com/juniorRubyist/rpassr")

def adv_recover():
  sta = int(input("Starting Passcode? [0000]: "))
  end = int(input("Ending Passcode? [9999]: "))
  recover(1,sta=sta,end=end)

opts = {
  'h' : (help,[]),
  'r' : (recover,[0]),
  'v' : (recover,[1]),
  'a' : (adv_recover,[]),
  'x' : (sys.exit,[0])
}

while True:
  print("H ~ Help\nR ~ Recover Passcode\nV ~ Verbose Recovery\nA ~ Advanced Recovery\nX ~ Exit")
  choice = input(">> ").lower()
  try:
    opts[choice][0](*opts[choice][1])
  except KeyError:
    print("Not an option")

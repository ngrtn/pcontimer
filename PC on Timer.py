# Idea: Set timer and turn off pc/
# code not 100% right!
import os
import time

def main():
   print('Welcome to PC on Timer!\nType the time you want your pc to be turned off\n')
   command = str(input('if u r ready type "start" or type "instructions" for getting the same message!\n'))

   if command == 'start':
      timer = int(input('Type number of seconds: '))
      while timer:
         print(timer)
         time.sleep(1)
         timer = timer-1
      if timer <= 0:
         os.system("shutdown -s -t 0")
   if command == 'instructions':
      main()
main()
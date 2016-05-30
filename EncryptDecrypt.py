import getpass
import os

def main():
	mode = raw_input('Mode: "e" for encrypt, "d" for decrypt > ')
	if mode == 'e':
		end = 'ENCRYPTED'
	elif mode == 'd':
		end = 'DECRYPTED'

     toProcess = raw_input(('Enter the sentence to be '+end+' > '))
	pwd = getpass.getpass('ENTER PASSWORD *will not be seen as you type* > ')

	processed = ''
	lenPwd = len(pwd)

	for counter in range(len(toProcess)):
		pwd += pwd[counter]
		if counter == lenPwd:
			counter = 0
          
	for index in range(len(toProcess)):
		encryptedLetters = letters[letters.index(pwd[index]):] + letters[:letters.index(pwd[index])]
		if mode == 'e':
			processed += encryptedLetters[letters.index(toProcess[index])]
		elif mode == 'd':
			processed += letters[encryptedLetters.index(toProcess[index])]

	print "\n"+end+' sentence: ',`processed`
	raw_input()
	main()
	
new = False
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ,abcdefghijklmnopqrstuvwxyz. 0123456789!#/=@$%&\':+-;*?'

#------------GET FILE----------------
try:
     f = open('logED.dat','r+')
except IOError:
     f = open('logED.dat','a+')
_f = f.readlines()
try:
     _f[0]
     if _f[0][:1] == '0':
		 new = True
except IndexError:
     new = True

if new:
     f.close()
     f = open('logED.dat','w+')

     f.write('0 \n')
     f.close()

     print '===============/!\ PLEASE READ THIS CAREFULLY /!\================'
     _a = "This encrypt/decrypter software (hereinafter called as \"software\") is provided \"AS IS\", and is still in a non-stable version (beta). There may be some bugs and/or defects. By using this program, you take the whatever risks you may have (but not limited to loss of love (break up), divorce, seizure, blindness, loss of hearing, marks dropping in school/college/university/education, loss of job, death (of anyone), assassination, etc.) (\"risks\") created as a result of this software. The software developer (\"developer\") does not hold any responsiblity regarding to your usage of this software. \n\nBy typing 'agree', you abide and agree to the terms and conditions, indemnify your own risks, and hold harmless of the developer > "
     agree = raw_input(_a).lower()
     if agree != 'agree':
		os.system('exit')
     else:
		print "=================================================================\n"
		f = open('logED.dat','w')
		f.write('1')
		f.close()

#--------------------------

f = open('logED.dat','r+')
_f = f.readlines()

if _f[0][:1] == '1':
     main()

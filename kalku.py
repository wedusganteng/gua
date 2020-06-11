import os,sys,time,random
blue = '\033[34;1m'
green = '\033[32;1m'
purple = '\033[35;1m'
cyan = '\033[36;1m'
red = '\033[31;1m'
white = '\033[37;1m'
yellow = '\033[33;1m'
os.system('clear')
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.2)
mengetik('WELCOME IN MY TOOLS..')
mengetik('.')
mengetik('.')
mengetik('menghubungi Fajar..')
mengetik ('Please Wait !!')
mengetik ('WELCOME..!!')
mengetik ('kalo gak Tau Username Sama Password Bisa pm = 6287837482552')
print
print ("\033[1;32mMasukan UserName&Password")
username = 'Wedus'
password = 'Gans'

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():
        uname = raw_input("username : ")
        if uname == username:
                pwd = raw_input("password : ")

                if pwd == password:
                	os.system('clear')
                else:
                        print "\n\033[1;36mSorry Invalid password !!!\033[00m"
                        print "Back Login\n"
                        restart()

        else:
                print "\n\033[1;36mSorry Invalid Username !!!\033[00m"
                print "Back Login\n"
                restart()

try:
        main()
except KeyboardInterrupt:
             os.system('clear')
banner="""
\033[31m
????????????
  ????????????
  ????????????
  ????????????
  ????????????
  ????????????
 ??????????????
 termux_hacking
 ??????????????
  ?????????????
  ?????????????
  ?????????????
  ?????????????
  ?????????????
   ??????????
     ???????????????????.?oO
     ????????
     ????????                                                                        
"""
os.system('figlet Kalkulator | lolcat')
os.system('date | lolcat')
print(banner)

#fungsi penjumlahan
def add(x,y):
    return x + y

#fungsi pengurangan
def subtract(x, y):
    return x - y

#fungsi perkalian
def multiply(x, y):
    return x * y

#fungsi pembagian
def divide(x, y):
    return x / y

print("Pilih Operasi")
print("\x1b[91m1.\x1b[94m Penjumlahan")
print("\x1b[91m2. \x1b[94mPengurangan")
print("\x1b[91m3. \x1b[94mPerkalian")
print("\x1b[91m4. \x1b[94mPembagian")

#Meminta input dari pengguna
choice = input("\x1b[0mMasukkan Pilihan Operasi Bilangan (1/2/3/4):\x1b[95m ")

num1 = int(input("\x1b[91mMasukkan Bilangan Pertama:\x1b[92m "))
num2 = int(input("\x1b[91mMasukkan Bilangan Kedua:\x1b[92m "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Masukan yg bener kontol!!!")
time.sleep(0.5)
print('\x1b[95mThanks sudah memggunakan tools ini')
time.sleep(0.5)
print('\x1b[94mFajar Gans')
#developer / Mohamed Alaa
#Key_Two-X
# The latest version of the project 
import socket
import sys
import webbrowser
from time import *
from random import choice
from tqdm import tqdm, trange
import os
import platform
import random
from gtts import gTTS
from company import company
import playsound
from pystyle import *
#import pygame
def text():
  ip = input("\033[1;32m   Enter A Domin : \033[39m")
  host = socket.gethostbyname(ip)
  print(host)


def IP():
  import socket
  hostName = socket.gethostname()
  ipAdd = socket.gethostbyname(hostName)
  print('\033[1;30m     PC Name or Phone Name : \033[39m' + hostName)
  print('\033[1;30m     IP-Address :\033[39m ' + ipAdd)


def Open():
  print('''\033[32;1m
    by : Momammed Alaa 
    my facebook : Mohamed Alaa
    my email : @unknown.com
    \033[39''')


def on_play():
  while True:
    num = int(input('\033[30m  Enter A Number Of A Even  : \033[39m'))
    if num % 2 == 0:
      print(
          f'\033[32m  {  num} This Number is Even....& Correct Answer✅✅✅ \033[39m'
      )
      exit()
    else:
      print(f'\033[1;31m {  num} This Number is Odd.. \033[39m')


def tool():
  i = input("\033[1;35m  Do you want to download the tool?   (Y/n) :\033[39m"
            ).lower()
  if i == "y":
  				
    # with tqdm(total=50) as pber:
    for I in tqdm(range(0,150),desc="Download TOOL...",unit ="  \33[31;1mWait For Doanload a TOOL\33[39m"):
        time.sleep(.122)
        
    print ('\33[1;31m   Preparing tool data..Wait \33[39m')
    # with tqdm(total=100) as pber:
    for I in tqdm(range(0,150),desc="\33[35;1mPreparing tool data..Wait \33[39m" ,unit='\33[36;1m  Tool it is need ROOT..!!~~!!\33[39m'):
          
          time.sleep(.11)
            
    print (''
        "\033[1;32m   Sorry, the tool requires root, You do not have root. \033[39m"
    )
  else:
    print('\033[1;31m  Ok The tool was not downloaded... \033[1;31m')
    print ('   The Code Is End...🫷')
    


def pelo():
  while True:
    smol = 'abcdefghijklmnopqrstwxyz.com'
    upeer = 'ABCDEFGHIGKLMNOPQRSTWXYZ.com'
    num = 'com0123456789'
    su = '.com[]{}/.#@-_\/$^*'
    all = smol + upeer
    m = num + su
    lo = 11
    password = "".join(random.sample(all, lo))
    word = "".join(random.sample(m, lo))
    print("\033[32mEmali : \033[39m", password)
    time.sleep(.5)
    print("\033[1;31mPassword : \033[39m", word)

def apple():
  # معرفه المكان الذي توجد فيه
  print ("\033[1;36m   current work dir : \033[39m" ,    os.getcwd())
  print ("\033[1;35m   Your platform is : \033[39m", platform.platform())
  #معرفه هل الجهاز ويندوز ام أندرويد او ...
def file():
				rt= open("File.txt" , "w")
				sys.stdout = rt
				print ("Opening the file")
				print ("Opening the file")
def size():
				print (" Max Size Is : " , sys.maxsize)
				#print (sys.argv)
def dor ():
      my_text =('Write any Words Want To Hear : ')
      text = gTTS (my_text)
      text.save ('Sound.mp3')
      sound = gTTS(ext= my_text , lang="ar")
      sound = gTTS(ext= my_text , lang="en")
      sound.save ('Sound.mp3')
      playsound('Sound.mp3')

def data ():
  from company import company

  Enployee1= company ("Mohamed Alaa" , 50 , "Facebook" , True , "Yes" , 3800)
  Enployee2= company ("Mahmoud Sami" , 25 , "YouTube" , False , "No" , 1500) 
  Enployee3= company ("Ahmed Muhammad" , 25 , "Google repository" , True , "Yes" , 2500) #*
  Enployee4= company ("Amr Hussein" , 19 , "NQ Company" , True , "Yes" , 2400)
  Enployee5= company ("Mustafa Rasheed" , 24 , "Google" , True , "Yes" , 3100)
  Enployee6= company ("Jaber Mahmoud" , 42 , "snap chat" , True , "Yes" , 2900)
  Enployee7= company ("Stephen Golder" , 45 , "Microsoft" , True , "Yes" , 2000)            
  Enployee8= company ("Adly Mohammadi" , 28 , "IOS developer" , True , "Yes" , 1700)
  Enployee9= company ("Mohammed Nasser" , 30 , "Android developer" , True , "Yes" , 2000)
  Enployee10= company ("Mohamed Ali" , 31 , "Website developer" , True , "Yes" , 2000)
  Enployee11= company ("Omar Badri" , 44 , "programs developer" , True , "Yes" , 2000)
  Enployee12= company ("Youssef Hamdi" , 30 , "Microsoft Edge" , False , "No" , 2300)
  Enployee13= company ("Hani Al-Sayed" , 42 , "Tick tock" , False , "No" , 2000)
  Enployee14= company ("Bilal Ghaly" , 49 , "Google Map" , False , "No " , 3500) 
  Enployee15= company ("Mahmoud Metwally" , 34 , "Director general" , False , "No" , 2900)
  Enployee16= company ("Ziad Mohammed" , 40 , "Google Translator" , False , "No" ,5000)#
  Enployee17= company ("Bayoumi Hassan" , 44 , "Google Drive" , False , "No" , 2400)
  Enployee18= company ("Mahmoud ElSayed" , 50 , "Google Earth" , False , "No" , 4000)
  Enployee19= company ("Syed Mohammed" , 38 , "Google Map" , False , "No" , 3500)
  Enployee20= company ("Saeed Saleh" , 39 , "Assistant Director" , True , "Yes" , 4000)
  Enployee21= company ("Mohamed salah" , 35 , "supervisor" , True , "Yes" , 2200)
  Enployee22= company ("Rania Hussein" , 41 , "H.R" , True , "Yes" , 7000)
  Enployee23= company ("ANKERRODRED" , 50 , "Google Samsung developer" , True , "Yes" , 7000)
  Enployee24= company ("Manuel Robson" , 45 , "Conference Supervisor" , True , "Yes" , 3500)
  Enployee25= company ("Laribaig" , 34 , "SQL developer" , True , "Yes" , 4000)
  Enployee26= company ("Sergey" , 64 , "WhatsApp developer" , True , "Yes" , 6000)
  Enployee27= company ("Steven Mark" , 45 , "Email developer" , True , "Yes" , 3000)
  Enployee28= company ("Hani Al-Saeed" , 42 , "Replicate developer" , False , "No" , 6300)#false
  Enployee29= company ("Ahmed" , 20 , "content creator" , False , "No" , 3500)
  Enployee30= company ("Nour Designer" , 25 , "content creator" , False , "No" , 2200)
  Enployee31= company ("TV number" , 30 , "content creator" , False , "No" , 2300)
  Enployee32= company ("Ahmed Abu Yazid" , 30 , "content creator" , False , "No" , 2400)
  Enployee33= company ("Jalal Muhammad" , 18 , "content creator" , False , "No" , 2400)
  Enployee34= company ("Amr Adib" ,    55 , "Journalist" , False , "No" , 3000)
  Enployee35= company ("Omar Musa" ,   51 , "Journalist" , True , "Yes" , 3000)
  Enployee36= company ("Lamis Al-Hadidi" , 42 , "Journalist" , True , "Yes" , 3000)
  Enployee37= company ("Mona El Shazly" , 40 , "Journalist" , True , "Yes", 3000) 
  Enployee38= company ("Tamer Amin" , 41 , "Journalist" , True , "Yes" , 3000)
  Enployee39= company ("jops alson" , 35 , "Messenger developer" , True , "Yes" , 4000)
  Enployee40= company ("Ashraf" , 40 , "Systems developer" , True , "Yes" , 8000)
  Enployee41= company ("Taher Mustafa" , 58 , "Facebook" , True , "Yes" , 4500)
  Enployee42= company ("Tamer Awad" , 35 , "Facebook" , True , "Yes" , 4500)
  Enployee43= company ("Ibrahim Sameh" , 34 , "Facebook" , True , "Yes" , 5000)
  Enployee44= company ("Mark Zuckerberg" , 45 , "Facebook" , False, "No" , 5000)#false
  Enployee45= company ("Aletta Sloker" , 40 , "Facebook" , False , "No" , 5000)
  Enployee46= company ("Nana Manuel" , 43 , "Facebook" , False , "No" , 4500)
  Enployee47= company ("Menna Mohammed" , 40 , "Facebook" , False , "No" , 4500)
  Enployee48= company ("Adressweiler" , 33 , "Facebook" , False , "No" , 5000)
  Enployee49= company ("Ahmed Dhamir" , 35 , "Facebook" , False , "No" , 4500)
  Enployee50= company ("Alberto" , 54 , "Facebook" , False , "No" , 5000)
  Enployee51= company ("Osama Mohammed" , 30 , "Facebook" , False , "No" , 4500)
  Enployee52= company ("Abdulaziz" , 36 , "Facebook" , False , "No" , 5000) 
  Enployee53= company ("Abd alhalim" , 39 , "WhatsApp" , False , "No" , 5000)#True
  Enployee54= company ("Ashraf Helmy" , 52 , "WhatsApp" , True , "Yes" , 4500)
  Enployee55= company ("Youssef Sabry" , 50 , "WhatsApp" , True , "Yes" , 5000)
  Enployee56= company ("Name not found" , 33 , "WhatsApp" , True , "Yes" , 4500)
  Enployee57= company ("Name not found" , 43 , "WhatsApp" , True , "Yes" , 4500)
  Enployee58= company ("Name not found" , 27 , "WhatsApp" , True , "Yes" , 5000)
  Enployee59= company ("Mr. Hafez" , 46 , "WhatsApp" , True , "Yes" , 5000)
  Enployee60= company ("Tamer Ahmed" , 40 , "WhatsApp" , True , "Yes" , 4500)
  Enployee61= company ("Elon Musk" , 45 , "Twitter" , True , "Yes" , 5000)
  Enployee62= company ("Issam Al-Debin" , 43 , "Twitter" , True , "Yes" , 4500)
  Enployee63= company ("Faisal Khalid" , 50 , "Twitter" , True , "Yes" , 5000)
  Enployee64= company ("Name not found" , 32 , "Twitter" , True , "Yes" , 3000)
  Enployee65= company ("Name not found" , 22 , "Twitter" , True , "Yes" , 2200) 
  Enployee66= company ("Name not found" , 31 , "Twitter" , True , "Yes" , 3000)
  Enployee67= company ("Mariam Mohammed" , 37 , "Twitter" , True , "Yes" , 3500)
  Enployee68= company ("Gne walid" , 40 , "Twitter" , True , "Yes" , 5000)
  Enployee69= company ("Sabry Muhammad" , 65 , "Twitter" , True , "Yes" , 5500)
  Enployee70= company ("Adel Madkour" , 45 , "YouTube" , True , "Yes" , 5000)
  Enployee71= company ("Name not found" , 43 , "YouTube" , True , "Yes" , 4500)
  Enployee72= company ("Rania" , 60 , "YouTube" , True , "Yes" , 4500)
  Enployee73= company ("Alaa Al-Sayed" , 76 , "YouTube" , True , "Yes" , 5000)
  Enployee74= company ("Hossam Mohammed" , 32 , "YouTube" , True , "Yes", 4500 )
  Enployee75= company ("Moaz Tamer" , 73 , "YouTube" , True , "Yes" , 5000) 
  Enployee76= company ("Falih Mansour" , 29 , "YouTube" , True , "Yes" , 4500)
  Enployee77= company ("Ahmed Saber" , 43 , "YouTube" , True , "Yes" , 5000)
  Enployee78= company ("Salah Mohammed" , 46 , "YouTube" , True , "Yes" , 4500)
  Enployee79= company ("Ahmed Mando" , 66 , "snap chat" , False , "No" , 5000)  
  Enployee80= company ("Name not found" , 46 , "snap chat" , False , "No" , 4500)
  Enployee81= company ("Name not found" , 62 , "snap chat" , False , "No" , 5000)
  Enployee82= company ("Name not found" , 68 , "snap chat" , False , "No" , 4500)
  Enployee83= company ("Name not found" , 32 , "snap chat" , False , "No" , 5000)
  Enployee84= company ("Name not found" , 72 , "snap chat" , False , "No" , 4500)
  Enployee85= company ("Name not found" , 71 , "snap chat" , False , "No" , 5000)
  Enployee86= company ("Name not found" , 36 , "snap chat" , False , "No" , 3800)
  Enployee87= company ("Name not found" , 40 , "Tik Tok" , False , "No" , 3500)
  Enployee88= company ("Saeed Halawani" , 35 , "Tik Tok" , False , "No" , 4000)
  Enployee89= company ("Sherif Arafah" , 60 , "Tik Tok" , True , "Yes" , 2100)#--------------------------------------------------------------
  Enployee90= company ("Tariq Al-Sharif" , 65 , "Tik Tok" , True , "Yes" , 7000)
  Enployee91= company ("Ammar Ali" , 35 , "Tik Tok" , True , "Yes" , 2100)
  Enployee92= company ("Karim Ghalib" , 40 , "Tik Tok" , True , "Yes" , 2010)
  Enployee93= company ("Karam Hamdi" , 43 , "Tik Tok" , True , "Yes" , 3000)
  Enployee94= company ("Fahd Khaled" , 33 , "Tik Tok" , True , "Yes" , 2700)
  Enployee95= company ("Khaled Al-Saeed" , 45 , "Microsoft" , True , "Yes" , 2000)
  Enployee96= company ("Nour Awad" , 30 , "Microsoft" , True , "Yes" , 2000)
  Enployee97= company ("Omar Ghareeb" , 65 , "Microsoft" , True , "Yes" , 2000)
  Enployee98= company ("Sherif Mansour" , 32 , "Microsoft" , True , "Yes" , 3000)
  Enployee99= company ("Assaf Abdullah" , 24 , "Microsoft" , True , "Yes" , 2800)
  Enployee100= company ("Ibrahim Mohamed" , 40 , "Microsoft" , True ,"Yes" , 4000)
  print("HELLO:",Enployee1.name ,"Your Department is" , Enployee1.department ,"Your Age is", Enployee1.age ,"Is he present or absent?" , Enployee1.Present_or_No ,"Your Salary" , Enployee1.salary) , Enployee1.bonus()
  print("HELLO:",Enployee2.name ,"Your Department is" , Enployee2.department ,"Your Age is", Enployee2.age ,"Is he present or absent?" , Enployee2.Present_or_No ,"Your Salary" , Enployee2.salary) , Enployee2.bonus()
  print("HELLO:",Enployee3.name ,"Your Department is" , Enployee3.department ,"Your Age is", Enployee3.age ,"Is he present or absent?" , Enployee3.Present_or_No ,"Your Salary" , Enployee3.salary) , Enployee3.bonus()
  print("HELLO:",Enployee4.name ,"Your Department is" , Enployee4.department ,"Your Age is", Enployee4.age ,"Is he present or absent?" , Enployee4.Present_or_No ,"Your Salary" , Enployee4.salary) , Enployee4.bonus()
  print("HELLO:",Enployee5.name ,"Your Department is" , Enployee5.department ,"Your Age is", Enployee5.age ,"Is he present or absent?" , Enployee5.Present_or_No ,"Your Salary" , Enployee5.salary) , Enployee5.bonus()
  print("HELLO:",Enployee6.name ,"Your Department is" , Enployee6.department ,"Your Age is", Enployee6.age ,"Is he present or absent?" , Enployee6.Present_or_No ,"Your Salary" , Enployee6.salary) , Enployee6.bonus()
  print("HELLO:",Enployee7.name ,"Your Department is" , Enployee7.department ,"Your Age is", Enployee7.age ,"Is he present or absent?" , Enployee7.Present_or_No ,"Your Salary" , Enployee7.salary) , Enployee7.bonus()
  print("HELLO:",Enployee8.name ,"Your Department is" , Enployee8.department ,"Your Age is", Enployee8.age ,"Is he present or absent?" , Enployee8.Present_or_No ,"Your Salary" , Enployee8.salary) , Enployee8.bonus()
  print("HELLO:",Enployee9.name ,"Your Department is" , Enployee9.department ,"Your Age is", Enployee9.age ,"Is he present or absent?" , Enployee9.Present_or_No ,"Your Salary" , Enployee9.salary) , Enployee9.bonus()
  print("HELLO:",Enployee10.name ,"Your Department is" , Enployee10.department ,"Your Age is", Enployee10.age ,"Is he present or absent?" , Enployee10.Present_or_No ,"Your Salary" , Enployee10.salary) , Enployee10.bonus()
  print("HELLO:",Enployee11.name ,"Your Department is" , Enployee11.department ,"Your Age is", Enployee11.age ,"Is he present or absent?" , Enployee11.Present_or_No ,"Your Salary" , Enployee11.salary) , Enployee11.bonus()
  print("HELLO:",Enployee12.name ,"Your Department is" , Enployee12.department ,"Your Age is", Enployee12.age ,"Is he present or absent?" , Enployee12.Present_or_No ,"Your Salary" , Enployee12.salary) , Enployee12.bonus()
  print("HELLO:",Enployee13.name ,"Your Department is" , Enployee13.department ,"Your Age is", Enployee13.age ,"Is he present or absent?" , Enployee13.Present_or_No ,"Your Salary" , Enployee13.salary) , Enployee13.bonus()
  print("HELLO:",Enployee14.name ,"Your Department is" ,Enployee14.department ,"Your Age is",  Enployee14.age ,"Is he present or absent?" , Enployee14.Present_or_No ,"Your Salary" , Enployee14.salary) , Enployee14.bonus()
  print("HELLO:",Enployee15.name ,"Your Department is" ,Enployee15.department ,"Your Age is",  Enployee15.age ,"Is he present or absent?" , Enployee15.Present_or_No ,"Your Salary" , Enployee15.salary) , Enployee15.bonus()
  print("HELLO:",Enployee16.name ,"Your Department is" , Enployee16.department ,"Your Age is", Enployee16.age ,"Is he present or absent?" , Enployee16.Present_or_No ,"Your Salary" , Enployee16.salary) , Enployee16.bonus()
  print("HELLO:",Enployee17.name ,"Your Department is" , Enployee17.department ,"Your Age is", Enployee17.age ,"Is he present or absent?" , Enployee17.Present_or_No ,"Your Salary" , Enployee17.salary) , Enployee17.bonus()
  print("HELLO:",Enployee18.name ,"Your Department is" , Enployee18.department ,"Your Age is", Enployee18.age ,"Is he present or absent?" , Enployee18.Present_or_No ,"Your Salary" , Enployee18.salary) , Enployee18.bonus()
  print("HELLO:",Enployee19.name ,"Your Department is" , Enployee19.department ,"Your Age is", Enployee19.age ,"Is he present or absent?" , Enployee19.Present_or_No ,"Your Salary" , Enployee19.salary) , Enployee19.bonus()
  print("HELLO:",Enployee20.name ,"Your Department is" , Enployee20.department ,"Your Age is", Enployee20.age ,"Is he present or absent?" , Enployee20.Present_or_No ,"Your Salary" , Enployee20.salary) , Enployee20.bonus()
  print("HELLO:",Enployee21.name ,"Your Department is" , Enployee21.department ,"Your Age is", Enployee21.age ,"Is he present or absent?" , Enployee21.Present_or_No ,"Your Salary" , Enployee21.salary) , Enployee21.bonus()
  print("HELLO:",Enployee22.name ,"Your Department is" , Enployee22.department ,"Your Age is", Enployee22.age ,"Is he present or absent?" , Enployee22.Present_or_No ,"Your Salary" , Enployee22.salary) , Enployee22.bonus()
  print("HELLO:",Enployee23.name ,"Your Department is" , Enployee23.department ,"Your Age is", Enployee23.age ,"Is he present or absent?" , Enployee23.Present_or_No ,"Your Salary" , Enployee23.salary) , Enployee23.bonus()
  print("HELLO:",Enployee24.name ,"Your Department is" , Enployee24.department ,"Your Age is", Enployee24.age ,"Is he present or absent?" , Enployee24.Present_or_No ,"Your Salary" , Enployee24.salary) , Enployee24.bonus()
  print("HELLO:",Enployee25.name ,"Your Department is" , Enployee25.department ,"Your Age is", Enployee25.age ,"Is he present or absent?" , Enployee25.Present_or_No ,"Your Salary" , Enployee25.salary) , Enployee25.bonus()
  print("HELLO:",Enployee26.name ,"Your Department is" , Enployee26.department ,"Your Age is", Enployee26.age ,"Is he present or absent?" , Enployee26.Present_or_No ,"Your Salary" , Enployee26.salary) , Enployee26.bonus()
  print("HELLO:",Enployee27.name ,"Your Department is" , Enployee27.department ,"Your Age is", Enployee27.age ,"Is he present or absent?" , Enployee27.Present_or_No ,"Your Salary" , Enployee27.salary) , Enployee27.bonus()
  print("HELLO:",Enployee28.name ,"Your Department is" , Enployee28.department ,"Your Age is", Enployee28.age ,"Is he present or absent?" , Enployee28.Present_or_No ,"Your Salary" , Enployee28.salary) , Enployee28.bonus()
  print("HELLO:",Enployee29.name ,"Your Department is" , Enployee29.department ,"Your Age is", Enployee29.age ,"Is he present or absent?" , Enployee29.Present_or_No ,"Your Salary" , Enployee29.salary) , Enployee29.bonus()
  print("HELLO:",Enployee30.name ,"Your Department is" , Enployee30.department ,"Your Age is", Enployee30.age,"Is he present or absent?" , Enployee30.Present_or_No ,"Your Salary" , Enployee30.salary) , Enployee30.bonus()
  print("HELLO:",Enployee31.name ,"Your Department is" , Enployee31.department ,"Your Age is", Enployee31.age ,"Is he present or absent?" , Enployee31.Present_or_No ,"Your Salary" , Enployee31.salary) , Enployee31.bonus()
  print("HELLO:",Enployee32.name ,"Your Department is" , Enployee32.department ,"Your Age is", Enployee32.age ,"Is he present or absent?" , Enployee32.Present_or_No ,"Your Salary" , Enployee32.salary) , Enployee32.bonus()
  print("HELLO:",Enployee33.name ,"Your Department is" , Enployee33.department ,"Your Age is", Enployee33.age ,"Is he present or absent?" , Enployee33.Present_or_No ,"Your Salary" , Enployee33.salary) , Enployee33.bonus()
  print("HELLO:",Enployee34.name ,"Your Department is" , Enployee34.department ,"Your Age is", Enployee34.age ,"Is he present or absent?" , Enployee34.Present_or_No ,"Your Salary" , Enployee34.salary) , Enployee34.bonus()
  print("HELLO:",Enployee35.name ,"Your Department is" , Enployee35.department ,"Your Age is", Enployee35.age ,"Is he present or absent?" , Enployee35.Present_or_No ,"Your Salary" , Enployee35.salary) , Enployee35.bonus()
  print("HELLO:",Enployee36.name ,"Your Department is" , Enployee36.department ,"Your Age is", Enployee36.age ,"Is he present or absent?" , Enployee36.Present_or_No ,"Your Salary" , Enployee36.salary) , Enployee36.bonus()
  print("HELLO:",Enployee37.name ,"Your Department is" , Enployee37.department ,"Your Age is", Enployee37.age ,"Is he present or absent?" , Enployee37.Present_or_No ,"Your Salary" , Enployee37.salary) , Enployee37.bonus()
  print("HELLO:",Enployee38.name ,"Your Department is" , Enployee38.department ,"Your Age is", Enployee38.age ,"Is he present or absent?" , Enployee38.Present_or_No ,"Your Salary" , Enployee38.salary) , Enployee38.bonus()
  print("HELLO:",Enployee39.name ,"Your Department is" , Enployee39.department ,"Your Age is", Enployee39.age ,"Is he present or absent?" , Enployee39.Present_or_No ,"Your Salary" , Enployee39.salary) , Enployee39.bonus()
  print("HELLO:",Enployee40.name ,"Your Department is" , Enployee40.department ,"Your Age is", Enployee40.age ,"Is he present or absent?" , Enployee40.Present_or_No ,"Your Salary" , Enployee40.salary) , Enployee40.bonus()
  print("HELLO:",Enployee41.name ,"Your Department is" , Enployee41.department ,"Your Age is", Enployee41.age ,"Is he present or absent?" , Enployee41.Present_or_No ,"Your Salary" , Enployee41.salary) , Enployee41.bonus()
  print("HELLO:",Enployee42.name ,"Your Department is" , Enployee42.department ,"Your Age is", Enployee42.age ,"Is he present or absent?" , Enployee42.Present_or_No ,"Your Salary" , Enployee42.salary) , Enployee42.bonus()
  print("HELLO:",Enployee43.name ,"Your Department is" , Enployee43.department ,"Your Age is", Enployee43.age ,"Is he present or absent?" , Enployee43.Present_or_No ,"Your Salary" , Enployee43.salary) , Enployee43.bonus()
  print("HELLO:",Enployee44.name ,"Your Department is" , Enployee44.department ,"Your Age is", Enployee44.age ,"Is he present or absent?" , Enployee44.Present_or_No ,"Your Salary" , Enployee44.salary) , Enployee44.bonus()
  print("HELLO:",Enployee45.name ,"Your Department is" , Enployee45.department ,"Your Age is", Enployee45.age ,"Is he present or absent?" , Enployee45.Present_or_No ,"Your Salary" , Enployee45.salary) , Enployee45.bonus()
  print("HELLO:",Enployee46.name ,"Your Department is" , Enployee46.department ,"Your Age is", Enployee46.age ,"Is he present or absent?" , Enployee46.Present_or_No ,"Your Salary" , Enployee46.salary) , Enployee46.bonus()
  print("HELLO:",Enployee47.name ,"Your Department is" , Enployee47.department ,"Your Age is", Enployee47.age ,"Is he present or absent?" , Enployee47.Present_or_No ,"Your Salary" , Enployee47.salary) , Enployee47.bonus()
  print("HELLO:",Enployee48.name ,"Your Department is" , Enployee48.department ,"Your Age is", Enployee48.age ,"Is he present or absent?" , Enployee48.Present_or_No ,"Your Salary" , Enployee48.salary) , Enployee48.bonus()
  print("HELLO:",Enployee49.name ,"Your Department is" , Enployee49.department ,"Your Age is", Enployee49.age ,"Is he present or absent?" , Enployee49.Present_or_No ,"Your Salary" , Enployee49.salary) , Enployee49.bonus()
  print("HELLO:",Enployee50.name ,"Your Department is" , Enployee50.department ,"Your Age is", Enployee50.age ,"Is he present or absent?" , Enployee50.Present_or_No ,"Your Salary" , Enployee50.salary) , Enployee50.bonus()
  print("HELLO:",Enployee51.name ,"Your Department is" , Enployee51.department ,"Your Age is", Enployee51.age ,"Is he present or absent?" , Enployee51.Present_or_No ,"Your Salary" , Enployee51.salary) , Enployee51.bonus()
  print("HELLO:",Enployee52.name ,"Your Department is" , Enployee52.department ,"Your Age is", Enployee52.age ,"Is he present or absent?" , Enployee52.Present_or_No ,"Your Salary" , Enployee52.salary) , Enployee52.bonus()
  print("HELLO:",Enployee53.name ,"Your Department is" , Enployee53.department ,"Your Age is", Enployee53.age ,"Is he present or absent?" , Enployee53.Present_or_No ,"Your Salary" , Enployee53.salary) , Enployee53.bonus()
  print("HELLO:",Enployee54.name ,"Your Department is" , Enployee54.department ,"Your Age is", Enployee54.age ,"Is he present or absent?" , Enployee54.Present_or_No ,"Your Salary" , Enployee54.salary) , Enployee54.bonus()
  print("HELLO:",Enployee55.name ,"Your Department is" , Enployee55.department ,"Your Age is", Enployee55.age ,"Is he present or absent?" , Enployee55.Present_or_No ,"Your Salary" , Enployee55.salary) , Enployee55.bonus()
  print("HELLO:",Enployee56.name ,"Your Department is" , Enployee56.department ,"Your Age is", Enployee56.age ,"Is he present or absent?" , Enployee56.Present_or_No ,"Your Salary" , Enployee56.salary) , Enployee56.bonus()
  print("HELLO:",Enployee57.name ,"Your Department is" , Enployee57.department ,"Your Age is", Enployee57.age ,"Is he present or absent?" , Enployee57.Present_or_No ,"Your Salary" , Enployee57.salary) , Enployee57.bonus()
  print("HELLO:",Enployee58.name ,"Your Department is" , Enployee58.department ,"Your Age is", Enployee58.age ,"Is he present or absent?" , Enployee58.Present_or_No ,"Your Salary" , Enployee58.salary) , Enployee58.bonus()
  print("HELLO:",Enployee59.name ,"Your Department is" , Enployee59.department ,"Your Age is", Enployee59.age ,"Is he present or absent?" , Enployee59.Present_or_No ,"Your Salary" , Enployee59.salary) , Enployee59.bonus()
  print("HELLO:",Enployee60.name ,"Your Department is" , Enployee60.department ,"Your Age is", Enployee60.age ,"Is he present or absent?" , Enployee60.Present_or_No ,"Your Salary" , Enployee60.salary) , Enployee60.bonus()
  print("HELLO:",Enployee61.name ,"Your Department is" , Enployee61.department ,"Your Age is", Enployee61.age ,"Is he present or absent?" , Enployee61.Present_or_No ,"Your Salary" , Enployee61.salary) , Enployee61.bonus()
  print("HELLO:",Enployee62.name ,"Your Department is" , Enployee62.department ,"Your Age is", Enployee62.age ,"Is he present or absent?" , Enployee62.Present_or_No ,"Your Salary" , Enployee62.salary) , Enployee62.bonus()
  print("HELLO:",Enployee63.name ,"Your Department is" , Enployee63.department ,"Your Age is", Enployee63.age ,"Is he present or absent?" , Enployee63.Present_or_No ,"Your Salary" , Enployee63.salary) , Enployee63.bonus()
  print("HELLO:",Enployee64.name ,"Your Department is" , Enployee64.department ,"Your Age is", Enployee64.age ,"Is he present or absent?" , Enployee64.Present_or_No ,"Your Salary" , Enployee64.salary) , Enployee64.bonus()
  print("HELLO:",Enployee65.name ,"Your Department is" , Enployee65.department ,"Your Age is", Enployee65.age ,"Is he present or absent?" , Enployee65.Present_or_No ,"Your Salary" , Enployee65.salary) , Enployee65.bonus()
  print("HELLO:",Enployee66.name ,"Your Department is" , Enployee66.department ,"Your Age is", Enployee66.age ,"Is he present or absent?" , Enployee66.Present_or_No ,"Your Salary" , Enployee66.salary) , Enployee66.bonus()
  print("HELLO:",Enployee67.name ,"Your Department is" , Enployee67.department ,"Your Age is", Enployee67.age ,"Is he present or absent?" , Enployee67.Present_or_No ,"Your Salary" , Enployee67.salary) , Enployee67.bonus()
  print("HELLO:",Enployee68.name ,"Your Department is" , Enployee68.department ,"Your Age is", Enployee68.age ,"Is he present or absent?" , Enployee68.Present_or_No ,"Your Salary" , Enployee68.salary) , Enployee68.bonus()
  print("HELLO:",Enployee69.name ,"Your Department is" , Enployee69.department ,"Your Age is", Enployee69.age ,"Is he present or absent?" , Enployee69.Present_or_No ,"Your Salary" , Enployee69.salary) , Enployee69.bonus()
  print("HELLO:",Enployee70.name ,"Your Department is" , Enployee70.department ,"Your Age is", Enployee70.age,"Is he present or absent?" , Enployee70.Present_or_No ,"Your Salary" , Enployee70.salary) , Enployee70.bonus()
  print("HELLO:",Enployee71.name ,"Your Department is" , Enployee71.department ,"Your Age is", Enployee71.age ,"Is he present or absent?" , Enployee71.Present_or_No ,"Your Salary" , Enployee71.salary) , Enployee71.bonus()
  print("HELLO:",Enployee72.name ,"Your Department is" , Enployee72.department ,"Your Age is", Enployee72.age ,"Is he present or absent?" , Enployee72.Present_or_No ,"Your Salary" , Enployee72.salary) , Enployee72.bonus()
  print("HELLO:",Enployee73.name ,"Your Department is" , Enployee73.department ,"Your Age is", Enployee73.age ,"Is he present or absent?" , Enployee73.Present_or_No ,"Your Salary" , Enployee73.salary) , Enployee73.bonus()
  print("HELLO:",Enployee74.name ,"Your Department is" , Enployee74.department ,"Your Age is", Enployee74.age ,"Is he present or absent?" , Enployee74.Present_or_No ,"Your Salary" , Enployee74.salary) , Enployee74.bonus()
  print("HELLO:",Enployee75.name ,"Your Department is" , Enployee75.department ,"Your Age is", Enployee75.age ,"Is he present or absent?" , Enployee75.Present_or_No ,"Your Salary" , Enployee75.salary) , Enployee75.bonus()
  print("HELLO:",Enployee76.name ,"Your Department is" , Enployee76.department ,"Your Age is", Enployee76.age ,"Is he present or absent?" , Enployee76.Present_or_No ,"Your Salary" , Enployee76.salary) , Enployee76.bonus()
  print("HELLO:",Enployee77.name ,"Your Department is" , Enployee77.department ,"Your Age is", Enployee77.age ,"Is he present or absent?" , Enployee77.Present_or_No ,"Your Salary" , Enployee77.salary) , Enployee77.bonus()
  print("HELLO:",Enployee78.name ,"Your Department is" , Enployee78.department ,"Your Age is", Enployee78.age ,"Is he present or absent?" , Enployee78.Present_or_No ,"Your Salary" , Enployee78.salary) , Enployee78.bonus()
  print("HELLO:",Enployee79.name ,"Your Department is" , Enployee79.department ,"Your Age is", Enployee79.age ,"Is he present or absent?" , Enployee79.Present_or_No ,"Your Salary" , Enployee79.salary) , Enployee79.bonus()
  print("HELLO:",Enployee80.name ,"Your Department is" , Enployee80.department ,"Your Age is", Enployee80.age ,"Is he present or absent?" , Enployee80.Present_or_No ,"Your Salary" , Enployee80.salary) , Enployee80.bonus()
  print("HELLO:",Enployee81.name ,"Your Department is" , Enployee81.department ,"Your Age is", Enployee81.age ,"Is he present or absent?" , Enployee81.Present_or_No ,"Your Salary" , Enployee81.salary) , Enployee81.bonus()
  print("HELLO:",Enployee82.name ,"Your Department is" , Enployee82.department ,"Your Age is", Enployee82.age ,"Is he present or absent?" , Enployee82.Present_or_No ,"Your Salary" , Enployee82.salary) , Enployee82.bonus()
  print("HELLO:",Enployee83.name ,"Your Department is" , Enployee83.department ,"Your Age is", Enployee83.age ,"Is he present or absent?" , Enployee83.Present_or_No ,"Your Salary" , Enployee83.salary) , Enployee83.bonus()
  print("HELLO:",Enployee84.name ,"Your Department is" , Enployee84.department ,"Your Age is", Enployee84.age ,"Is he present or absent?" , Enployee84.Present_or_No ,"Your Salary" , Enployee84.salary) , Enployee84.bonus()
  print("HELLO:",Enployee85.name ,"Your Department is" , Enployee85.department ,"Your Age is", Enployee85.age ,"Is he present or absent?" , Enployee85.Present_or_No ,"Your Salary" , Enployee85.salary) , Enployee85.bonus()
  print("HELLO:",Enployee86.name ,"Your Department is" , Enployee86.department ,"Your Age is", Enployee86.age ,"Is he present or absent?" , Enployee86.Present_or_No ,"Your Salary" , Enployee86.salary) , Enployee86.bonus()
  print("HELLO:",Enployee87.name ,"Your Department is" , Enployee87.department ,"Your Age is", Enployee87.age ,"Is he present or absent?" , Enployee87.Present_or_No ,"Your Salary" , Enployee87.salary) , Enployee87.bonus()
  print("HELLO:",Enployee88.name , "Your Department is" , Enployee88.department ,"Your Age is", Enployee88.age ,"Is he present or absent?" , Enployee88.Present_or_No ,"Your Salary" , Enployee88.salary) , Enployee88.bonus()
  print("HELLO:",Enployee89.name , "Your Department is" , Enployee89.department ,"Your Age is", Enployee89.age ,"Is he present or absent?" , Enployee89.Present_or_No ,"Your Salary" , Enployee89.salary) , Enployee89.bonus()
  print("HELLO:",Enployee90.name , "Your Department is" , Enployee90.department ,"Your Age is", Enployee90.age ,"Is he present or absent?" , Enployee90.Present_or_No ,"Your Salary" , Enployee90.salary) , Enployee90.bonus()
  print("HELLO:",Enployee91.name , "Your Department is" , Enployee91.department ,"Your Age is", Enployee91.age ,"Is he present or absent?" , Enployee91.Present_or_No ,"Your Salary" , Enployee91.salary) , Enployee91.bonus()
  print("HELLO:",Enployee92.name , "Your Department is" , Enployee92.department ,"Your Age is", Enployee92.age ,"Is he present or absent?" , Enployee92.Present_or_No ,"Your Salary" , Enployee92.salary) , Enployee92.bonus()
  print("HELLO:",Enployee93.name , "Your Department is" , Enployee93.department ,"Your Age is", Enployee93.age ,"Is he present or absent?" , Enployee93.Present_or_No ,"Your Salary" , Enployee93.salary) , Enployee93.bonus()
  print("HELLO:",Enployee94.name , "Your Department is" , Enployee94.department ,"Your Age is", Enployee94.age ,"Is he present or absent?" , Enployee94.Present_or_No ,"Your Salary" , Enployee94.salary) , Enployee94.bonus()
  print("HELLO:",Enployee95.name , "Your Department is" , Enployee95.department ,"Your Age is", Enployee95.age ,"Is he present or absent?" , Enployee95.Present_or_No ,"Your Salary" , Enployee95.salary) , Enployee95.bonus()
  print("HELLO:",Enployee96.name , "Your Department is" , Enployee96.department ,"Your Age is", Enployee96.age ,"Is he present or absent?" , Enployee96.Present_or_No ,"Your Salary" , Enployee96.salary) , Enployee96.bonus()
  print("HELLO:",Enployee97.name , "Your Department is" , Enployee97.department ,"Your Age is", Enployee97.age ,"Is he present or absent?" , Enployee97.Present_or_No ,"Your Salary" , Enployee97.salary) , Enployee97.bonus()
  print("HELLO:",Enployee98.name , "Your Department is" , Enployee98.department ,"Your Age is", Enployee98.age ,"Is he present or absent?" , Enployee98.Present_or_No ,"Your Salary" , Enployee98.salary) , Enployee98.bonus()
  print("HELLO:",Enployee99.name ,  "Your Department is" , Enployee99.department ,"Your Age is", Enployee99.age ,"Is he present or absent?" , Enployee99.Present_or_No ,"Your Salary" , Enployee99.salary) , Enployee99.bonus()
  print("HELLO:",Enployee100.name  ,"Your Department is" , Enployee100.department ,"Your Age is",  Enployee100.age ,"Is he present or absent?" , Enployee100.Present_or_No ,"Your Salary" , Enployee100.salary) , Enployee100.bonus()

# Enployee99.bonus()


# ******
# 1 - الإسم                                   *    
# 2 - العمر                                  *
# 3 - القسم                                  *
# 4 - حاله حضوره                             *
# 5 - حاضر ام لا                              *
# 6 - الكود غير كامل بيانات العملاء ناقصه؟  *
# BY : MOHAMED ALAA MOHAMED (DEVELOPER  HERO) *
# *******





  
print("""\033[1;31m
  _  _           _                              _ 
 |  \/  |     | |                            | |
 | \  / | _ | |_   _ _ _ _ _   _  _| |
 | |\/| |/ _ \| '_ \ / ` | ' ` _ \ / _ \/ _` |
 | |  | | () | | | | (| | | | | | |  _/ (| |
 ||  ||\/|| ||\,|| || ||\_|\,|
 
█████╗  ██╗     █████╗  █████╗ 
██╔══██╗██║     ██╔══██╗██╔══██╗
███████║██║     ███████║███████║
██╔══██║██║     ██╔══██║██╔══██║
██║  ██║███████╗██║  ██║██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝                                              
\033[39m""")

print ("""\033[32m

██   ██ ███████ ██    ██         ████████ ██     ██  ██████        ██   ██ 
██  ██  ██       ██  ██             ██    ██     ██ ██    ██        ██ ██  
█████   █████     ████              ██    ██  █  ██ ██    ██ █████   ███   
██  ██  ██         ██               ██    ██ ███ ██ ██    ██        ██ ██  
██   ██ ███████    ██    ████████   ██     ███ ███   ██████        ██   ██ 
                                                                           
                                                                           

\033[39m""")

print("""\033[\033[34m
   [01]   Get IP Any Website
   [02]   Get IP Your Phone - Pc - Laptop
   [03]   Download A This Tool !
   [04]   Calculate Your Cumulative GPA
   [05]   Play Game
   [06]   Even Or Odd 
   [07]   Hack Insta
   [08]   device you have, Mac or Windows, phone or tablet,    and the Name of the tool file
   [09]   Create a mining file 
   [10]   Max Int Size 
   [11]   Write and listen 
   [12]   Data Of Any Website An Link    
   \33[31;1m[13]   Web Scraping For Any DOMIN Of Website {5$} For 5 Minutes  \33[39m
   \033[34m[14]   About TOOL..!?
  \033[34m [00]   About Developer
   
   [>>] BY : Mohamed Alaa [<<]
\033[39m""")
print (Box.DoubleCube (    "Key_Two-X [TOOL] [*** BY MOHAMMED ALAA DEVELOPER ***]"))
Write.Print("    Select any Number....\n\n",Colors.green_to_blue,interval=.01)
select = input("\033[1;33m    [>>>] Select Number : \033[39m")
if select:
  print('')
else:
  print('\033[1;31m    Please Write Anyting...\033[39m')
if select == '1':
  text()
elif select == '2':
  IP()
elif select == '3':
  tool()

#				exit()
elif select == '4':
  print("   Welcome To Users An Application Mark ")
  Mark1 = float(input("\033[32m  Enter  The First Subject : "))
  Mark2 = float(input("\033[32m  Entthe The Second  Subject : "))
  Mark3 = float(input("\033[32m  Enter The Third Subject : "))
  Mark4 = float(input("\033[1;31m  Enter The Fourth Subject : "))
  Mark5 = float(input("\033[1;31m  Enter The Fifth Subject : "))
  Mark6 = float(input("\033[1;31m  Enter The Sixth Subject : "))
  Mark7 = float(input("\033[1;34m  Enter The Seventh Subject : \033[39m"))
  e = (Mark1 + Mark2 + Mark3 + Mark4 + Mark5 + Mark6 + Mark7)
  p = float(e * 410 // 100)
  print("المعدل التراكمي هو :", p, "of 2870")
  print("النسبه المئوية هي :", p / 7, "of 410")
  print("     Egyptian education ")
elif select == '0' or select == '00':
  Open()
elif select == '5':
  books = []
  f1 = input("   Put any book : ")  #deep work
  books.append(f1)
  f2 = input("   Put any book 2 : ")  #scrum
  books.append(f2)
  print(f"\033[32m  Your Library: {books} \033[39m")
  f3 = input(
      "   Write the name of a book you will buy in the future : ")  #outlive
  f4 = input(
      "   Write the name of a book you will buy in the future another.. : "
  )  #Monday
  books.remove(f1)
  books.remove(f2)
  books.append(f3)
  books.append(f4)
  print(f"\033[32m  Your Whislist : {books}\033[39m")
  f5 = input("   Write a book off the wish list you've got : ")  #2Monday
  books.append(f1)
  books.append(f2)
  books.append(f5)
  print(f"\033[32m  Updated Library : {f1,f2,f4}\033[39m")
  books.append(f3)
  print(f"\033[32m  Updated WHISLIST : {f3}\033[39m")
  f6 = input(
      "\033[1;33m   Type the name of the book you want to donate choose beetwen f1 to f3 : \033[39m"
  ).lower()
  if f6.lower() == "f1":
        print(f"\033[\033[34m   After the donation, the library remains in it....{f2,f4} \033[39m")
  elif f6.lower() == "f2":
            print(f"\033[\033[34m   After the donation, the library remains in it....{f1,f4} \033[39m")
  elif f6.lower() == "f3":
                print(f"\033[\033[34m   After the donation, the library remains in it....{f3,f4} \033[39m")

#اداه جديده بعنوان Key_Two -X
#تحديث 1.1.0
#Update 1.1.0
#BY /\ MR : DEVELOPER OF PYTHON 
elif select == '6':
  on_play()
elif select == '7':
  pelo()
elif select == '8':
  apple()
elif select == "9":
  file()
elif select == '10':
  size()
elif select == "11":
  dor()
elif select =='12':
  data()
elif select =='13':
      # print("\t"f"\33[31;1mTHIS Mony IT is Not Enough\33[39m  {mony}")
      mony = input("\t"'\33[34;2mSet Mony For Useing This Command : \33[39m').lower()
      
      if mony.lower() == '%*%s':
            for i in tqdm(range(100), desc ="\33[95;1mDownload & Refresh Data \33[39m ",unit ="  \33[31;1mData Is Refreshd"):
                  sleep(.1111)
            print("\n\t\t\n""\33[36;2mPyment Not Found...\33[39m")
            print("\n\t\t\n""\33[31;2mPyment Not Found...\33[39m")
            print("\n\t\t\n""\33[33;2mPyment Not Found...\33[39m\n")
            exit()
                  
            
        
            import requests
            from bs4 import BeautifulSoup
            import ttkbootstrap as ttk
            from ttkbootstrap.constants import *
            from tkinter import ttk
            from tkinter import *
            from tkinter import messagebox 
            import socket
            import os
            from time import *
            import webbrowser

            def all_info():
                save_network.insert(0,get_info)
                
                


            def ip():
                IP_web.config(bootstyle='danger')
                IP_web ['state'] = 'disable'
                IP_web.delete(0,'end')
                web.delete(0,'end')
                save_network.delete(0,'end')
                IP.delete(0,'end')
                lb = ttk.Label(root,text="  Website IP ↓",font=("",12,"bold"),bootstyle="inverse-dark")
                lb.place(x=588,y=40,width=112,height=25)
                host = socket.gethostbyname(IP_web.get())
                web.insert(0,host)
              
                # i=messagebox.showerror("SyntaxError","Invalid IP and IP is Error Try Again..Please! If You Can't Geting IP Please Connect Support")
                # pass
            def delete_all():
                dell = messagebox.askokcancel("Delete and Settings Restart","are You Want To Delete All and Settings Restart if Accept Click Ok unAccept Click Cancel...")
                if dell == True:
                    IP_web.config(bootstyle='PRIMRY')
                    IP_web ['state'] = 'normal'
                    web.delete(0,'end')
                    save_network.delete(0,'end')
                    list_me.delete(0,'end')
                    IP.delete(0,'end')
                    IP_web.delete(0,'end')
                    rod.config (state = "normal")
                    rod.config(bootstyle="SUCCESS-outline-toolbutton")
                    rod ['text'] = 'Save Data'
                    IP_web.focus()
                    web.insert(0,"يظهر هنا IP " +","+" في الرابط https لا تكتب كلمه")
                    lb = ttk.Label(root,text="",font=("",12,"bold"))
                    lb.place(x=588,y=40,width=112,height=25)
                    messagebox.showwarning("INFO OUR APP","Settings Restart and Delete is Ok")
                else:
                    pass
                
                
                
            def connect ():
                con=messagebox.askokcancel("تواصل مع المطور","https://t.me/MRMEDO2"+"\nYes للتواصل اضغط"+"\n\n ©DELEVOPER / MOHAMMED ALAA")
                if con == True: 
                        messagebox.showinfo("....يتم التحويل","جاري تحويلك للتواصل شكرا لك") 
                        sleep(.50)
                        webbrowser.open("https://t.me/MRMEDO2") 
                else:
                        messagebox.showwarning("OK","....لم يتم التواصل")    

            def it_we():
                list_me.insert(10,".... تم رفح طلبك وهو تحت الإجراء")
                
            def Share():
              
                    i=messagebox.askretrycancel("root","Can't Sand Any Message...")
                    if i == True:
                        messagebox.askretrycancel("root","Can't Sand Any Message...")
                        messagebox.askretrycancel("root","Can't Sand Any Message...")
                        messagebox.showerror("root","Full All Rate....goodbay!")
                        
                        pass
                    elif i == False:
                        messagebox.showinfo("OPPS","Please Connect Us Of Support - Developer...")

            # Share()
            def deel():
                    list_me.delete(0,'end')
            root =Tk()
            root.iconbitmap('web.ico')
            root.title("Get Info Our Any Website")
            # root.resizable(False,False)
            # root.config (background = '#ff2010')
            root.state("zoomed")
            root.geometry("1400x550")
            MY = ttk.Label(root,text="\t\t\t\t\t\t"+"Developer : "+" Mohamed Alaa" ,font=("",15,"bold"),bootstyle="inverse-dark").pack(fill=X,side=TOP)

            # messagebox.showinfo("Get All Info",get_info)

            # show_info_website = ttk.Entry(root)
            # show_info_website.place(x=0,y=0,width=300,height=500)

            # bt_get = ttk.Button(root,text="Get all info an website",command=all_info)
            # bt_get.place(x=200,y=300)
            #------------------------------------
            #------------------------------------
            #------------------------------------
            lb = Label(root,text="Enter IP of Website For Get Info :",font=("",10,"bold")).place(x=760,y=45)
            all_info_web = ttk.Button(root,text="Get All info An Website", bootstyle=("primary-outline"),command=all_info)
            all_info_web.place(x=1060,y=75,width=150,height=30)
            IP = ttk.Entry(root,bootstyle="SUCCESS",show="●")
            IP.place(x=975,y=40,width=300,height=30)
            # show_password = Button(root,text="👁",command=show,font=("",10,"bold"),justify='center').place(x=530,y=40,height=25)
            #----------------------------------------------------------------------------------
            lb = Label(root,text="Ente Website Name For Get IP :",font=("",10,"bold")).place(x=8,y=45)
            all_info_website = ttk.Button(root,text="Get IP Of Website",command=ip,bootstyle=(DARK,OUTLINE))
            all_info_website.place(x=300,y=75,width=150)
            IP_web = ttk.Entry(root,bootstyle="PRIMRY",show="●") 
            IP_web.place(x=220,y=38,width=300,height=30)
            # p = input ("\033[1;32m   Enter A Domin : \033[39m")

                # print (host)
            #('\33[34;1mEnter IP For Geting Data an Website : \33[39m')

            req = requests.get(f'http://www.whois.com/whois/{IP}')
            src = req.content
            sop = BeautifulSoup(src)
            get_info =(root,sop.find_all('pre',{"df-raw"}))
            # print(get_info)
            save_network = Listbox(root,font=("",12,"bold"))
            save_network.place(x=220,y=110,width=1000,height=620)

            #--------------------
            web = Listbox(root,font=("",10,"bold"),justify='center',bg="#0984e3")
            web.insert(0,"يظهر هنا IP " +","+" في الرابط https لا تكتب كلمه")
            web.place(x=540,y=70,width=226,height=40)

            #----------------add code-----------------
            code = ttk.Label(root,text=" Control Settings : ",bootstyle="inverse-dark",font=("",14,"bold")).place(x=0,y=94,width=210)
            #------------------------------------------------------------------
            bt_delete = ttk.Button(root,text="Delete All and Restart All",command=delete_all,bootstyle=SUCCESS)
            bt_delete.place(x=35,y=133,width=170)
            #------------------------------------------------------------------
            bt_connect = ttk.Button(root,text="Connect With Us",command=connect,bootstyle=INFO)
            bt_connect.place(x=35,y=172,width=170)

            #------------------------------------------------------------------
            bt_share = ttk.Button(root,text="Share Program",bootstyle="warning",command=Share)
            bt_share.place(x=35,y=210,width=170)
            #------------------------------------------------------------------
            bt_help = ttk.Button(root,text="Help Me",bootstyle="pirmary")
            bt_help.place(x=35,y=245,width=170)
            #------------------------------------------------------------------
            bt_exit = ttk.Button(root,text="Exit App",command=root.quit,bootstyle="danger")
            bt_exit.place(x=35,y=280,width=170)
            #------------------------------------------------------------------
            #------------------------------------------------------------------

            list_me = Listbox(root,font=("",12,"bold"),justify="center",fg="#fff",bg="#000000")
            list_me.place(x=15,y=360,height=330,width=200)
            #------------------------------------------------------------------
            #------------------------------------------------------------------

            def Key():
                
                messagebox.showwarning("Error On Save Data","The Program can't Saved Any Data.... , Sorry! or it is Error")
                messagebox.showwarning("Error On Save Data","حدث خطأ. يُرجى إعادة المحاولة لاحقًا. (رقم تعريف التشغيل: Rt-6s0UC1B0e0Xsl) مزيد من المعلومات, Sorry! or it is Error")
                messagebox.showerror("Error On Save Data","The Program can't Saved Any Data.... , Sorry! or it is Error")
                rod.config (state = "disable")
                rod ['text'] = 'Data Saved'
                
                

            rod=ttk.Radiobutton(root,text="Save Data",bootstyle="SUCCESS-outline-toolbutton",command=Key)
            rod.place(x=40,y=320,width=150)

            # ---------------------------------
            # ---------------------------------
            man = ttk.Menubutton(root,text="Note Our App ",bootstyle="outline")
            man.place(x=5,y=700,width=200)

            sett = Menu(man,fg="#2ecc71")
            man  ["menu"]=sett
            sett.add_checkbutton(label=" [+] مسح قائمة المهام",command=deel)
            sett.add_checkbutton(label=" [+] سئ",command=it_we)
            sett.add_checkbutton(label=" [+] جيد",command=it_we)
            sett.add_checkbutton(label=" [+] جيد جدا",command=it_we)
            sett.add_checkbutton(label=" [+] ممتاز",command=it_we)
            sett.add_checkbutton(label=" [+] يحتاح الي المزيد من التطوير ",command=it_we)
            sett.add_checkbutton(label=" [+] عن المطور ",command=it_we)
            sett.add_checkbutton(label=" [+] شراء البرنامج ",command=it_we)
            sett.add_checkbutton(label=" [+] شراء النسخه المدفوعه من اصدار البرنامج ",command=it_we)
            sett.add_checkbutton(label=" [+] لا يتوافق مع جميع الأعمار",command=it_we)
            sett.add_checkbutton(label=" [+] إغلاق البرنامج",command=exit)
            # ---------------------------------
            # ---------------------------------
            os.system("cls")  
            root.mainloop()
      elif mony == "%d%S%D%":
                  from os import *
                  import requests
                  from bs4 import BeautifulSoup

                  #system("cls")

                  IP = input ("\t"'\33[32;1m   Enter IP For Geting Data an Website : \33[39m')
                  if IP :
                        ()
                  else:
                            print("\t"'\33[35;1mPlease Enter IP of WEBSITE...\33[39m')
                  req = requests.get(f'https://www.whois.com/whois/{IP}')
                  src = req.content
                  sop = BeautifulSoup(src)
                  get_info = sop.find_all('pre',{"df-raw"})
                  print (get_info)
      else:
        print("\t\n\t""\33[36;1mThis  Mony Not Enough , GOODBAY...!!\33[39m")
#system("cls")      
     

# Last Update Of Date 2024/1/7 at Clock 3:07AM
    
    
    
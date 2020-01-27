p = input('please enter one name:')
o = int(input('please enter a number:'))
if ((o<=20)and(o>=0)):
    no = open ('pycharm project.text',"a+")
    no.write(p)
    no.write(","+str(o)+"\r\n")
    no.close()
else:
    print(" error your number most be in range 0 to 20 ")
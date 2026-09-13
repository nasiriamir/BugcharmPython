VAR03 = 12
print(type(VAR03))

var09 = 2 ** (1/2)

print(type(var09))

var05 = 100.5
var10 = int(var05)
print(var10)

var11 = float(VAR03)
print(var11)

var11 = "150.3"

var12 = int(float(var11))
print(var12)

friend01 = 10
friend02 = 20
friend03 = 15

#NAMgozari moteghayera bayad ye seri ghavaed dashte bashe
seyed_debt = 10
meti_debt = 20
ehsan_debt = 15

#Faghat underline adad va hororf bozorg va kochik
#a z
#A Z
#0 9
#_

#lowercasenaming
mystudentnumber = 100

#UPPERCASENAMING
MUSTUDENTNUMBER = 200

#PascalCaseNaming
MyStudentNumber = 300

#camelCaseNaming
myStudentNumber = 400

#snake_case_naming
my_student_number = 500


#ghaede agar ye motayer mikhay meghdar sabet dashte bashe adat khobesh ine kole horofesh horof bozorg bashe age ye jaei to barnamat masalan y motagheyro 
PI = 3.14


var20 = var21 = var22 = 15.5
var20, var21, var22 = 15.5, 18, 25
print(var21)

money = 127
ten = money // 10
print(ten)
five = (money % 10) // 5
print(five)
one = (money % 10) % 5
print(one)

money = int(float(input("please enter an int number: "))) #input khodesh aval miad str migire
ten = money // 10
print(ten)
five = (money % 10) // 5
print(five)
one = (money % 10) % 5
print(one)
print(type(money))

#tamrin
a = 50
b = 73

c = b
b = a
a = c
print(a)
print(b)

var30 = 1001
print("this is even")

if var30 % 2 == 0:
    print("this is even")

if var30 % 2 == 1:
    print("this is odd")
    pass #vaghty miay pass minivisi yaani boro to in block az code vli (yaani manzoram ine ke mitoni ye sharty bzri baad pass bzni baad rad mikone mire in agar pass tanha bezari ye shart mizaram alan dakhelesh khalie vali baadan poresh mikonam)

if var30 > 1000: #mitoni y block az codo begiri va rooye on block baham tab bzni
    print("your number is greater than 1000")

else: #in else e miad be ghabli khodesh vasl mishe be ghabl tarin if i k hast ghablesh
    print("**********")

if var30 % 5 == 0:
    print('this is 0')
elif var30 % 5 == 1:
    print("this is 1")
    
#age biay hamasho masalan if bezani kar ezafe az computeret keshidi!
else:
    print("this is 1")

#Loops
var31 = int(input("adadi az mazrab se vared konid"))

#
for havij in range(100):
    var31 = int(input("adadi az mazrab se vared konid"))

    if var31 % 3 == 0:
        print("Doorod bar to!")
    else:
        var31 = int(input("adadi az mazrab se vared konid"))

while var31 % 3 != 0:
    var31 = int(input("adadi az mazrab se vared konid"))
# Set Method (py)
# Author: Md. Nuruzzaman Khan 
# 1.Enter the number of Set(s)
# 2.Enter element of the sets(separated by ",")
# 3.Enter the Set method (Example: Union,Intersection,Difference,Number of Elements,cross)

SetList=[]
Newst=[]

n=int(input("Enter the number of Set(s): "))
for x in range(n):
    if n==1:
        vv=input("Elements of this Set: ")
    else:
        vv=input("Elements of number {} Set: ".format(x+1))
    values=vv.split(",")
    SetList.append(set(values))
while True:
    mtd1=input("Set method: ")
    mtd=mtd1.lower().strip()
    if mtd[:2]=="un": # Union
        for y1 in range(n):
            Newst+=SetList[y1]
        print("Union= ",set(Newst))
        
    elif mtd[:2]=="in": # Intersection
        re=set(SetList[0])
        for j in range(n):
            temp=set(SetList[j])
            for y2 in range(n):
                temp.intersection_update(set(SetList[y2]))
            re.intersection_update(temp)
        if re==set():
            print("Intersection= {}")
        else:
            print("Intersection= ",re)

    elif mtd[:2]=="di": # Difference
        if n<=1:
            print("Another Set is required...")
        else:
            if n>2:
                num1=input("Enter two Set numbers: ").strip()
                num=num1.split(",")
                differ=set(SetList[int(num[0])-1]).difference(set(SetList[int(num[1])-1]))
            else:
                differ=set(SetList[0]).difference(set(SetList[1]))
            if differ==set():
                print("Difference= {}")
            else:
                print("Difference= ",differ)
   
    elif mtd[:2]=="nu" or mtd[:2]=="el" or mtd[:2]=="le":
        if len(SetList)==1:
            length=len(set(SetList[0]))
        else:
            get_set=int(input("Set number: "))-1
            length=len(set(SetList[get_set]))
        print("Number of elements= {}".format(length))

    elif mtd[:2]=="cr" or mtd[:2]=="car":
        if n>2:
            num1=input("Enter two Set numbers A, B: ").strip()
            num=num1.split(",")
        else:
            num=[1,2]
        product=[(x, y) for x in SetList[int(num[0])-1] for y in SetList[int(num[1])-1]]
        print("Cartesian Product‍‍‌,A X B = ",set(product))

    else:
        break


# OUTPUT:

# Enter the number of Set(s): 3
# Elements of number 1 Set: 1,2,3,4,5,6,7,8,9
# Elements of number 2 Set: 1,3,5,7,9
# Elements of number 3 Set: 2,4,6,8  
# Set method: union,
# Union=  {'2', '8', '3', '4', '6', '1', '5', '9', '7'}
# Set method: intersection
# Intersection= {}
# Set method: difference
# Enter two Set numbers: 1,3
# Difference=  {'3', '1', '5', '9', '7'}
# Set method: number of elements
# Set number: 1
# Number of elements= 9
# Set method: cross
# Enter two Set numbers A, B: 2,3
# Cartesian Product‍‍‌,A X B =  {('5', '6'), ('1', '4'), ('3', '4'), ('1', '2'), ('7', '4'), ('9', '8'), ('3','2'), ('7', '2'),
# ('5', '8'), ('9', '4'),('1', '6'), ('5', '4'), ('3', '6'), ('7', '6'), ('9', '2'), ('5', '2'), ('1', '8'), ('9', '6'), ('3', '8'), ('7', '8')}
# Set method: exit

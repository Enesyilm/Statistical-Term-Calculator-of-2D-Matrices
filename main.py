
import numpy as np

import math

import matplotlib.pyplot as plt

columnSize =3 #i defined size of the column in to a variable with that variable i can change number whenever i want

rowSize=150 #same with above

dataValues1= np.random.randint(10,150,size=(rowSize,columnSize))#created new random array between 10 to 150

dataValues=dataValues1.copy() #copied from datavalue1 the reason for copying is mod() function orders numbers in datavalues when i call it so i store real sequence in dataValues



def AddNewElement(input0,input1,input2):#Function that adds new elements to array

    dataValues =np.append(dataValues1,[[input0,input1,input2]],axis=0)#np.append could add new rows or columns,i need to add only rows so  i choosed axis =0

    return dataValues

def InterquartileRange(rowNumb):#function that finds InterquartileRange

    for i in range(rowSize):#sorting algorithm sorts array for preparation of calculating formula

        min=i;

        for j in range(i+1,rowSize):

            if dataValues[min][rowNumb] > dataValues[j][rowNumb]:

                min = j

        dataValues[i][rowNumb], dataValues[min][rowNumb] = dataValues[min][rowNumb], dataValues[i][rowNumb]#i already explained this at top lines

    if(len(dataValues)%2==0):#same algorithm logic with median function diffence is i added calculation q1 and q2 first and last quartile

        half=len(dataValues)//2

        result=(dataValues[half-1][rowNumb]+dataValues[half][rowNumb])/2

        quarter=half//2

        q1=dataValues[quarter][rowNumb]#calculates q1

        q2=dataValues[rowSize-1-quarter][rowNumb]#calculates q2

        temp=q2-q1
    else:

        half=len(dataValues)//2

        result =dataValues[half][rowNumb]

        quarter=half//2

        q1=(dataValues[quarter][rowNumb]+dataValues[quarter-1][rowNumb])/2#generally same with if statement the only difference: length of array is odd so index could be change bit

        q2=(dataValues[rowSize-1-quarter][rowNumb]+dataValues[rowSize-1-quarter+1][rowNumb])/2

        temp=q2-q1

    result=(q2-q1)

    return result

def MeanAbsoluteDeviation():

    value=[None]*columnSize

    for rowNumb in range(0,columnSize):#applies the function for all columns

        counter=0

        mean=ArithmeticAverage()[rowNumb]#calls results of average function from columns

        for i in range(rowSize):

            counter += abs(dataValues[i][rowNumb]-mean)#abs method turns values to absolute

        value[rowNumb]= round(counter/rowSize,1)#round method removes unnecessary digits before decimal point  from result

    return value

def CoefficientVariation():

    result=[None]*columnSize#defined array for all column results

    for rowNumb in range(0,columnSize):#applies the function for all columns

        #CoefficientVariable calculated according to Sample formule

        standartDev=StandartDeviation()[rowNumb]#we need Standart Deviation for calculating coefficientVariation

        mean=ArithmeticAverage()[rowNumb]#also need Average result

        result[rowNumb]= round(standartDev/mean,1)# applied formula and find CoefficientVariation

    return result

def StandartDeviation():

    #StandartDeviation calculated according to Sample formule

    standartDev=[None]*columnSize#defined array for all column results

    for rowNumb in range(0,columnSize):#applies the function for all columns

        standartDev[rowNumb]=round(math.sqrt(Variance()[rowNumb]),1)#saves the result in array we create at first

    return standartDev

def ArithmeticAverage():#finds aritmetic Average

    average=[None]*columnSize#created new array for store all column results in same variable

    for rowNumb in range(0,columnSize):#'for' loop that provides wander along columns

        counter=0#variable which sum all

        for i in range(rowSize):#wander among all elements in our list to sum all of it

            counter +=dataValues[i][rowNumb]#sums every element

        average[rowNumb]=round(counter/rowSize,1)#and applying Average formula

    return average

def RemoveElement():#Function that removes last elements in array

    dataValues=np.delete(dataValues1,len(dataValues1)-1,0)#i setup this method to erase last element but i could remove from every index

    return dataValues

def Mod(rowNumb):#hardest function of this task :d

    for i in range(rowSize):#first i am sorting array elements

        min=i;

        for j in range(i+1,rowSize):

            if dataValues[min][rowNumb] > dataValues[j][rowNumb]:

                min = j

        dataValues[i][rowNumb], dataValues[min][rowNumb] = dataValues[min][rowNumb], dataValues[i][rowNumb]#this line swaps index between old min value and new min value

    temp=dataValues[0][rowNumb]#variable for check previous element during 'for' loop

    counter=1

    maxNumbCount=1

    max=[dataValues[0][rowNumb],maxNumbCount]#first i am defined first element as a max it changes every time statements work

    for i in range(1,rowSize):#this 'for' loop wander along the elements

        if dataValues[i][rowNumb]==max[0]:

            maxNumbCount+=1#variable that counts most used Value

            max=[dataValues[i][rowNumb],maxNumbCount]#'max' variable holds most used Value

        elif dataValues[i][rowNumb]==temp:#if current value in loop same with previous one it increase counter by 1

            counter+=1

            if counter>maxNumbCount:#if current value counter more than counter of max than it assigns current number as max

                if len(max)>2:#when ide enter upper 'if' state that mean there is only one max used value in array

                    while len(max)>2:#it checks array of max in case there is more than one

                        max.pop()#deletes excess elements

                max[0]=dataValues[i][rowNumb]

                maxNumbCount+=1

                max[1]=maxNumbCount

            elif counter== maxNumbCount:#else works when current value counter same to maxcounter

                max.append(dataValues[i][rowNumb])# adds new index for arr because there is a two max numbers right now


        else:#if current value is not equal to previous one it resets counter

            temp=dataValues[i][rowNumb]#assigns it as a temp to show the current number as a reference in the next loop
            #
            counter=1
    max.pop(1)#function ejected element in index 1 because that value was maxcounter its counter for most used number(max)

    return max#and returns arr of max

def RangeFind():

    result=[None]*columnSize

    for rowNumb in range(0,columnSize):

        min= dataValues[0][rowNumb]

        max=min#min and max equal at first

        for i in range(rowSize):#'for' loop that finds min

            if min>dataValues[i][rowNumb]:

                min =dataValues[i][rowNumb]

            if max<dataValues[i][rowNumb]:#'for' loop that finds max in all rows in same column

                max=dataValues[i][rowNumb]

        result[rowNumb]=float(max-min)#substract min from max

    return result

def Variance():

    variance=[None]*columnSize

    for rowNumb in range(0,columnSize):#applies the function for all columns

        counter=0

        mean=ArithmeticAverage()[rowNumb]#calls results of average function from columns

        for i in range(rowSize):

            counter += (dataValues[i][rowNumb]-mean)**2#this line takes square of the diffence

        variance[rowNumb]= round(counter/(rowSize-1),1)#round method removes unnecessary digits before decimal point  from result


    return variance

def Boxplot():#i imported Matplotlib for calling Boxplot funct

    fig = plt.figure(figsize =(10, 7))

    ax = fig.add_axes([0, 0, 1, 1])

    plt.boxplot(dataValues)

    plt.show()

def Median():
    result=[None]*columnSize#i was explained this at average func

    for rowNumb in range(0,columnSize):#i was explained this at average func

        for i in range(rowSize):#wander among all elements in our list to sum all of it

            min=i;#storing min value


            for j in range(i+1,rowSize):#this is a sorting algorithm which is sorts by value

                if dataValues[min][rowNumb] > dataValues[j][rowNumb]:

                    min = j#min value changes every time that if statment find new min

            dataValues[i][rowNumb], dataValues[min][rowNumb] = dataValues[min][rowNumb], dataValues[i][rowNumb]#and this line swaps index

        if(len(dataValues)%2==0):#when sorting is done there is two statment, 'if' coded for cases that len of elements  is pair ,else coded for cases that len of elements is odd

            half=len(dataValues)//2#takes half of it

            result[rowNumb]=(dataValues[half-1][rowNumb]+dataValues[half][rowNumb])/2#and applies formula


        else:

            half=len(dataValues)//2#takes half of it but fractions are not included

            result[rowNumb] =dataValues[half][rowNumb]

    return result


def main():#menu works in here

    #the 'main' contains codes for menu only so it can be any shape the programmer wants so i wont have to explain all this
    global rowSize#values are global because im not defined all of these functions in a class  so cant make changes to this values from main

    global dataValues

    global dataValues1

    global x

    x="y"#init value

    while(x!="N" or x!="n"):#works until menu input is 'N' or'n'

        #this line informates users
        print('For add new element press(a|A): \nFor remove element press(r|R): \nFor print results in text press(p|P): \nBoxplot(b|B): \nFor determine application press(e|E): ')

        x = input()#takes input from user

        if(x=="a" or x=="a"):

            print("Enter number for first Column")

            c=int(input())

            print("Enter number for second Column")

            a=int(input())

            print("Enter number for third Column")

            b=int(input())

            dataValues=AddNewElement(c,a,b)

            dataValues1=dataValues.copy()

            rowSize+=1

        elif(x=='r' or x=='R'):

            dataValues=RemoveElement()

            dataValues1=dataValues.copy()

            rowSize-=1

        elif(x=='p'or x=='P'):

            file=open("Results.txt","w")#opened file for writing

            file.write("*********Daily numbers of house purchasing by foreign country citizens in Turkey for 200 day*********\n")#header of text file

            file.writelines(["                       USA","  England","  Germany\n"])



            file.write("ArithmeticAverage:     ")

            file.writelines([str(ArithmeticAverage()),"\n\n"])

            file.write("Variance:              ")

            file.writelines([str(Variance()),"\n\n"])

            file.write("StandartDeviation:     ")

            file.writelines([str(StandartDeviation()),"\n\n"])

            file.write("Median:                ")

            file.writelines([str(Median()),"\n\n"])

            file.write("RangeFind:             ")

            file.writelines([str(RangeFind()),"\n\n"])

            file.write("MeanAbsoluteDeviation: ")

            file.writelines([str(MeanAbsoluteDeviation()),"\n\n"])

            file.write("CoefficientVariation:   ")

            file.writelines([str(CoefficientVariation()),"\n\n"])

            file.write("InterquartileRange:    ")


            for rowNumb in range(0,columnSize):

                file.writelines(["[",str(InterquartileRange(rowNumb)),"]   "])

            file.write("\n\nMod:                   ")

            for rowNumb in range(0,columnSize):

                file.writelines([str(Mod(rowNumb)),"  "])

            file.writelines(["\n\nDataValues\n       US Eng Gr  "])

            for i in range(0,rowSize):

                file.writelines(["\n",str(i+1),".Day ",str(dataValues1[i])])

            file.close()

        elif(x=="b" or x=="B"):

            Boxplot()

        elif(x=="e" or x=="E"):

            break




if __name__ == "__main__":
    main()



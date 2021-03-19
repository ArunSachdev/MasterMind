from tkinter import *
import random
import sys

root=Tk()
root.title("Mastermind")

c=Canvas(root, height=700, width=800,bg="gray5", cursor="hand2")
id=c.create_rectangle(50,25,500,675, width=5, outline="white")
fnt=("Cooper Std Black",30,"underline")
id=c.create_text(650,130,text="MasterMind",font=fnt,fill="white")
quit=c.create_rectangle(600,430,700,470,width=2,outline="white",fill="gray50")
fnt=("Minion Pro Med",20)
idexit=c.create_text(650,450,text="QUIT",font=fnt,fill="white")

xd=65
yd=70
x1=70
y1=620
x2=110
y2=660

counter=0
counter1=0
counter2=0
flag1=0
flag2=0
flag3=0
flag4=0

cnt3=0
cnt4=0
flag5=0
flag6=0
flag7=0
flag8=0

cnt5=0
cnt6=0
flag9=0
flag10=0
flag11=0
flag12=0

cnt7=0
cnt8=0
flag13=0
flag14=0
flag15=0
flag16=0

cnt9=0
cnt10=0
flag17=0
flag18=0
flag19=0
flag20=0

cnt11=0
cnt12=0
flag21=0
flag22=0
flag23=0
flag24=0

cnt13=0
cnt14=0
flag25=0
flag26=0
flag27=0
flag28=0

l1=[random.choice('gybpo') for _ in range(4)]
l2=l1[:]
l3=l1[:]
l4=l1[:]
l5=l1[:]
l6=l1[:]
l7=l1[:]



temp1=[]
temp2=[]
temp3=[]
temp4=[]
temp5=[]
temp6=[]
temp7=[]
temp8=[]
temp9=[]
temp10=[]
temp11=[]
temp12=[]
temp13=[]
temp14=[]



gs1=[]
gs2=[]
gs3=[]
gs4=[]
gs5=[]
gs6=[]
gs7=[]

s=''
for i in l1:
	s=s+i

#top line
id=c.create_line(50,170,500,170, width=2, fill="white")

#first row - big circles
g1=c.create_oval(70,200,110,240, width=2, outline="white")
g2=c.create_oval(135,200,175,240, width=2, outline="white")
g3=c.create_oval(200,200,240,240, width=2, outline="white")
g4=c.create_oval(265,200,305,240, width=2, outline="white")

#first row - small circles
d1=c.create_oval(345,215,360,230, width=2, outline="white")
d2=c.create_oval(380,215,395,230, width=2, outline="white")
d3=c.create_oval(415,215,430,230, width=2, outline="white")
d4=c.create_oval(450,215,465,230, width=2, outline="white")

#second row
g5=c.create_oval(70,270,110,310, width=2, outline="white")
g6=c.create_oval(135,270,175,310, width=2, outline="white")
g7=c.create_oval(200,270,240,310, width=2, outline="white")
g8=c.create_oval(265,270,305,310, width=2, outline="white")

#second row - small circles
d5=c.create_oval(345,285,360,300, width=2, outline="white")
d6=c.create_oval(380,285,395,300, width=2, outline="white")
d7=c.create_oval(415,285,430,300, width=2, outline="white")
d8=c.create_oval(450,285,465,300, width=2, outline="white")

#third row
g9=c.create_oval(70,340,110,380, width=2, outline="white")
g10=c.create_oval(135,340,175,380, width=2, outline="white")
g11=c.create_oval(200,340,240,380, width=2, outline="white")
g12=c.create_oval(265,340,305,380, width=2, outline="white")

#third row - small circles
d9=c.create_oval(345,355,360,370, width=2, outline="white")
d10=c.create_oval(380,355,395,370, width=2, outline="white")
d11=c.create_oval(415,355,430,370, width=2, outline="white")
d12=c.create_oval(450,355,465,370, width=2, outline="white")

#fourth row
g13=c.create_oval(70,410,110,450, width=2, outline="white")
g14=c.create_oval(135,410,175,450, width=2, outline="white")
g15=c.create_oval(200,410,240,450, width=2, outline="white")
g16=c.create_oval(265,410,305,450, width=2, outline="white")

#fourth row - small circles
d13=c.create_oval(345,425,360,440, width=2, outline="white")
d14=c.create_oval(380,425,395,440, width=2, outline="white")
d15=c.create_oval(415,425,430,440, width=2, outline="white")
d16=c.create_oval(450,425,465,440, width=2, outline="white")

#fifth row 
g17=c.create_oval(70,480,110,520, width=2, outline="white")
g18=c.create_oval(135,480,175,520, width=2, outline="white")
g19=c.create_oval(200,480,240,520, width=2, outline="white")
g10=c.create_oval(265,480,305,520, width=2, outline="white")

#fifth row - small circles
d17=c.create_oval(345,495,360,510, width=2, outline="white")
d18=c.create_oval(380,495,395,510, width=2, outline="white")
d19=c.create_oval(415,495,430,510, width=2, outline="white")
d20=c.create_oval(450,495,465,510, width=2, outline="white")

#sixth row
g11=c.create_oval(70,550,110,590, width=2, outline="white")
g12=c.create_oval(135,550,175,590, width=2, outline="white")
g13=c.create_oval(200,550,240,590, width=2, outline="white")
g14=c.create_oval(265,550,305,590, width=2, outline="white")

#sixth row - small circles
d21=c.create_oval(345,565,360,580, width=2, outline="white")
d22=c.create_oval(380,565,395,580, width=2, outline="white")
d23=c.create_oval(415,565,430,580, width=2, outline="white")
d24=c.create_oval(450,565,465,580, width=2, outline="white")

#seventh row
g15=c.create_oval(70,620,110,660, width=2, outline="white")
g16=c.create_oval(135,620,175,660, width=2, outline="white")
g17=c.create_oval(200,620,240,660, width=2, outline="white")
g18=c.create_oval(265,620,305,660, width=2, outline="white")

#seventh row - small circles
d25=c.create_oval(345,635,360,650, width=2, outline="white")
d26=c.create_oval(380,635,395,650, width=2, outline="white")
d27=c.create_oval(415,635,430,650, width=2, outline="white")
d28=c.create_oval(450,635,465,650, width=2, outline="white")


#Colors
c1=c.create_oval(550,235,590,275, width=2, outline="green",fill="green")
c2=c.create_oval(630,235,670,275, width=2, outline="yellow",fill="yellow")
c3=c.create_oval(710,235,750,275, width=2, outline="blue",fill="blue")
c4=c.create_oval(590,290,630,330, width=2, outline="hotpink",fill="hotpink")
c5=c.create_oval(670,290,710,330, width=2, outline="orange",fill="orange")
	
def onClickc1(none):
	global counter
	counter+=1
	fillxy()
	id=c.create_oval(x1,y1,x2,y2, width=2, outline="green", fill="green")
	if counter==1 or counter==2 or counter==3 or counter==4:
		gs1.append('g')
	elif counter==5 or counter==6 or counter==7 or counter==8:
		gs2.append('g')
	elif counter==9 or counter==10 or counter==11 or counter==12:
		gs3.append('g')
	elif counter==13 or counter==14 or counter==15 or counter==16:
		gs4.append('g')
	elif counter==17 or counter==18 or counter==19 or counter==20:
		gs5.append('g')
	elif counter==21 or counter==22 or counter==23 or counter==24:
		gs6.append('g')
	elif counter==25 or counter==26 or counter==27 or counter==28:
		gs7.append('g')
	
	if counter==4:
		check1()
	elif counter==8:
		check2()
	elif counter==12:
		check3()
	elif counter==16:
		check4()
	elif counter==20:
		check5()
	elif counter==24:
		check6()
	elif counter==28:
		check7()
	
	

def onClickc2(none):
	global counter
	counter+=1
	fillxy()
	id=c.create_oval(x1,y1,x2,y2, width=2, outline="yellow", fill="yellow")
	if counter==1 or counter==2 or counter==3 or counter==4:
		gs1.append('y')
	elif counter==5 or counter==6 or counter==7 or counter==8:
		gs2.append('y')
	elif counter==9 or counter==10 or counter==11 or counter==12:
		gs3.append('y')
	elif counter==13 or counter==14 or counter==15 or counter==16:
		gs4.append('y')
	elif counter==17 or counter==18 or counter==19 or counter==20:
		gs5.append('y')
	elif counter==21 or counter==22 or counter==23 or counter==24:
		gs6.append('y')
	elif counter==25 or counter==26 or counter==27 or counter==28:
		gs7.append('y')
	
	if counter==4:
		check1()
	elif counter==8:
		check2()
	elif counter==12:
		check3()
	elif counter==16:
		check4()
	elif counter==20:
		check5()
	elif counter==24:
		check6()
	elif counter==28:
		check7()
		
		
def onClickc3(none):
	global counter
	counter+=1
	fillxy()
	id=c.create_oval(x1,y1,x2,y2, width=2, outline="blue", fill="blue")
	if counter==1 or counter==2 or counter==3 or counter==4:
		gs1.append('b')
	elif counter==5 or counter==6 or counter==7 or counter==8:
		gs2.append('b')
	elif counter==9 or counter==10 or counter==11 or counter==12:
		gs3.append('b')
	elif counter==13 or counter==14 or counter==15 or counter==16:
		gs4.append('b')
	elif counter==17 or counter==18 or counter==19 or counter==20:
		gs5.append('b')
	elif counter==21 or counter==22 or counter==23 or counter==24:
		gs6.append('b')
	elif counter==25 or counter==26 or counter==27 or counter==28:
		gs7.append('b')
	
	if counter==4:
		check1()
	elif counter==8:
		check2()
	elif counter==12:
		check3()
	elif counter==16:
		check4()
	elif counter==20:
		check5()
	elif counter==24:
		check6()
	elif counter==28:
		check7()
	
def onClickc4(none):
	global counter
	counter+=1
	fillxy()
	id=c.create_oval(x1,y1,x2,y2, width=2, outline="hotpink", fill="hotpink")
	if counter==1 or counter==2 or counter==3 or counter==4:
		gs1.append('p')
	elif counter==5 or counter==6 or counter==7 or counter==8:
		gs2.append('p')
	elif counter==9 or counter==10 or counter==11 or counter==12:
		gs3.append('p')
	elif counter==13 or counter==14 or counter==15 or counter==16:
		gs4.append('p')
	elif counter==17 or counter==18 or counter==19 or counter==20:
		gs5.append('p')
	elif counter==21 or counter==22 or counter==23 or counter==24:
		gs6.append('p')
	elif counter==25 or counter==26 or counter==27 or counter==28:
		gs7.append('p')
	
	if counter==4:
		check1()
	elif counter==8:
		check2()
	elif counter==12:
		check3()
	elif counter==16:
		check4()
	elif counter==20:
		check5()
	elif counter==24:
		check6()
	elif counter==28:
		check7()
	
def onClickc5(none):
	global counter
	counter+=1
	fillxy()
	id=c.create_oval(x1,y1,x2,y2, width=2, outline="orange", fill="orange")
	if counter==1 or counter==2 or counter==3 or counter==4:
		gs1.append('o')
	elif counter==5 or counter==6 or counter==7 or counter==8:
		gs2.append('o')
	elif counter==9 or counter==10 or counter==11 or counter==12:
		gs3.append('o')
	elif counter==13 or counter==14 or counter==15 or counter==16:
		gs4.append('o')
	elif counter==17 or counter==18 or counter==19 or counter==20:
		gs5.append('o')
	elif counter==21 or counter==22 or counter==23 or counter==24:
		gs6.append('o')
	elif counter==25 or counter==26 or counter==27 or counter==28:
		gs7.append('o')
	
	if counter==4:
		check1()
	elif counter==8:
		check2()
	elif counter==12:
		check3()
	elif counter==16:
		check4()
	elif counter==20:
		check5()
	elif counter==24:
		check6()
	elif counter==28:
		check7()
	
def fillxy():
	global x1,y1,x2,y2,yd,counter
		
	if counter==1:
		x1=70
		y1=620
		x2=110
		y2=660
	elif counter==2:
		x1=70+xd
		y1=620
		x2=110+xd
		y2=660
	elif counter==3:
		x1=x1+xd
		y1=620
		x2=x2+xd
		y2=660
	elif counter==4:
		x1=x1+xd
		y1=620
		x2=x2+xd
		y2=660
	elif counter==5:
		x1=70
		y1=620-yd
		x2=110
		y2=660-yd
	elif counter==6:
		x1=70+xd
		y1=620-yd
		x2=110+xd
		y2=660-yd
	elif counter==7:
		x1=x1+xd
		y1=620-yd
		x2=x2+xd
		y2=660-yd
	elif counter==8:
		x1=x1+xd
		y1=620-yd
		x2=x2+xd
		y2=660-yd
	elif counter==9:
		x1=70
		y1=620-(2*yd)
		x2=110
		y2=660-(2*yd)
	elif counter==10:
		x1=70+xd
		y1=620-(2*yd)
		x2=110+xd
		y2=660-(2*yd)
	elif counter==11:
		x1=x1+xd
		y1=620-(2*yd)
		x2=x2+xd
		y2=660-(2*yd)
	elif counter==12:
		x1=x1+xd
		y1=620-(2*yd)
		x2=x2+xd
		y2=660-(2*yd)
	elif counter==13:
		x1=70
		y1=620-(3*yd)
		x2=110
		y2=660-(3*yd)
	elif counter==14:
		x1=70+xd
		y1=620-(3*yd)
		x2=110+xd
		y2=660-(3*yd)
	elif counter==15:
		x1=x1+xd
		y1=620-(3*yd)
		x2=x2+xd
		y2=660-(3*yd)
	elif counter==16:
		x1=x1+xd
		y1=620-(3*yd)
		x2=x2+xd
		y2=660-(3*yd)
	elif counter==17:
		x1=70
		y1=620-(4*yd)
		x2=110
		y2=660-(4*yd)
	elif counter==18:
		x1=70+xd
		y1=620-(4*yd)
		x2=110+xd
		y2=660-(4*yd)
	elif counter==19:
		x1=x1+xd
		y1=620-(4*yd)
		x2=x2+xd
		y2=660-(4*yd)
	elif counter==20:
		x1=x1+xd
		y1=620-(4*yd)
		x2=x2+xd
		y2=660-(4*yd)
	elif counter==21:
		x1=70
		y1=620-(5*yd)
		x2=110
		y2=660-(5*yd)
	elif counter==22:
		x1=70+xd
		y1=620-(5*yd)
		x2=110+xd
		y2=660-(5*yd)
	elif counter==23:
		x1=x1+xd
		y1=620-(5*yd)
		x2=x2+xd
		y2=660-(5*yd)
	elif counter==24:
		x1=x1+xd
		y1=620-(5*yd)
		x2=x2+xd
		y2=660-(5*yd)
	elif counter==25:
		x1=70
		y1=620-(6*yd)
		x2=110
		y2=660-(6*yd)
	elif counter==26:
		x1=70+xd
		y1=620-(6*yd)
		x2=110+xd
		y2=660-(6*yd)
	elif counter==27:
		x1=x1+xd
		y1=620-(6*yd)
		x2=x2+xd
		y2=660-(6*yd)
	elif counter==28:
		x1=x1+xd
		y1=620-(6*yd)
		x2=x2+xd
		y2=660-(6*yd)

def check1():
	global counter1,flag1,flag2,flag3,flag4
	if l1[0]==gs1[0]:
		counter1+=1
		flag1=1
		
	if l1[1]==gs1[1]:
		counter1+=1
		flag2=1
		
	if l1[2]==gs1[2]:
		counter1+=1
		flag3=1
	
	if l1[3]==gs1[3]:
		counter1+=1
		flag4=1
		
	red1()	
	popred1()
	#print(gs1)
	#print(l1)
	checkw1()
	white1()
	

def popred1():
	global flag1,flag2,flag3,flag4,temp1,temp2
	if flag1==1:
		gs1.pop(0)
		gs1.insert(0,0)
		l1.pop(0)
		l1.insert(0,1)
		
	if flag2==1:
		gs1.pop(1)
		gs1.insert(1,0)
		l1.pop(1)
		l1.insert(1,1)
		
	if flag3==1:
		gs1.pop(2)
		gs1.insert(2,0)
		l1.pop(2)
		l1.insert(2,1)
		
	if flag4==1:
		gs1.pop(3)
		gs1.insert(3,0)
		l1.pop(3)
		l1.insert(3,1)
		
	for i in l1:
		if i not in temp1:
			temp1.append(i)
	#print(temp1)
	
	for i in gs1:
		if i not in temp2:
			temp2.append(i)
	#print(temp2)
		
def red1():
	global counter1
	if counter1==1:
		c.create_oval(345,635,360,650, width=2, outline="red",fill='red')
			
	elif counter1==2:
		c.create_oval(345,635,360,650, width=2, outline="red",fill='red')
		c.create_oval(380,635,395,650, width=2, outline="red",fill='red')
			
	elif counter1==3:
		c.create_oval(345,635,360,650, width=2, outline="red",fill='red')
		c.create_oval(380,635,395,650, width=2, outline="red",fill='red')
		c.create_oval(415,635,430,650, width=2, outline="red",fill='red')
				
	elif counter1==4:
		c.create_oval(345,635,360,650, width=2, outline="red",fill='red')
		c.create_oval(380,635,395,650, width=2, outline="red",fill='red')
		c.create_oval(415,635,430,650, width=2, outline="red",fill='red')
		c.create_oval(450,635,465,650, width=2, outline="red",fill='red')


def checkw1():
	global counter2,temp1
	for i in temp1:
		for j in temp2:
			if j==i:
				counter2+=1
	#print(counter2)
	
	
	
	
def white1():
	global counter2,counter1
	if counter1==0:
		if counter2==1:
			c.create_oval(345,635,360,650, width=2, outline="white",fill='white')
		elif counter2==2:
			c.create_oval(345,635,360,650, width=2, outline="white",fill='white')
			c.create_oval(380,635,395,650, width=2, outline="red",fill='red')
			
		elif counter2==3:
			c.create_oval(345,635,360,650, width=2, outline="white",fill='white')
			c.create_oval(380,635,395,650, width=2, outline="white",fill='white')
			c.create_oval(415,635,430,650, width=2, outline="white",fill='white')
					
		elif counter2==4:
			c.create_oval(345,635,360,650, width=2, outline="white",fill='white')
			c.create_oval(380,635,395,650, width=2, outline="white",fill='white')
			c.create_oval(415,635,430,650, width=2, outline="white",fill='white')
			c.create_oval(450,635,465,650, width=2, outline="white",fill='white')
			
	if counter1==1:
		if counter2==1:
			c.create_oval(380,635,395,650, width=2, outline="red",fill='red')
		elif counter2==2:
			c.create_oval(380,635,395,650, width=2, outline="white",fill='white')
			c.create_oval(415,635,430,650, width=2, outline="white",fill='white')
		elif counter2==3:
			c.create_oval(380,635,395,650, width=2, outline="white",fill='white')
			c.create_oval(415,635,430,650, width=2, outline="white",fill='white')
			c.create_oval(450,635,465,650, width=2, outline="white",fill='white')
			
	if counter1==2:
		if counter2==1:
			c.create_oval(415,635,430,650, width=2, outline="white",fill='white')
		elif counter2==2:
			c.create_oval(415,635,430,650, width=2, outline="white",fill='white')
			c.create_oval(450,635,465,650, width=2, outline="white",fill='white')
			
	if counter1==3:
		if counter2==1:
			c.create_oval(450,635,465,650, width=2, outline="white",fill='white')
			
	if counter1==4:
		fnt=("Comic Sans Ms",20)
		c.create_text(270,70,text="You Won!!",font=fnt,fill="white")
		fnt=("Comic Sans Ms",15)
		c.create_text(270,120,text="The Answer is {}".format(s),font=fnt,fill="white")
			
			
			
			
# For 2nd row
def check2():
	global cnt3,flag5,flag6,flag7,flag8
	if l2[0]==gs2[0]:
		cnt3+=1
		flag5=1
		
	if l2[1]==gs2[1]:
		cnt3+=1
		flag6=1
		
	if l2[2]==gs2[2]:
		cnt3+=1
		flag7=1
	
	if l2[3]==gs2[3]:
		cnt3+=1
		flag8=1
		
	red2()
	popred2()
	
	#print(gs2)
	#print(l2)
	checkw2()
	white2()

def popred2():
	global flag5,flag6,flag7,flag8,temp3,temp4
	
	
	if flag5==1:
		gs2.pop(0)
		gs2.insert(0,0)
		l2.pop(0)
		l2.insert(0,1)
		
	if flag6==1:
		gs2.pop(1)
		gs2.insert(1,0)
		l2.pop(1)
		l2.insert(1,1)
		
	if flag7==1:
		gs2.pop(2)
		gs2.insert(2,0)
		l2.pop(2)
		l2.insert(2,1)
		
	if flag8==1:
		gs2.pop(3)
		gs2.insert(3,0)
		l2.pop(3)
		l2.insert(3,1)
		
	for i in l2:
		if i not in temp3:
			temp3.append(i)
	#print(temp3)
	
	for i in gs2:
		if i not in temp4:
			temp4.append(i)
	#print(temp4)

def red2():
	global cnt3
	if cnt3==1:
		c.create_oval(345,565,360,580, width=2, outline="red",fill='red')
			
	elif cnt3==2:
		c.create_oval(345,565,360,580, width=2, outline="red",fill='red')
		c.create_oval(380,565,395,580, width=2, outline="red",fill='red')
			
	elif cnt3==3:
		c.create_oval(345,565,360,580, width=2, outline="red",fill='red')
		c.create_oval(380,565,395,580, width=2, outline="red",fill='red')
		c.create_oval(415,565,430,580, width=2, outline="red",fill='red')
				
	elif cnt3==4:
		c.create_oval(345,565,360,580, width=2, outline="red",fill='red')
		c.create_oval(380,565,395,580, width=2, outline="red",fill='red')
		c.create_oval(415,565,430,580, width=2, outline="red",fill='red')
		c.create_oval(450,565,465,580, width=2, outline="red",fill='red')
	
def checkw2():
	global cnt4
	for i in temp3:
		for j in temp4:
			if j==i:
				cnt4+=1
	#print(cnt4)
	
def white2():
	global cnt4,cnt3
	if cnt3==0:
		if cnt4==1:
			c.create_oval(345,565,360,580, width=2, outline="white",fill='white')
		elif cnt4==2:
			c.create_oval(345,565,360,580, width=2, outline="white",fill='white')
			c.create_oval(380,565,395,580, width=2, outline="red",fill='red')
			
		elif cnt4==3:
			c.create_oval(345,565,360,580, width=2, outline="white",fill='white')
			c.create_oval(380,565,395,580, width=2, outline="white",fill='white')
			c.create_oval(415,565,430,580, width=2, outline="white",fill='white')
					
		elif cnt4==4:
			c.create_oval(345,565,360,580, width=2, outline="white",fill='white')
			c.create_oval(380,565,395,580, width=2, outline="white",fill='white')
			c.create_oval(415,565,430,580, width=2, outline="white",fill='white')
			c.create_oval(450,565,465,580, width=2, outline="white",fill='white')
			
	if cnt3==1:
		if cnt4==1:
			c.create_oval(380,565,395,580, width=2, outline="red",fill='red')
		elif cnt4==2:
			c.create_oval(380,565,395,580, width=2, outline="white",fill='white')
			c.create_oval(415,565,430,580, width=2, outline="white",fill='white')
		elif cnt4==3:
			c.create_oval(380,565,395,580, width=2, outline="white",fill='white')
			c.create_oval(415,565,430,580, width=2, outline="white",fill='white')
			c.create_oval(450,565,465,580, width=2, outline="white",fill='white')
			
	if cnt3==2:
		if cnt4==1:
			c.create_oval(415,565,430,580, width=2, outline="white",fill='white')
		elif cnt4==2:
			c.create_oval(415,565,430,580, width=2, outline="white",fill='white')
			c.create_oval(450,565,465,580, width=2, outline="white",fill='white')
			
	if cnt3==3:
		if cnt4==1:
			c.create_oval(450,565,465,580, width=2, outline="white",fill='white')
			
	if cnt3==4:
		fnt=("Comic Sans Ms",20)
		c.create_text(270,70,text="You Won!!",font=fnt,fill="white")
		fnt=("Comic Sans Ms",15)
		c.create_text(270,120,text="The Answer is {}".format(s),font=fnt,fill="white")
			
			


# for 3rd row
def check3():
	global cnt5,flag9,flag10,flag11,flag12
	if l3[0]==gs3[0]:
		cnt5+=1
		flag9=1
		
	if l3[1]==gs3[1]:
		cnt5+=1
		flag10=1
		
	if l3[2]==gs3[2]:
		cnt5+=1
		flag11=1
	
	if l3[3]==gs3[3]:
		cnt5+=1
		flag12=1
		
	red3()	
	popred3()
	#print(gs3)
	#print(l3)
	checkw3()
	white3()
	

def popred3():
	global flag9,flag10,flag11,flag12,temp5,temp6
	if flag9==1:
		gs3.pop(0)
		gs3.insert(0,0)
		l3.pop(0)
		l3.insert(0,1)
		
	if flag10==1:
		gs3.pop(1)
		gs3.insert(1,0)
		l3.pop(1)
		l3.insert(1,1)
		
	if flag11==1:
		gs3.pop(2)
		gs3.insert(2,0)
		l3.pop(2)
		l3.insert(2,1)
		
	if flag12==1:
		gs3.pop(3)
		gs3.insert(3,0)
		l3.pop(3)
		l3.insert(3,1)
		
	for i in l3:
		if i not in temp5:
			temp5.append(i)
	#print(temp5)
	
	for i in gs3:
		if i not in temp6:
			temp6.append(i)
	#print(temp6)
		
def red3():
	global cnt5
	if cnt5==1:
		c.create_oval(345,495,360,510, width=2, outline="red",fill='red')
			
	elif cnt5==2:
		c.create_oval(345,495,360,510, width=2, outline="red",fill='red')
		c.create_oval(380,495,395,510, width=2, outline="red",fill='red')
			
	elif cnt5==3:
		c.create_oval(345,495,360,510, width=2, outline="red",fill='red')
		c.create_oval(380,495,395,510, width=2, outline="red",fill='red')
		c.create_oval(415,495,430,510, width=2, outline="red",fill='red')
				
	elif cnt5==4:
		c.create_oval(345,495,360,510, width=2, outline="red",fill='red')
		c.create_oval(380,495,395,510, width=2, outline="red",fill='red')
		c.create_oval(415,495,430,510, width=2, outline="red",fill='red')
		c.create_oval(450,495,465,510, width=2, outline="red",fill='red')


def checkw3():
	global cnt6,temp5
	for i in temp5:
		for j in temp6:
			if j==i:
				cnt6+=1
	#print(cnt6)
	
	
	
	
def white3():
	global cnt6,cnt5
	if cnt5==0:
		if cnt6==1:
			c.create_oval(345,495,360,510, width=2, outline="white",fill='white')
		elif cnt6==2:
			c.create_oval(345,495,360,510, width=2, outline="white",fill='white')
			c.create_oval(380,495,395,510, width=2, outline="red",fill='red')
			
		elif cnt6==3:
			c.create_oval(345,495,360,510, width=2, outline="white",fill='white')
			c.create_oval(380,495,395,510, width=2, outline="white",fill='white')
			c.create_oval(415,495,430,510, width=2, outline="white",fill='white')
					
		elif cnt6==4:
			c.create_oval(345,495,360,510, width=2, outline="white",fill='white')
			c.create_oval(380,495,395,510, width=2, outline="white",fill='white')
			c.create_oval(415,495,430,510, width=2, outline="white",fill='white')
			c.create_oval(450,495,465,510, width=2, outline="white",fill='white')
			
	if cnt5==1:
		if cnt6==1:
			c.create_oval(380,495,395,510, width=2, outline="red",fill='red')
		elif cnt6==2:
			c.create_oval(380,495,395,510, width=2, outline="white",fill='white')
			c.create_oval(415,495,430,510, width=2, outline="white",fill='white')
		elif cnt6==3:
			c.create_oval(380,495,395,510, width=2, outline="white",fill='white')
			c.create_oval(415,495,430,510, width=2, outline="white",fill='white')
			c.create_oval(450,495,465,510, width=2, outline="white",fill='white')
			
	if cnt5==2:
		if cnt6==1:
			c.create_oval(415,495,430,510, width=2, outline="white",fill='white')
		elif cnt6==2:
			c.create_oval(415,495,430,510, width=2, outline="white",fill='white')
			c.create_oval(450,495,465,510, width=2, outline="white",fill='white')
			
	if cnt5==3:
		if cnt6==1:
			c.create_oval(450,495,465,510, width=2, outline="white",fill='white')
			
	if cnt5==4:
		fnt=("Comic Sans Ms",20)
		c.create_text(270,70,text="You Won!!",font=fnt,fill="white")
		fnt=("Comic Sans Ms",15)
		c.create_text(270,120,text="The Answer is {}".format(s),font=fnt,fill="white")		
	
		
# for 4th row
def check4():
	global cnt7,flag13,flag14,flag15,flag16
	if l4[0]==gs4[0]:
		cnt7+=1
		flag13=1
		
	if l4[1]==gs4[1]:
		cnt7+=1
		flag14=1
		
	if l4[2]==gs4[2]:
		cnt7+=1
		flag15=1
	
	if l4[3]==gs4[3]:
		cnt7+=1
		flag16=1
		
	red4()
	popred4()
	#print(gs4)
	#print(l4)
	checkw4()
	white4()
	

def popred4():
	global flag13,flag14,flag15,flag16,temp7,temp8
	if flag13==1:
		gs4.pop(0)
		gs4.insert(0,0)
		l4.pop(0)
		l4.insert(0,1)
		
	if flag14==1:
		gs4.pop(1)
		gs4.insert(1,0)
		l4.pop(1)
		l4.insert(1,1)
		
	if flag15==1:
		gs4.pop(2)
		gs4.insert(2,0)
		l4.pop(2)
		l4.insert(2,1)
		
	if flag16==1:
		gs4.pop(3)
		gs4.insert(3,0)
		l4.pop(3)
		l4.insert(3,1)
		
	for i in l4:
		if i not in temp7:
			temp7.append(i)
	#print(temp7)
	
	for i in gs4:
		if i not in temp8:
			temp8.append(i)
	#print(temp8)
		
def red4():
	global cnt7
	if cnt7==1:
		c.create_oval(345,425,360,440, width=2, outline="red",fill='red')
			
	elif cnt7==2:
		c.create_oval(345,425,360,440, width=2, outline="red",fill='red')
		c.create_oval(380,425,395,440, width=2, outline="red",fill='red')
			
	elif cnt7==3:
		c.create_oval(345,425,360,440, width=2, outline="red",fill='red')
		c.create_oval(380,425,395,440, width=2, outline="red",fill='red')
		c.create_oval(415,425,430,440, width=2, outline="red",fill='red')
				
	elif cnt7==4:
		c.create_oval(345,425,360,440, width=2, outline="red",fill='red')
		c.create_oval(380,425,395,440, width=2, outline="red",fill='red')
		c.create_oval(415,425,430,440, width=2, outline="red",fill='red')
		c.create_oval(450,425,465,440, width=2, outline="red",fill='red')


def checkw4():
	global cnt8,temp7
	for i in temp7:
		for j in temp8:
			if j==i:
				cnt8+=1
	#print(cnt8)
	
	
	
	
def white4():
	global cnt8,cnt7
	if cnt7==0:
		if cnt8==1:
			c.create_oval(345,425,360,440, width=2, outline="white",fill='white')
		elif cnt8==2:
			c.create_oval(345,425,360,440, width=2, outline="white",fill='white')
			c.create_oval(380,425,395,440, width=2, outline="red",fill='red')
			
		elif cnt8==3:
			c.create_oval(345,425,360,440, width=2, outline="white",fill='white')
			c.create_oval(380,425,395,440, width=2, outline="white",fill='white')
			c.create_oval(415,425,430,440, width=2, outline="white",fill='white')
					
		elif cnt8==4:
			c.create_oval(345,425,360,440, width=2, outline="white",fill='white')
			c.create_oval(380,425,395,440, width=2, outline="white",fill='white')
			c.create_oval(415,425,430,440, width=2, outline="white",fill='white')
			c.create_oval(450,425,465,440, width=2, outline="white",fill='white')
			
	if cnt7==1:
		if cnt8==1:
			c.create_oval(380,425,395,440, width=2, outline="red",fill='red')
		elif cnt8==2:
			c.create_oval(380,425,395,440, width=2, outline="white",fill='white')
			c.create_oval(415,425,430,440, width=2, outline="white",fill='white')
		elif cnt8==3:
			c.create_oval(380,425,395,440, width=2, outline="white",fill='white')
			c.create_oval(415,425,430,440, width=2, outline="white",fill='white')
			c.create_oval(450,425,465,440, width=2, outline="white",fill='white')
			
	if cnt7==2:
		if cnt8==1:
			c.create_oval(415,425,430,440, width=2, outline="white",fill='white')
		elif cnt8==2:
			c.create_oval(415,425,430,440, width=2, outline="white",fill='white')
			c.create_oval(450,425,465,440, width=2, outline="white",fill='white')
			
	if cnt7==3:
		if cnt8==1:
			c.create_oval(450,425,465,440, width=2, outline="white",fill='white')
			
	if cnt7==4:
		fnt=("Comic Sans Ms",20)
		c.create_text(270,70,text="You Won!!",font=fnt,fill="white")
		fnt=("Comic Sans Ms",15)
		c.create_text(270,120,text="The Answer is {}".format(s),font=fnt,fill="white")				
			
	
	
#for 5th row
def check5():
	global cnt9,flag17,flag18,flag19,flag20
	if l5[0]==gs5[0]:
		cnt9+=1
		flag17=1
		
	if l5[1]==gs5[1]:
		cnt9+=1
		flag18=1
		
	if l5[2]==gs5[2]:
		cnt9+=1
		flag19=1
	
	if l5[3]==gs5[3]:
		cnt9+=1
		flag20=1
	
	red5()	
	popred5()
	#print(gs5)
	#print(l5)
	checkw5()
	white5()
	

def popred5():
	global flag17,flag18,flag19,flag20,temp9,temp10
	if flag17==1:
		gs5.pop(0)
		gs5.insert(0,0)
		l5.pop(0)
		l5.insert(0,1)
		
	if flag18==1:
		gs5.pop(1)
		gs5.insert(1,0)
		l5.pop(1)
		l5.insert(1,1)
		
	if flag19==1:
		gs5.pop(2)
		gs5.insert(2,0)
		l5.pop(2)
		l5.insert(2,1)
		
	if flag20==1:
		gs5.pop(3)
		gs5.insert(3,0)
		l5.pop(3)
		l5.insert(3,1)
		
	for i in l5:
		if i not in temp9:
			temp9.append(i)
	#print(temp9)
	
	for i in gs5:
		if i not in temp10:
			temp10.append(i)
	#print(temp10)
		
def red5():
	global cnt9
	if cnt9==1:
		c.create_oval(345,355,360,370, width=2, outline="red",fill='red')
			
	elif cnt9==2:
		c.create_oval(345,355,360,370, width=2, outline="red",fill='red')
		c.create_oval(380,355,395,370, width=2, outline="red",fill='red')
			
	elif cnt9==3:
		c.create_oval(345,355,360,370, width=2, outline="red",fill='red')
		c.create_oval(380,355,395,370, width=2, outline="red",fill='red')
		c.create_oval(415,355,430,370, width=2, outline="red",fill='red')
				
	elif cnt9==4:
		c.create_oval(345,355,360,370, width=2, outline="red",fill='red')
		c.create_oval(380,355,395,370, width=2, outline="red",fill='red')
		c.create_oval(415,355,430,370, width=2, outline="red",fill='red')
		c.create_oval(450,355,465,370, width=2, outline="red",fill='red')


def checkw5():
	global cnt10,temp9
	for i in temp9:
		for j in temp10:
			if j==i:
				cnt10+=1
	#print(cnt10)
	
	
	
	
def white5():
	global cnt10,cnt9
	if cnt9==0:
		if cnt10==1:
			c.create_oval(345,355,360,370, width=2, outline="white",fill='white')
		elif cnt10==2:
			c.create_oval(345,355,360,370, width=2, outline="white",fill='white')
			c.create_oval(380,355,395,370, width=2, outline="red",fill='red')
			
		elif cnt10==3:
			c.create_oval(345,355,360,370, width=2, outline="white",fill='white')
			c.create_oval(380,355,395,370, width=2, outline="white",fill='white')
			c.create_oval(415,355,430,370, width=2, outline="white",fill='white')
					
		elif cnt10==4:
			c.create_oval(345,355,360,370, width=2, outline="white",fill='white')
			c.create_oval(380,355,395,370, width=2, outline="white",fill='white')
			c.create_oval(415,355,430,370, width=2, outline="white",fill='white')
			c.create_oval(450,355,465,370, width=2, outline="white",fill='white')
			
	if cnt9==1:
		if cnt10==1:
			c.create_oval(380,355,395,370, width=2, outline="red",fill='red')
		elif cnt10==2:
			c.create_oval(380,355,395,370, width=2, outline="white",fill='white')
			c.create_oval(415,355,430,370, width=2, outline="white",fill='white')
		elif cnt10==3:
			c.create_oval(380,355,395,370, width=2, outline="white",fill='white')
			c.create_oval(415,355,430,370, width=2, outline="white",fill='white')
			c.create_oval(450,355,465,370, width=2, outline="white",fill='white')
			
	if cnt9==2:
		if cnt10==1:
			c.create_oval(415,355,430,370, width=2, outline="white",fill='white')
		elif cnt10==2:
			c.create_oval(415,355,430,370, width=2, outline="white",fill='white')
			c.create_oval(450,355,465,370, width=2, outline="white",fill='white')
			
	if cnt9==3:
		if cnt10==1:
			c.create_oval(450,355,465,370, width=2, outline="white",fill='white')
			
	if cnt9==4:
		fnt=("Comic Sans Ms",20)
		c.create_text(270,70,text="You Won!!",font=fnt,fill="white")
		fnt=("Comic Sans Ms",15)
		c.create_text(270,120,text="The Answer is {}".format(s),font=fnt,fill="white")	

#for 6th row
def check6():
	global cnt11,flag21,flag22,flag23,flag24
	if l6[0]==gs6[0]:
		cnt11+=1
		flag21=1
		
	if l6[1]==gs6[1]:
		cnt11+=1
		flag22=1
		
	if l6[2]==gs6[2]:
		cnt11+=1
		flag23=1
	
	if l6[3]==gs6[3]:
		cnt11+=1
		flag24=1
		
	red6()	
	popred6()
	#print(gs6)
	#print(l6)
	checkw6()
	white6()
	

def popred6():
	global flag21,flag22,flag23,flag24,temp11,temp12
	if flag21==1:
		gs6.pop(0)
		gs6.insert(0,0)
		l6.pop(0)
		l6.insert(0,1)
		
	if flag22==1:
		gs6.pop(1)
		gs6.insert(1,0)
		l6.pop(1)
		l6.insert(1,1)
		
	if flag23==1:
		gs6.pop(2)
		gs6.insert(2,0)
		l6.pop(2)
		l6.insert(2,1)
		
	if flag24==1:
		gs6.pop(3)
		gs6.insert(3,0)
		l6.pop(3)
		l6.insert(3,1)
		
	for i in l6:
		if i not in temp11:
			temp11.append(i)
	#print(temp11)
	
	for i in gs6:
		if i not in temp12:
			temp12.append(i)
	#print(temp12)
		
def red6():
	global cnt11
	if cnt11==1:
		c.create_oval(345,285,360,300, width=2, outline="red",fill='red')
			
	elif cnt11==2:
		c.create_oval(345,285,360,300, width=2, outline="red",fill='red')
		c.create_oval(380,285,395,300, width=2, outline="red",fill='red')
			
	elif cnt11==3:
		c.create_oval(345,285,360,300, width=2, outline="red",fill='red')
		c.create_oval(380,285,395,300, width=2, outline="red",fill='red')
		c.create_oval(415,285,430,300, width=2, outline="red",fill='red')
				
	elif cnt11==4:
		c.create_oval(345,285,360,300, width=2, outline="red",fill='red')
		c.create_oval(380,285,395,300, width=2, outline="red",fill='red')
		c.create_oval(415,285,430,300, width=2, outline="red",fill='red')
		c.create_oval(450,285,465,300, width=2, outline="red",fill='red')


def checkw6():
	global cnt12,temp11
	for i in temp11:
		for j in temp12:
			if j==i:
				cnt12+=1
	#print(cnt12)
	
	
	
	
def white6():
	global cnt12,cnt11
	if cnt11==0:
		if cnt12==1:
			c.create_oval(345,285,360,300, width=2, outline="white",fill='white')
		elif cnt12==2:
			c.create_oval(345,285,360,300, width=2, outline="white",fill='white')
			c.create_oval(380,285,395,300, width=2, outline="red",fill='red')
			
		elif cnt12==3:
			c.create_oval(345,285,360,300, width=2, outline="white",fill='white')
			c.create_oval(380,285,395,300, width=2, outline="white",fill='white')
			c.create_oval(415,285,430,300, width=2, outline="white",fill='white')
					
		elif cnt12==4:
			c.create_oval(345,285,360,300, width=2, outline="white",fill='white')
			c.create_oval(380,285,395,300, width=2, outline="white",fill='white')
			c.create_oval(415,285,430,300, width=2, outline="white",fill='white')
			c.create_oval(450,285,465,300, width=2, outline="white",fill='white')
			
	if cnt11==1:
		if cnt12==1:
			c.create_oval(380,285,395,300, width=2, outline="red",fill='red')
		elif cnt12==2:
			c.create_oval(380,285,395,300, width=2, outline="white",fill='white')
			c.create_oval(415,285,430,300, width=2, outline="white",fill='white')
		elif cnt12==3:
			c.create_oval(380,285,395,300, width=2, outline="white",fill='white')
			c.create_oval(415,285,430,300, width=2, outline="white",fill='white')
			c.create_oval(450,285,465,300, width=2, outline="white",fill='white')
			
	if cnt11==2:
		if cnt12==1:
			c.create_oval(415,285,430,300, width=2, outline="white",fill='white')
		elif cnt12==2:
			c.create_oval(415,285,430,300, width=2, outline="white",fill='white')
			c.create_oval(450,285,465,300, width=2, outline="white",fill='white')
			
	if cnt11==3:
		if cnt12==1:
			c.create_oval(450,285,465,300, width=2, outline="white",fill='white')
			
	if cnt11==4:
		fnt=("Comic Sans Ms",20)
		c.create_text(270,70,text="You Won!!",font=fnt,fill="white")
		fnt=("Comic Sans Ms",15)
		c.create_text(270,120,text="The Answer is {}".format(s),font=fnt,fill="white")

#for 7th row
def check7():
	global cnt13,flag25,flag26,flag27,flag28
	if l7[0]==gs7[0]:
		cnt13+=1
		flag25=1
		
	if l7[1]==gs7[1]:
		cnt13+=1
		flag26=1
		
	if l7[2]==gs7[2]:
		cnt13+=1
		flag27=1
	
	if l7[3]==gs7[3]:
		cnt13+=1
		flag28=1
		
	red7()
	popred7()
	#print(gs7)
	#print(l7)
	checkw7()
	white7()
	

def popred7():
	global flag25,flag26,flag27,flag28,temp13,temp14
	if flag25==1:
		gs7.pop(0)
		gs7.insert(0,0)
		l7.pop(0)
		l7.insert(0,1)
		
	if flag26==1:
		gs7.pop(1)
		gs7.insert(1,0)
		l7.pop(1)
		l7.insert(1,1)
		
	if flag27==1:
		gs7.pop(2)
		gs7.insert(2,0)
		l7.pop(2)
		l7.insert(2,1)
		
	if flag28==1:
		gs7.pop(3)
		gs7.insert(3,0)
		l7.pop(3)
		l7.insert(3,1)
		
	for i in l7:
		if i not in temp13:
			temp13.append(i)
	#print(temp13)
	
	for i in gs7:
		if i not in temp14:
			temp14.append(i)
	#print(temp14)
		
def red7():
	global cnt13
	if cnt13==1:
		c.create_oval(345,215,360,230, width=2, outline="red",fill='red')
			
	elif cnt13==2:
		c.create_oval(345,215,360,230, width=2, outline="red",fill='red')
		c.create_oval(380,215,395,230, width=2, outline="red",fill='red')
			
	elif cnt13==3:
		c.create_oval(345,215,360,230, width=2, outline="red",fill='red')
		c.create_oval(380,215,395,230, width=2, outline="red",fill='red')
		c.create_oval(415,215,430,230, width=2, outline="red",fill='red')
				
	elif cnt13==4:
		c.create_oval(345,215,360,230, width=2, outline="red",fill='red')
		c.create_oval(380,215,395,230, width=2, outline="red",fill='red')
		c.create_oval(415,215,430,230, width=2, outline="red",fill='red')
		c.create_oval(450,215,465,230, width=2, outline="red",fill='red')


def checkw7():
	global cnt14,temp13
	for i in temp13:
		for j in temp14:
			if j==i:
				cnt14+=1
	#print(cnt14)
	
	
	
	
def white7():
	global cnt14,cnt13
	if cnt13==0:
		if cnt14==1:
			c.create_oval(345,215,360,230, width=2, outline="white",fill='white')
		elif cnt14==2:
			c.create_oval(345,215,360,230, width=2, outline="white",fill='white')
			c.create_oval(380,215,395,230, width=2, outline="red",fill='red')
			
		elif cnt14==3:
			c.create_oval(345,215,360,230, width=2, outline="white",fill='white')
			c.create_oval(380,215,395,230, width=2, outline="white",fill='white')
			c.create_oval(415,215,430,230, width=2, outline="white",fill='white')
					
		elif cnt14==4:
			c.create_oval(345,215,360,230, width=2, outline="white",fill='white')
			c.create_oval(380,215,395,230, width=2, outline="white",fill='white')
			c.create_oval(415,215,430,230, width=2, outline="white",fill='white')
			c.create_oval(450,215,465,230, width=2, outline="white",fill='white')
			
	if cnt13==1:
		if cnt14==1:
			c.create_oval(380,215,395,230, width=2, outline="red",fill='red')
		elif cnt14==2:
			c.create_oval(380,215,395,230, width=2, outline="white",fill='white')
			c.create_oval(415,215,430,230, width=2, outline="white",fill='white')
		elif cnt14==3:
			c.create_oval(380,215,395,230, width=2, outline="white",fill='white')
			c.create_oval(415,215,430,230, width=2, outline="white",fill='white')
			c.create_oval(450,215,465,230, width=2, outline="white",fill='white')
			
	if cnt13==2:
		if cnt14==1:
			c.create_oval(415,215,430,230, width=2, outline="white",fill='white')
		elif cnt14==2:
			c.create_oval(415,215,430,230, width=2, outline="white",fill='white')
			c.create_oval(450,215,465,230, width=2, outline="white",fill='white')
			
	if cnt13==3:
		if cnt14==1:
			c.create_oval(450,215,465,230, width=2, outline="white",fill='white')
			
	if cnt13==4:
		fnt=("Comic Sans Ms",20)
		c.create_text(270,70,text="You Won!!",font=fnt,fill="white")
		fnt=("Comic Sans Ms",15)
		c.create_text(270,120,text="The Answer is {}".format(s),font=fnt,fill="white")
	else:
		fnt=("Comic Sans Ms",20)
		c.create_text(270,70,text="You Lost!!",font=fnt,fill="red")
		fnt=("Comic Sans Ms",15)
		c.create_text(270,120,text="The Answer is {}".format(s),font=fnt,fill="white")
		
def onQuit(none):
	root.quit()

c.tag_bind(idexit, '<ButtonPress-1>', onQuit)	
c.tag_bind(c1, '<ButtonPress-1>', onClickc1)
c.tag_bind(c2, '<ButtonPress-1>', onClickc2)
c.tag_bind(c3, '<ButtonPress-1>', onClickc3)
c.tag_bind(c4, '<ButtonPress-1>', onClickc4)
c.tag_bind(c5, '<ButtonPress-1>', onClickc5)
 
	
c.pack()
root.mainloop()

		


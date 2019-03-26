import random

def dig(stp):
	
	l=[['16','? ','14','? ','12','11'],
	   ['17','  ','  ','  ','  ','10'],
	   ['18','  ','  ','  ','  ','9 '],
	   ['? ','  ','W ','26','? ','? '],
	   ['20','? ','22','23','24','7 '],
	   ['1 ','2 ','3 ','? ','5 ','6 ']]
	for k in range (len(l)):
		for j in range (len(l[k])):
		 if(l[k][j]!="? ") and l[k][j]!="  " and l[k][j]!="W ":  
	  	  g= int(l[k][j])
		  if stp==g:
			l[k][j]="@ "		
	for m in l:
		for n in m:		
			print n,"",
 		print"\n"



def quest(qn):
	q=[["qn1.the first web based e-mail is called ","hot mail "],
	  ["qn2.which company is nicknamed big blue ","IBM"],
	  ["qn3.it is a small pidce of test stored ion user's computer by a web browser in maintaining the state. What is it?", "cookie"],
	  ["qn4.in internet terminology IP means ","internet protocol"],
	  ["qn5.the first page of a website is called ","homepage"],
	  ["qn6.website address is a unique name that identifies a specific ____ on the the web ","link"],
	  ["qn7.the standard protocol of internet is ","IP"],
	  ["qn8.the founder of netscape communication ","Marc Anderson"],
	  ["qn9.the inventor of world wide web ","Tim Berners Lee"],
	  ["qn10.the father of internet ","Vint Cerf"]]
	for i in range(0,10):
	  if i==qn:
	  	print q[i][0]
	        break
	s=raw_input("enter the answer : ")
	if q[qn][1]==s:
		print" your answer is correct"
		return 1
	else:
		print "your answer is wrong "
		return 0		


def pos(stp,qn,lf):
	if stp==4:
		print""" wizard had fallen into a fox's den ...,the cunning fox would only let wizard stay   
if he answers the question correctly. Your QUESTION is: """
		g=quest(qn)
		if g==0:
			lf-=2
			stp-=3
		qn+=1
	elif stp==8:
		print"""wizard met a wild trojan horse....,the wild horse would only let wizard stay   
if he answers the question correctly. Your QUESTION is: """
		g=quest(qn)
		if g==0:
			lf-=2
			stp-=2
		qn+=1
	elif stp==13:
		print"""wizard found a well.... which has magical water that could restore wizared's life by 5
..wizard drnk the water got lot of energy and jumped 4 steps """
		lf+=5
		stp+=4
	elif stp==19:
		print"""wizard saw a large python snake ...the snake would only let the wizard stay   
if he answers the question correctly. Your QUESTION is: """
	 	g=quest(qn)
		if g==0:
			lf-=4
			stp-=3
		qn+=1
	elif stp==21:
		print"""wizard ran into a bush,which was under the territory of a mouse... the mouse would only let him stay if he answers 
the queation correctly.Your QUESTION is: """
		g=quest(qn)
		if g==0:
			lf=-1
			stp=-2 
		qn+=1
	elif stp==15:
		print""" wizard saw an apple tree ,he was so tired that he wished to have an apple... the wizard could only have the apple ,if he answers the question correctly  .Your quetion is: """	
		g=quest(qn)
                if g==0:
			lf-=3
			stp-=0	
		qn+=1
 	elif stp==25:		
		print """wizard met the deadly villain virus...the virus only let the wizard stay   
if he answers the question correctly. Your QUESTION is: """
		g=quest(qn)
		if g==0:
			lf-=5
			stp-=8
		qn+=1

	print"now you are on step: ",stp
	print "your life is ",lf
	return stp,qn,lf




print"                    COMPUTER   WIZARD "
print""" Once up on a time, an virus stole a valuable data which could save human race and hid in the 
softwares jungle . To regain the data the programmer asks the computer wizard for help.....
ARE YOU WILLING TO ASSIST THE COMPUTER WIZARD IN REGAINING THE DATA ?"""
c=raw_input("Enter y-yes & n-no  ")
if(c=='y'): 
 print """
                                         WELCOME TO COMPUTER WIZARD

		******************************************************************
		*	   |APPLE     | 	 |restoring|	      |  	 *
		*    16	   | step:0   |    14	 |  well   |	12    |	   11	 *
		*__________| life:-3  |__________|         |__________|__________*
		*	   |-----------		 |step:+4  |	      |		 * 
		*    17	   | 			 |life:+5  |	      |	   10	 *
		*__________|                      ---------           |__________*		 
		*	   |	    ____________                      |	         *
		*    18	   | 	   |            |           ----------|	   9 	 *
		*__________|       | \        / |___________|  VIRUS  |__________*		 	
		*PYTHON		   |  \  /\  / 	|	    | step:-8 |	 TROJAN  *
		*  step:-3 |	   |   \/  \/ON	|    26	    | life:-6 |	step:-3  *
		*__life:-4_|_______|____________|___________|_________| life:-2  * 	
		*	   | MOUSE    |		|     	    |	      |__________* 
		*    20    |step:-4   |   22    |    23	    |   24    |    	 *
		*__________|life:-3___|_________|___________|_________|    7     *
		*          | 	      | 	|   FOX	    |	      |__________* 	
		*   start  |	2     |   3	| step:-2   | 	5     |	   6     * 
		*     1    |          |         | life:-2   |         |          *
		******************************************************************     
 
                  """
 print"""rules:
 1.innitial life :10 
 2.game over when life=0
 3.on each encounter with obstacles,the animals would ask a question; if correct answer is provided the wizard would be uneffected
 4.game won when step=23
  
 START"""
 stp=0
 lf=10
 qn=0

 c=raw_input("Do you want to roll the dice?  ") 
 while (c=='y' and stp<27 and lf>0) :
	print "Rolling the dices..."
    	a=random.randint(1,6)
	print """
		 ___
 		| . |	
	.......	|___|....  the value is	""",a
	print"\n"
	stp+=a
    	if stp<27:	
		stp,qn,lf=pos(stp,qn,lf)
		print"\n"
		dig(stp)
		print"\n"
    		roll_again = raw_input(" Roll the dice again?  ")
	

    	elif stp==27:
		print "congrajulations ..."
		print "GAME WON "
		break

   	else:
		stp-=a
		print "sorry, you have cross the limit of steps.."
		print"try again"
		print"\n"
		c=raw_input("Do you want to roll the dice again ") 












	


 


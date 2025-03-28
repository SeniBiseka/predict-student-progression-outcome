
 # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.

 # Any code taken from other sources is referenced within my code solution.

 # Student ID: 20531122(UOW)\20232416(IIT ID)

 # Date: 14.11.2023 


## Part- 1, 2, 3

from graphics import*


def out_range():
    """Print Out of range"""
    
    print("Out of range. ")
    print()


def another_set():
    """Ask the user wants to enter another set
    of data and get the input return the input
    to work with it later. """
    
    print()
    print("Would you like to enter another set of data? ")
    choice=input("Enter 'y' for yes or 'q' to quit and view results: ")
    choice=choice.lower()
    while choice!='y' and choice!='q':
        print("Invalid option. Check and enter again. ")
        print()
        choice=input("Enter 'y' for yes or 'q' to quit and view results: ")
        
    print()
    return choice


def List():             
    """Access the stored data from the list, data_list
    and display the data. """
    
    print()
    print("Part 2: ")
    for data in data_list:      #https://zzzcode.ai/code-generator?id=29aff5eb-f703-4c94-aedc-4a1e72dcb869
        print(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}")
        

def text_File():
    """Save the inputted data to a text file named
    'progression_outcomes.txt' and access the stored
    data and print """
    
    f=open("progression_outcomes.txt",'w')
    f.write("Part 3:\n")

    for data in data_list:
        f.write(f"{data[0]} - {data[1]}, {data[2]}, {data[3]}\n")

    f.close()

    f=open("progression_outcomes.txt",'r')
    print()
    print(f.read())


        #drawing the histogram  #called the List() and text_File() functions       
def histogram():                            
    """Displaying a Histogram with the data inputed
    using the graphics.py module. Then call the
    List() function and the text_File() function"""
    
    win=GraphWin("Histogram",800,600)
    win.setBackground(color_rgb(237,242,236))

    # the x axis
    x_axis=Line(Point(50,500),Point(750,500))
    x_axis.draw(win)


    ###drawing Rectangles
    # Progress box - Box 1
    box_1=Rectangle(Point(100,500),Point(235,box1_len))
    box_1.setFill(color_rgb(172,249,164))
    box_1.draw(win)

    # Trailer box - Box 2
    box_2=Rectangle(Point(255,500),Point(390,box2_len))
    box_2.setFill(color_rgb(160,198,137))
    box_2.draw(win)

    # Retriever box - Box 3
    box_3=Rectangle(Point(410,500),Point(545,box3_len))
    box_3.setFill(color_rgb(167,188,119))
    box_3.draw(win)

    # Excluded box - Box 4
    box_4=Rectangle(Point(565,500),Point(700,box4_len))
    box_4.setFill(color_rgb(210,182,181))
    box_4.draw(win)


    ###adding Text
    # Hisrogram Results title
    title=Text(Point(226,40),"Histogram Results")
    title.setSize(21)
    title.setStyle("bold")
    title.setTextColor(color_rgb(98,98,98))
    title.draw(win)

    # Progress text
    title_1=Text(Point(167,520),"Progress")
    title_1.setSize(16)
    title_1.setStyle("bold")
    title_1.setTextColor(color_rgb(122,134,153))
    title_1.draw(win)

    # Trailer text
    title_2=Text(Point(322,520),"Trailer")
    title_2.setSize(16)
    title_2.setStyle("bold")
    title_2.setTextColor(color_rgb(122,134,153))
    title_2.draw(win)

    # Retriever text
    title_3=Text(Point(477,520),"Retriever")
    title_3.setSize(16)
    title_3.setStyle("bold")
    title_3.setTextColor(color_rgb(122,134,153))
    title_3.draw(win)

    # Excluded text
    title_4=Text(Point(632,520),"Excluded")
    title_4.setSize(16)
    title_4.setStyle("bold")
    title_4.setTextColor(color_rgb(122,134,153))
    title_4.draw(win)

    # Outcome total text
    title_5=Text(Point(245,560),str(total_count)+" outcomes in total.")
    title_5.setSize(18)
    title_5.setStyle("bold")
    title_5.setTextColor(color_rgb(122,134,153))
    title_5.draw(win)

    ## Outcome texts above the Rectangles
     #Progress outcome
    outcome_1=Text(Point(167,outcome1_len),progress_count)
    outcome_1.setSize(17)
    outcome_1.setStyle("bold")
    outcome_1.setTextColor(color_rgb(122,134,153))
    outcome_1.draw(win)

    #Trailer outcome
    outcome_2=Text(Point(322,outcome2_len),trailer_count)
    outcome_2.setSize(17)
    outcome_2.setStyle("bold")
    outcome_2.setTextColor(color_rgb(122,134,153))
    outcome_2.draw(win)

    #Retriever outcome
    outcome_3=Text(Point(477,outcome3_len),retriever_count)
    outcome_3.setSize(17)
    outcome_3.setStyle("bold")
    outcome_3.setTextColor(color_rgb(122,134,153))
    outcome_3.draw(win)

    #Excluded outcome
    outcome_4=Text(Point(632,outcome4_len),exclude_count)
    outcome_4.setSize(17)
    outcome_4.setStyle("bold")
    outcome_4.setTextColor(color_rgb(122,134,153))
    outcome_4.draw(win)

    List()

    text_File()

    win.mainloop()



#initializing counts to zero
total_count=0
progress_count=0
trailer_count=0
retriever_count=0
exclude_count=0


#ask whether the user is a student(1) or a staff member(0)  
who=input("Please enter 0 if you are a Staff member.\nPlease enter 1 if you are a Student: ")
while who!= '1' and who!='0':
    print("Invalid option. Check and enter again. ")
    print()
    who=input("Please enter 0 if you are a Staff member.\nPlease enter 1 if you are a Student: ")
    
print()

#making a list to store data entered
data_list=[]

choice=True  #initializing before the loop

while True:
    try:
        passc=int(input("Enter your total PASS credits: ")) #pass credit input
        while passc not in range(0,130,20):
            out_range()
            passc=int(input("Enter your total PASS credits: "))
            
        defer=int(input("Enter your total DEFER credits: "))#defer credit input
        while defer not in range(0,130,20):
            out_range()
            defer=int(input("Enter your total DEFER credits: "))

        fail=int(input("Enter your total FAIL credits: "))#fail credit input
        while fail not in range(0,130,20):
            out_range()
            fail=int(input("Enter your total FAIL credits: "))


        if passc+defer+fail==120: #checking the total is equal to 120
            total_count+=1 

            if passc==120:
                print("Progress")                    #Progress
                progress_count+=1
                data_list.append(["Progress",passc,defer,fail])
                            
            elif passc==100:
                print("Progress (module trailer)")   #Trailer
                trailer_count+=1
                data_list.append(["Progress (module trailer)",passc,defer,fail])
                            
            elif passc+defer>=fail:
                print("Module retriever")            #Retriever
                retriever_count+=1
                data_list.append(["Module retriever",passc,defer,fail])
                            
            else:
                passc+defer<fail
                print("Exclude")                     #Exclude
                exclude_count+=1
                data_list.append(["Exclude",passc,defer,fail])

        else:
            print("Total incorrect.")
            print()
            continue
            
                           #student=1   #staff member=0
        if who=='0':       #program for a staff member        
            
            CHOICE=another_set()  #ask whether the staff member wants to add another set
            
            if CHOICE=='q': #using 'q' to quit

                #finding the y co-ordinates for the rectangles in the histogram
                box1_len= 500-(25*progress_count)
                box2_len= 500-(25*trailer_count)
                box3_len= 500-(25*retriever_count)
                box4_len= 500-(25*exclude_count)
                
                #finding the y co-ordinates for the outcome results
                outcome1_len= box1_len-15
                outcome2_len= box2_len-15   
                outcome3_len= box3_len-15
                outcome4_len= box4_len-15
                
                histogram()
                
                break


        else:             #program for a student
            
            List()           #display the list

            text_File()      #save to a text file 
            
            break


    except ValueError:
        print("Integer required")
        print()
        


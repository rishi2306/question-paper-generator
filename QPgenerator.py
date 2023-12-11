import mysql.connector as co
import random
import itertools
from operator import itemgetter
import tabulate

user = input("Enter username for SQL:")
password = input("Enter password:")
database = input("Enter database name: ")
con = co.connect(user = user,password = password, host = 'localhost', database = database)
if con.is_connected():
    print("Connected")
else:
    print("Not connected")
cur = con.cursor()
#--------------------------------

def qbankmaker():
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        q = input("Enter question:")
        m = int(input("Enter number of marks for this question:"))
        #cur.execute("USE {}".format(database))
        cur.execute("INSERT INTO {} (question, marks) VALUES (%s, %s)".format(tname), (q, m))
        con.commit()
        ch = input("Do you want to continue? Y or N?:")

#Start of comberqmbp() for option 3 - making qpaps based on marks and number of questions
def comberqmbp(): #COMBINATION MAKER - for making question papers based on marks and number of questions
    lst = []
    mlist = list(qmdict.values())


    while True:
        try:
            for combo in itertools.combinations(mlist, qn):
                if sum(combo) == m:
                    lst.append(combo)
            break
        except:
            print("No valid combinations for", m, "marks", "and ", qn, "number of questions")

    l1 = []
    for qbp in lst:
        if qbp not in l1:
            l1.append(tuple(sorted(qbp)))
    
    global qbps
    qbps = list(set(l1))

    if len(qbps) == 0:
        #print("No valid combinations can be made")
        return False
    else:
        return True
#End of comberqmbp() for option 3 - making qpaps based on marks and number of questions

#------------------------

#Start of qbnum() - making question papers based on number of questions(option1)
def qbpnum():
    qpapnum = int(input("How many question papers do you want?:")) #number of questionpapers

    for count in range(1, qpapnum+1):
        print("Paper", count)
        qnum = int(input("How many questions do you want the paper"+str(count)+" to have?: ")) #no. of questions in each paper

        s = 0
        if qnum<=len(qmdictkeys):

            qpap = open("/Users/grishichakravarthy/Desktop/questionpapers/qpaper" + str(count) + ".txt", "a+")  # making/opening question papers
            qdict = {}

            for x in range(qnum):
                while s!=len(qmdictkeys):
                    q = random.choice(qmdictkeys)
                    #qpap.seek(0)
                    if q not in qdict:
                        qmarks = qmdict[q]
                        qdict[q]=qmarks
                        s+=1
                        break
                    else:
                        pass

            sortedqmdict = dict(sorted(qdict.items(), key=itemgetter(1)))
            l = list(sortedqmdict.values())
            s = list(set(l))
            L = []

            for unqm in s:
                lst = []
                for i in range(l.count(unqm)):
                    lst.append(unqm)
                L.append(lst)

            sec = ord('A')
            num = 1
            for unqmlist in L:
                if len(unqmlist)>1:
                    qpap.write(str("Section" + str(chr(sec) + "-" + str(unqmlist[0]) + "markers:" + str(unqmlist[0]) + "M" + "*" + str(len(unqmlist)) + "=" + str(str(len(unqmlist)*unqmlist[0])) + "M" + "\n")))
                else:
                    qpap.write(str("Section" + str(chr(sec) + "-" + str(unqmlist[0]) + "marker\n")))

                for m in unqmlist:
                    while True:
                        q = random.choice(list(sortedqmdict.keys()))
                        qpap.seek(0)
                        if (sortedqmdict[q] == m) and (q not in qpap.read()):
                            qpap.write(str(num)+"." + q + '\n')
                            break
                        else:
                            pass
                    num+=1
                sec += 1
                qpap.write("---------------------\n")


            qpap.close()

        else:
            print("Number of questions in questions bank is low")



#End of qbnum() - making question papers based on number of questions(option 1)

#------------------------'''

#Start of qbpmarks() - making question papers based on total marks(option 2)
def qbpmarks():

    qpapnum = int(input("How many question papers do you want?:"))  # number of questionpapers

    for count in range(1, qpapnum+1):
        print("Paper", count)
        marks = int(input("How many marks do you want your paper to be for?: "))
        bpslst = []
        while True:
            try:
                for size in range(1, len(mlist) + 1):
                    for combo in itertools.combinations(mlist, size):
                        if sum(combo) == marks and sorted(combo) not in bpslst:
                            bpslst.append(sorted(combo))
                break
            except:
                break
        if len(bpslst)==0:
            print("No question papers can be generated - Entered total marks exceeds the maximum marks of the question bank")
        else:
            qpap = open("/Users/grishichakravarthy/Desktop/questionpapers/qpaper" + str(count) + ".txt","a+")  # making/opening question papers
            bp = random.choice(bpslst)
            s = list(set(bp))
            L = []
            #print("BLUE PRINT -", bp)
            for unqm in s:
                lst = []
                for i in range(bp.count(unqm)):
                    lst.append(unqm)
                L.append(lst)
            sec = ord('A')
            num = 1
            for unqmlist in L:
                if len(unqmlist)>1:
                    qpap.write(str("Section" + str(chr(sec) + "-" + str(unqmlist[0]) + "markers:" + str(unqmlist[0]) + "M" + "*" + str(len(unqmlist)) + "=" + str(str(len(unqmlist)*unqmlist[0])) + "M" + "\n")))
                else:
                    qpap.write(str("Section" + str(chr(sec) + "-" + str(unqmlist[0]) + "marker\n")))
                for m in unqmlist:
                    while True:
                        q = random.choice(qmdictkeys)
                        qpap.seek(0)
                        if (qmdict[q] == m) and (q not in qpap.read()):
                            qpap.write(str(num)+"." + q + '\n')
                            break
                        else:
                            pass
                    num+=1
                sec+=1
                qpap.write("---------------------\n")
            qpap.close()
            


#End of qbpmarks() - making question papers based on total marks(option 2)

#------------------------

#Start of qbnummarks() - making question paper based on number of questions and marks(option 3)
def qbpnummarks():

    qpapnum = int(input("How many question papers do you want?:"))

    for i in range (1,qpapnum+1):

        print("Paper", i)
        print()
        global m
        m = int(input("How many marks should the question paper be for?:"))
        global qn
        qn = int(input("How many questions should be in the question paper?:"))
        print()

        comberqmbp()

        if comberqmbp():
            global qpap
            qpap = open("/Users/grishichakravarthy/Desktop/questionpapers/qpaper" + str(i) + ".txt", "a+")

            count = 1
            for qblueprint in qbps:
                print(count, qblueprint)
                count += 1
            bpinput = int(input("Enter appropriate blue print for your question paper:"))
            print("A", m, "mark question paper with", qn, "questions in the ",qbps[bpinput-1], "pattern is being generated...")
            #print("A", m, "mark question paper with", qn, "questions in the ",qbps[bpinput-1], "pattern has been generated successfully!")
            print()

            bp = (qbps[bpinput-1])

            s = list(set(bp))
            L = []

            for unqm in s:
                lst = []
                for i in range(bp.count(unqm)):
                    lst.append(unqm)
                L.append(lst)
            sec = ord('A')
            num = 1
            for unqmlist in L:
                if len(unqmlist)>1:
                    qpap.write(str("Section" + str(chr(sec) + "-" + str(unqmlist[0]) + "markers:" + str(unqmlist[0]) + "M" + "*" + str(len(unqmlist)) + "=" + str(str(len(unqmlist)*unqmlist[0])) + "M" + "\n")))
                else:
                    qpap.write(str("Section" + str(chr(sec) + "-" + str(unqmlist[0]) + "marker\n")))

                for mark in unqmlist:
                    while True:
                        q = random.choice(qmdictkeys)
                        qpap.seek(0)
                        if (qmdict[q] == mark) and (q not in qpap.read()):
                            qpap.write(str(num)+"." +q+'\n')
                            break
                        else:
                            pass
                    num+=1
                sec+=1
                qpap.write("---------------------\n")
            print("A", m, "mark question paper with", qn, "questions in the ", qbps[bpinput - 1], "pattern has been generated successfully!")

            qpap.close()

        else:
            print("No valid combinations can be made")
#------------------------
#End of qbnummarks i.e making question paper based on number of questions and marks(option 3)
#------------------------

mainput = int(input("Do you want to make question paper(1) or question bank?(2):"))
if mainput == 1:

    # Question - mark dictionary
    cur.execute("use {}".format(database))
    cur.execute("show tables")
    data = cur.fetchall()
    print("Tables:")
    count = 1
    for table in data:
        print(count, ".", table[0])
        count += 1
    con.commit()
    tinp = int(input("Choose number of table which you want to select"))
    tname = data[tinp - 1][0]

    cur.execute("select * from {}".format(tname))
    questionsdata = cur.fetchall()
    print(tabulate.tabulate(questionsdata))
    # print("Data:", data)
    qmdict = {}
    for item in questionsdata:
        qmdict[item[0]] = item[1]
    # print("qmdict:", qmdict)
    qmdictkeys = list(qmdict.keys())  # List of all questions
    mlist = list(qmdict.values())


    qinp = int(input("Do you want to make question papers based on: \n1.Number of questions \n2.Total marks\n3.Number of questions and marks\n--->Enter choice:"))

    if qinp == 1:
        qbpnum()
    elif qinp == 2:
        qbpmarks()
    elif qinp == 3:
        qbpnummarks()

elif mainput == 2:
    tablesubject = int(input("Do you want to work on an existing table(1) or new table?(2):"))

    if tablesubject == 1:

        cur.execute("use {}".format(database))
        cur.execute("show tables")
        data = cur.fetchall()
        print("Tables:")
        count = 1
        for table in data:
            print(count,".", table[0])
            count+=1
        con.commit()
        tinp = int(input("Choose number of table which you want to select"))
        tname = data[tinp-1][0]
        cur.execute("select * from {}".format(tname))
        qs = cur.fetchall()
        print(tabulate.tabulate(qs))


        changesinp = input("Do you want to make any changes to the table?(Y/N): ")
        if changesinp == 'Y' or changesinp == 'y':
            qbankmaker()
            cur.execute("select * from {}".format(tname))
            qs = cur.fetchall()
            print(type(qs))
            print(tabulate.tabulate(qs))
            print("Question bank has been successfully updated")
        elif changesinp == 'N' or changesinp == 'n':
            print("You have chosen to not make any changes.")

    elif tablesubject == 2:

        tname = input("Enter table name(DO NOT USE SPACES) in which you want to make changes:")
        cur.execute("use {}".format(database))
        cur.execute("Create table {} (question varchar(100), marks int)".format(tname))
        con.commit()
        print("Question bank i.e the table {} has been successfully created".format(tname))
        qbankmaker()
        cur.execute("select * from {}".format(tname))
        qs = cur.fetchall()
        con.commit()
        print(tabulate.tabulate(qs))
        print("Question bank i.e the table {} has been successfully updated".format(tname))

    else:
        print("Enter valid input")

else:
    print("Invalid input, try again with valid input")

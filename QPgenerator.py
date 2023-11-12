import random
import itertools

qbank = open("/Users/grishichakravarthy/Desktop/qbank.txt", "r") #opening questionbank
qs = qbank.readlines() #storing qbank questions in a list
qslen = len(qs) #number of questions in question bank
qinp = int(input("Do you want to make question papers based on: \n1.Number of questions \n2.Total marks\n3.Number of questions and marks\n--->Enter choice:"))

#Question - mark dictionary
qmdict = {}
for q in qs:
    try:
        qm = q.split("{M:")
        qm2 = qm[1].split("}")
        qmark = int(qm2[0])
    except:
        qmark = 0
    qmdict[q.split("{")[0]] = qmark
#print(qmdict)
qmdictkeys = list(qmdict.keys()) #List of all questions
mlist = list(qmdict.values()) #List of all marks

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
        qpap = open("/Users/grishichakravarthy/Desktop/questionpapers/qpaper"+str(count)+".txt", "a+") #making/opening question papers

        s = 0

        for x in range(qnum):
            while s!=len(qmdictkeys):
                q = random.choice(qmdictkeys)
                qpap.seek(0)
                if q not in qpap.read():
                    qpap.write(q+"\n")
                    s+=1
                    break
                else:
                    pass

        qpap.close()
        qbank.close()

#End of qbnum() - making question papers based on number of questions(option 1)

#------------------------

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
            for mark in bp:
                while True:
                    q = random.choice(qmdictkeys)
                    qpap.seek(0)
                    if (qmdict[q] == mark) and (q not in qpap.read()):
                        qpap.write(q + '\n')
                        break
                    else:
                        pass
            qpap.close()
            qbank.close()


#End of qbpmarks() - making question papers based on total marks(option 2)

#------------------------

#Start of qbnummarks() - making question paper based on number of questions and marks(option 3)
def qbpnummarks():

    qpapnum = int(input("How many question papers do you want?:"))

    for i in range (1,qpapnum+1):
        global qpap
        qpap = open("/Users/grishichakravarthy/Desktop/questionpapers/qpaper"+str(i)+".txt", "a+")
        print("Paper", i)
        print()
        global m
        m = int(input("How many marks should the question paper be for?:"))
        global qn
        qn = int(input("How many questions should be in the question paper?:"))
        print()

        comberqmbp()

        if comberqmbp():
            count = 1
            for qblueprint in qbps:
                print(count, qblueprint)
                count += 1
            bpinput = int(input("Enter appropriate blue print for your question paper:"))
            print("A", m, "mark question paper with", qn, "questions in the ",qbps[bpinput-1], "pattern is being generated...")
            print("A", m, "mark question paper with", qn, "questions in the ",qbps[bpinput-1], "pattern has been generated successfully!")
            print()

            for mark in qbps[bpinput-1]:
                while True:
                    q = random.choice(qmdictkeys)
                    qpap.seek(0)
                    if (qmdict[q] == mark) and (q not in qpap.read()):
                        qpap.write(q+'\n')
                        break
                    else:
                        pass
            qbank.close()
            qpap.close()

        else:
            print("No valid combinations can be made")
            qbank.close()
            qpap.close()
#------------------------
#End of qbnummarks i.e making question paper based on number of questions and marks(option 3)

if qinp == 1:
    qbpnum()
elif qinp == 2:
    qbpmarks()
elif qinp == 3:
    qbpnummarks()
else:
    print("Invalid input, try again with valid input")
    

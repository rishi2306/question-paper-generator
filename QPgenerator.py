import random
import itertools

qbank = open("/Users/grishichakravarthy/Desktop/qbank.txt", "r") #opening questionbank
qs = qbank.readlines() #storing qbank questions in a list
qslen = len(qs) #number of questions in question bank
qinp = int(input("Do you want to make question papers based on: \n1.Number of questions \n2.Total marks\n3.Number of questions and marks"))

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
qmdictkeys = list(qmdict.keys())
mlist = list(qmdict.values())

def comberqmbp(): #for making question papers based on marks and question numbers
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

    count = 1
    for qblueprint in qbps:
        print(count,qblueprint)
        count+=1

def qbpnum():
    qpapnum = int(input("How many question papers do you want?:")) #number of questionpapers

    for count in range(1, qpapnum+1):
        print("Paper", count)
        qnum = int(input("How many questions do you want the paper"+str(count)+" to have?: ")) #no. of questions in each paper
        qpap = open("/Users/grishichakravarthy/Desktop/questionpapers/qpaper"+str(count)+".txt", "a+") #making/opening question papers
    
        for i in range(qnum):
            num = random.randint(0,qnum-1) #randomly selecting a question
            if qs[num] not in qpap:
                q = qs[num]
                qpap.write(q)#writing question into question paper
        qpap.close()#closing question paper - will go back to for loop and repeat for other qpapers

    qbank.close()#closes questionbank



#Question paper making based on marks
def qbpnummarks():

    qpapnum = int(input("How many question papers do you want?:"))
    

    #insert invalid combinations, try again - thing   

    

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
        
        bpinput = int(input("Enter appropriate blue print for your question paper:"))
        print("A", m, "mark question paper with", qn, "questions in the ",qbps[bpinput-1], "pattern is being generated...")
        print("A", m, "mark question paper with", qn, "questions in the ",qbps[bpinput-1], "pattern has been generated successfully!")
        print()


        for mark in qbps[bpinput-1]:
            while True:
                global q
                q = random.choice(qmdictkeys)
                if qmdict[q] == mark:
                    if q not in qpap:
                        qpap.write(q+"\n")
                        break
                    else:
                        continue
                else:
                    continue
        qpap.write(" ")
        qpap.write((str(m)+"marks"))

        
        '''for mark in qbps[bpinput-1]:
            while True:
                global q
                q = random.choice(qmdictkeys)
                if qmdict[q] == mark and q not in qpap:
                    qpap.write(q+"\n")
                    break
                else:
                    continue'''

    
        qbank.close()
        qpap.close()

if qinp == 1:
    qbpnum()
if qinp == 3:
    qbpnummarks()

    


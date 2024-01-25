from typing import Any
from selenium import webdriver
from selenium.webdriver.common.by import By
import io

url = ""
name = "John Doe"

gimkit = webdriver.Chrome()

#this section creates a list of questions, each value is [question, answer]
questions = []
qs = open("questions.txt")
text = qs.read()
#print(qs.read())
q = []
buf= io.StringIO(text)
for ln in range(text.count("\n") +1):
    
    line = buf.readline()
    q.append(line.removesuffix('\n'))
    if len(q) == 2:
        questions.append(q)
        q = []

def find_answer(questions: list, question):
    for qa in questions:
        if qa[0].lower() == question.lower():
            #print(qa[0])
            #print(qa[1])
            return qa[1]
#qnum = 11
#print(questions[qnum][0])
#print(find_answer(questions, "An example of Leonardo Da Vinci's engineering ideas"))

#print(find_answer(questions, "In his notebooks, Da Vinci sketched about things having to do with flying, such as:"))
#start gimkit game
gimkit.get(url)
nameBox = gimkit.find_element(By.CLASS_NAME, "sc-iQAVnG")
nameBox.send_keys(name)
join = gimkit.find_element(By.CLASS_NAME, "sc-eYulFz")
join.click()
try:
    start = gimkit.find_element(By.CLASS_NAME, "sc-gLgtkKs")
    start.click()
except:
    print("button not found please manually start gimkit")
input("press enter when ready to answer")
bait = 0
while 1==1:
    try:

        question = gimkit.find_element(By.CLASS_NAME, "sc-qVkRw").text
        print(question)
        answer =find_answer(questions, question)
        if answer != None:
            buttons = gimkit.find_elements(By.CLASS_NAME, "sc-qVkRw")
            for button in buttons:
                if button.text ==answer:
                    button.click()
                    bait +=1
        else:
            continuebtn = gimkit.find_elements(By.CLASS_NAME, "sc-qVkRw")
            
            for btn in continuebtn:
                if btn.text == "Continue":
                    btn.click()
        
    except:
        #print("question not found")
        try:
            #print(gimkit.find_elements(By.CLASS_NAME, "sc-sImlw").text)
            if gimkit.find_element(By.CLASS_NAME, "sc-sImlw").text != "Out of bait!":
                gimkit.find_elements(By.CLASS_NAME, "css-1k9m51z")[0].click()
        except:
            pass
#sc-qVkRw class name for answer buttons

input()
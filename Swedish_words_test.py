import pandas as pd
import sys

def quiz_lst(q_lst):
    score = 0
    for i in range(len(q_lst)):
        w = q_lst[0][i]
        q = input(f"What is {w} in Swedish? ")
        if q == q_lst[1][i].strip(" "):
            score += 1
            print("Correct", f"Score: {score}")
        else:
            retry = input("Do you want to try again?\nIf you do, type y, otherwis type n ")
            while retry == "y" and q != q_lst[1][i].strip(" "):
                q = input(f"What is {w} in Swedish? ")
                if q == q_lst[1][i].strip(" "):
                    score += 1
                    print("Correct", f"Score: {score}")
                else:
                    retry = input("Do you want to try again?\nIf you do, type y, otherwis type n ")
            
    print("Total score:", score)


def start_f(file_path):
    question = input("Are you willing to take a Swedish test?\nIt is about \'Color\'.If yes, type y if not, type n. ")
    print(question)
    content = pd.read_csv(file_path, header = None)
    if question == "y":
        quiz_lst(content)
    else:
        pass           
       
start_f(sys.argv[1])

# Caleb Ngatuvai
# 4 July 2025
# P4HW1
# Collect scores using loops

#create variables and list
num_scores = int(input("How many scores do you want to enter? "))
print()
n = 1
scores_list = []

while n <= num_scores:
    score = float(input(f"Enter score #{n}: "))
    while (score < 0) or (score > 100):
        print("\nINVALID SCORE ENTERED!!!!\nScore should be between 0 and 100\n")
        score = float(input(f"Please enter a valid score for score #{n}: ")) 
    
    
    scores_list.append(score)
    n += 1

print("--------------------Results--------------------")
print(f"\nLowest Score   : {min(scores_list):<10.1f}")
low_score = min(scores_list)

#drop lowest score
scores_list.remove(low_score)

print(f"Modified List  : {scores_list}")

#compute average score
avg = sum(scores_list) / len(scores_list)
print(f"Scores Average : {avg:<10.2f}")

#print letter grade
if avg >= 90:
    print("Grade          : A")
elif avg >= 80:
    print("Grade          : B")
elif avg >= 70:
    print("Grade          : C")
elif avg >= 60:
    print("Grade          : D")
else:
    print("Grade          : F")
print()
print("-----------------------------------------------")

'''
Program calculates the average score using two while loops.
Scores input need to be within the range of 0 to 100.
The lowest score input is dropped.
The remaining scores are averaged.
Results are output.
'''

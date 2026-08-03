groups=[[85,40,72],[30,95,60],[55,20,88]]
i=0
sum=0
passing_scores = []
while i<len(groups):
    print(f"student{i+1}:{groups[i]}")
    for student_num, score in enumerate(groups[i], start=1):
        
        if score >= 50:
            print(f"student {student_num} passed with score {score}")
            passing_scores.append(score)
        else:
            print(f"student {student_num} failed with score {score}")
        if score > 90:
            print(f"student #{student_num} is a TOP PERFORMER!")
        
    i += 1
print("\nSummary of Passing Scores:")
for index, score in enumerate(passing_scores, start=1):
    print(f"{index}. {score}")
    sum+=passing_scores[index-1]
print(f"Average:{sum/len(passing_scores)}")
    
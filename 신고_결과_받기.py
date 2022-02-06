print("학점 계산기")
subject_num = int(input("number of subject : "))

arr = []
for i in range(1, subject_num+1):
    arr.append(int(input(f"adding your {i}_grade : ")))


print("멘티여러분 고생많으셨습니다")
avg = sum(arr)/subject_num
print(f"Average : {avg}")

if avg > 90:
    grade = 'A'
elif avg > 80:
    grade = 'B'
else:
    grade = 'F'

print(f"Your grade : {grade}")
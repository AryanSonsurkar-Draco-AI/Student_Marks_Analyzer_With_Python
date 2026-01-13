
def subjects():
    subject = {}
    while True:
        try:
            a = int(input("How many subjects do you have???\n"))
            if a == 0 :
                print("Enter atleast 1 subject.")
                continue
            else:
                break

        except ValueError:
            print("Please write numbers only!")

    i=1
    while (i<=a):    
        try:
            sub = input("Enter subject name : \n")
            marks = int(input(f"Enter marks of {sub} : "))

            if marks < 0 or marks > 100:
                print("Marks should be between 0 and 100.")
                continue

            subject[sub] = marks
            i = i + 1
                
        except ValueError:
            print("Enter valid marks.")
        
    return subject

def analyze(subject):
    total = sum(subject.values())
    percentage = total/len(subject)

    highest = max(subject,key=subject.get)
    lowest = min(subject, key=subject.get)

    return total, percentage, highest, lowest

def main():
    print("------------------------------------------------")
    print("Welcome to Student Marks Analyzer")
    print("------------------------------------------------")
    
    subject_marks = subjects()
    total, percentage, highest, lowest = analyze(subject_marks)
    
    if percentage >= 74 :
        grade = "First class with distinction"

    elif percentage >= 55 and percentage < 74:
        grade = "First class"

    elif percentage >= 40 and percentage < 55:
        grade = "Second Class"

    else:
        grade = "Fail"

    print("-----Result-----")
    print("Total Marks:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)
    print("Highest Scoring Subject:", highest)
    print("Lowest Scoring Subject:", lowest)

if __name__ == "__main__":
    main()
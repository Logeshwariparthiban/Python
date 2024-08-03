class MultipleFunction():
    def Subfields(items):
        print("Subfields in AI are:")        
        mylist = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech processing", "Natural Language Processing"]
        for item in mylist:
            print(item)
    
    def OddEven():
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is an even number")
        else:
            print(f"{num} is an odd number")

    def Eligible():
        Gender = input("Your Gender: ")
        Age = int(input("Your Age: "))
        if Gender.lower() == "male":
            if Age >= 21:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        elif Gender.lower() == "female":
            if Age >= 18:
                print("ELIGIBLE")
            else:
                print("NOT ELIGIBLE")
        else:
            print("Invalid Gender")

    def percentage():
        sub1 = int(input("subject1 = "))
        sub2 = int(input("subject2 = "))
        sub3 = int(input("subject3 = "))
        sub4 = int(input("subject4 = "))
        sub5 = int(input("subject5 = "))
        Total = sub1 + sub2 + sub3 + sub4 + sub5
        print(Total)
        Percentage = (Total / 500) * 100
        print(Percentage)

    def triangle():
        Height = int(input("Height: "))
        Breadth = int(input("Breadth: "))
        formula1 = "(Height * Breadth) / 2"
        Area = (Height * Breadth) / 2
        print(f"Area formula: {formula1}") 
        print(f"Area of Triangle: {Area}")
        
        Height1 = int(input("Height1: "))
        Height2 = int(input("Height2: "))
        Breadth = int(input("Breadth: "))
        formula2 = "Height1 + Height2 + Breadth"
        Perimeter = Height1 + Height2 + Breadth
        print(f"Perimeter formula: {formula2}")
        print(f"Perimeter of Triangle: {Perimeter}")

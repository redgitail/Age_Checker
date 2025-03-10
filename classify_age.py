def classify_age():
    while True:
        age = input("Enter age to show classification: ")
        
        if 0 <= int(age) <= 12:
            print(age, " year(s) old is considered a Child.")
            choice = input("Would you like to enter another age? (y/n)")
            if choice =="y":
                continue
            else:
                print("Exiting.")
                break
                
        elif 13 <= int(age) <= 19:
            print(age, " years old is considered a Teen.")
            choice = input("Would you like to enter another age? (y/n)")
            if choice =="y":
                continue
            else:
                print("Exiting.")
                break
                
        elif 20 <= int(age) <= 64:
            print(age, " years old is considered an Adult.")
            choice = input("Would you like to enter another age? (y/n)")
            if choice =="y":
                continue
            else:
                print("Exiting.")
                break
                                
        elif int(age) >= 65:
            print(age, " years old is considered a Senior.")
            choice = input("Would you like to enter another age? (y/n)")
            if choice =="y":
                continue
            else:
                print("Exiting.")
                break
                
        else:
            print("Error in input. Please input age >= 0")
            choice = input("Would you like to try again? (y/n)")
            if choice == "y":
                continue
            else:
                print("Exiting.")
                break
            
classify_age()
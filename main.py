with open("Input/Names/invited_names.txt") as name:
        names=name.readlines()  
        
with open("Input/Letters/starting_letter.txt") as letter:
     letter_data=letter.read()     
     for name in names:
        stripped_name=name.strip()
        with open(f"Output/ReadyToSend/letter_for_{stripped_name}.txt","w") as letter:
            complete_letter=letter_data.replace("[name]",stripped_name)
            letter.write(complete_letter) 


# luke kaden eben
'''
print("=== Secure notes app ===")

choice = input("choose add / view: ").strip().lower()
if choice == "add":
    note = input("enter note: ").strip().lower()

    encrypted = " "
    for ch in note:
        encrypted = encrypted + chr(ord(ch)+1)

    file = open("secure_notes.txt", "a")
    file.write(encrypted + "\n")
    file.close()

    print("note saved securly. ")

elif choice == "view":
    file = open("secure_notes.txt", "r")

    count = 0 
    for line in file:
        decrypted = " "
        for ch in line.strip():
            decrypted = decrypted + chr(ord(ch)-1)

        
        print("- " + decrypted)
        count = count + 1
    file.close()
    print("total notes:", count)
else:
    print("invalid option")
'''



while True:
    choice = input("1. add feedback \n2. view feedback \n3. analyze feeback \n4. search feedback \n5. exit \n- ").strip().lower()
    if choice == "1":
        note = input("type feedback text: ").strip().lower()
        feed_text = " "
        for ch in note:
            feed_text = feed_text + chr(ord(ch)+1)
        file = open("secure_feeback.txt ", "a")
        file.write(feed_text + "\n")
        file.close()
        print("successfully saved")
    if choice == "2":
        file = open("secure_feeback.txt ", "r")
        count = 0
        for line in file:
            feed_text= " "
            for ch in line.strip():
                feed_text = feed_text + chr(ord(ch)-1)
            count += 1
            print("- " + feed_text)
    if choice == "3":
        count = 0
        file = open("secure_feeback.txt ", "r")
        lines = file.readlines()
        linecount = len(lines)
        print(f"total number of entries = {linecount}")
        for line in file:
            feed_text= " "
            for ch in line:
                feed_text = feed_text + chr(ord(ch)-1)
            word = len(feed_text)
            print(f"total words is {int(word)}")
    if choice == "4":
        keyword = input("key word: ")
        file = open("secure_feeback.txt ", "r")
        for line in file:
            feed_text= " "
            for ch in line:
                feed_text = feed_text + chr(ord(ch)-1)
        for line in feed_text:
            if keyword in line:
                print(line.strip())
    if choice == "5":
        break 

        





        









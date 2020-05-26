students = ['Petrov', 'Sidorov', 'Rakovych', 'Fredorov', 'Surnamovich']


def main():
    # add your solution here:

    dict = {}
    max_len = -1            #width of table
    #max_grade = -1         #digits of max number
    for student in students:
        print("")
        print("Current student:",student)
        while True:
            value = input("Enter grade: ")
            try:
                data = int(value)
                if data < 0 or data > 100:
                    print("Incorrect input")
                    continue
                dict[student] = data
                break
            except:
                print("Incorrect input")
                continue

    #getting max length of full string
    for item,value in dict.items():
        res = "|" + str(item) + ":" + str(value) + "|"
        #if value > max_grade:
            #max_grade = value
        if len(res)>max_len:
            max_len = len(res)

    #print("")
    #print("length:",max_len)
    print("")
    print("Grades:")
    print((max_len + 2) * "-")      # +2 to finish the lines

    for item,value in dict.items():
        #padding based on length of string
        print("|" + str(item + ":").ljust(max_len - len(str(value))) + str(value) + "|")

    print((max_len + 2) * "-")

if __name__ == '__main__':
    main()


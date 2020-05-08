input_file_names = ["a_example.txt", "b_read_on.txt", "c_incunabula.txt", "d_tough_choices.txt", "e_so_many_books.txt", "f_libraries_of_the_world.txt"]

#for file_selector in range(0, 6):
for file_selector in range(len(input_file_names)):
    #reading input file
    f_in = open(input_file_names[file_selector], "r")

    #extracting general info
    print("============================================================")
    print(str(file_selector) + ".1. Extracting info from file", input_file_names[file_selector])
    first_line = f_in.readline().split() #containts info about Books, Libraries and Days
    B = int(first_line[0])
    L = int(first_line[1])
    D = int(first_line[2])

    #extracting book info
    second_line = f_in.readline().split() #contains Book scores
    books = {}
    for i in range(len(second_line)):
        books[str(i)] = int(second_line[i])

    #extracting library info
    libraries = {}
    lib_id = 0; i = 0; temp = 0
    for line in f_in:
        if len(line.strip()) == 0:
            continue
        splitted_line = line.split()
        #print(splitted_line)
        #print(lib_id, i, temp)
        if (temp == 0):
            libraries[i] = [int(splitted_line[0]), int(splitted_line[1]), int(splitted_line[2])]
            temp += 1
        else:
            temp_books = {}
            for book in splitted_line:
                temp_books[book] = books[book]
            sorted_temp_books = dict(sorted(temp_books.items(), key=lambda kv: kv[1], reverse = True))
            libraries[i].append(sorted_temp_books)
            i += 1
            temp = 0
        lib_id += 1

    #sorting by signup time, then sort by book score (descending)
    print(str(file_selector) + ".2. Sorting libraries by signup time and then by books per day")
    sorted_libraries = dict(sorted(libraries.items(), key = lambda x: (x[1][1], -x[1][2], -x[1][0])))
    #avoiding scanning duplicate books
    print(str(file_selector) + ".3. Avoiding scanning of duplicate books")
    scanned_books = set()
    for i in sorted_libraries.copy().keys():
        for j in sorted_libraries[i][3].copy().keys():
            if j not in scanned_books:
                scanned_books.add(j)
            else:
                del sorted_libraries[i][3][j]
        if not bool(sorted_libraries[i][3]):
            del sorted_libraries[i]

    #output to file
    print(str(file_selector) + ".4. Writing to output file")
    f_out = open(input_file_names[file_selector][0: input_file_names[file_selector].find('.')] + ".out.txt", "w")
    f_out.write(str(len(sorted_libraries)) + "\n")
    for i in sorted_libraries.keys():
        f_out.write(str(i) + " ")
        f_out.write(str(len(sorted_libraries[i][3])) + "\n")
        for j in sorted_libraries[i][3].keys():
            f_out.write(str(j) + " ")
        f_out.write("\n")
    print("============================================================")
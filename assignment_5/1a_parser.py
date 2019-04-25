filename = "BLOSUM62.txt"

def txt_substitionmatrix(filename):
    file = open(filename, "r")
    matrix = dict()
    for line in file:
        if line.startswith("#") or line.startswith("*"):
            pass               # Ignore line with comments and * aminoacid
        elif line.startswith(" "):
            column_names = []  # Initialize list with aminoacids in column name line
            # Replace carriage return and newline as well as * aminoacid
            line = line.replace("\r","").replace("\n","").replace("*", "")
            for character in line:
                if character != " ":
                    column_names.append(character)
        else:   # else line starts with aminoacid
            # positive numbers with leading +, so we can simply split lines by space
            splitted_line = line.replace("  ", " +").split(" ")
            for i in range(0, len(column_names)):
                # key is AA in line, AA in column; value in list at index
                matrix[(splitted_line[0], column_names[i])]= int(splitted_line[i+1])
    file.close()
    return matrix

blossum62 = txt_substitionmatrix(filename)
print(blossum62)


filename = "BLOSUM62.txt"

def txt_to_substition_matrix(filename):
    file = open(filename, "r")
    matrix = dict()
    for line in file:
        if line.startswith("#") or line.startswith("*"):
            pass                                         # Ignore line with comments and the last line starting with *
        elif line.startswith(" "):                       # This is the line containing column names in one letter code
            column_names = []
            line = line.replace("\r","").replace("\n","").replace("*", "")       # Delete carriage return, new line, *
            for character in line:
                if character != " ":
                    column_names.append(character)                            # Add single letter code to column names
        else:                                    # One letter code followed by scores for the each pair of amino acids
            # Every column is 3 character wide, negative scores have one " ", whereas positive scores have two "  ".
            # By replacing "  " with " +" each value has exactly one leading space by which we can split the line into
            # two character strings containing the scores.
            splitted_line = line.replace("  ", " +").split(" ")
            for i in range(0, len(column_names)):
                # Key is a tuple of the one letter code at the beginning of the line and the one letter code in the
                # column name. Note that the column names are indexed from 0, whereas in the splitted line they are
                # indexed from 1, therefore we add 1 to the index of the column names
                matrix[(splitted_line[0], column_names[i])]= int(splitted_line[i + 1])
    file.close()
    return matrix

blossum62 = txt_to_substition_matrix(filename)
print(blossum62)


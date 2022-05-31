"""First Attempt to parse our document"""


def attempt_parse():
    with open("DSM5_Subset.txt") as file:
        myfile = list(file)

    is_start_section = False
    for line in myfile:
        line = line.lstrip()
        if "Diagnostic Criteria" in line:
            is_start_section = True

        elif is_start_section is True:
            # removing the \n
            if str(line).startswith('Note:'):
                continue
            is_start_section = node_one(line, 0)
            if is_start_section is True:
                print(line[:-1])

def node_one(line, index, last_letter=None):
    if not line:
        return False
    if line[index].isupper():
        return node_two(line, index + 1)
    if line[index].isdigit():
        return node_one(line, index + 1, line[index])
    # if lat letter is none, then it won't become a digit (str(None).isdigit() is False)
    if line[index] == '.' and str(last_letter).isdigit():
        return node_two(line, index)
    return True

def node_two(line, index):
    if not line:
        return False
    if line[index] == '.':
        return node_three(line, index + 1)
    return False

def node_three(line, index):
    if not line:
        return False
    if line[index] == ' ':
        return True
    return False

if __name__ == '__main__':
    attempt_parse()
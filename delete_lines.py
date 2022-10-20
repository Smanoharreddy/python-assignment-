def delete_lines(file):
    lines = []
    with open(file, 'r') as f:
        lines = f.readlines()

    with open(file, 'w') as f:
        if len(lines) % 2 == 0:
            for number, line in enumerate(lines):
                if (number + 1) != len(lines) // 2 and (number + 1) != (len(lines) // 2) + 1:
                    f.write(line)
        else:
            for number, line in enumerate(lines):
                if (number + 1) != (len(lines) // 2)+1:
                    f.write(line)
delete_lines("text.txt")
delete_lines("text1.txt")
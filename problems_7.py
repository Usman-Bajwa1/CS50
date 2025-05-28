line_count = 0

with open("problems_3.py", "r") as file:
    for line in file:
        if line[0] in ['','#']:
            pass
        else:
            line_count += 1
####################################print(line_counts, contents.rsplit())
blocks_dict= {
    "list_1": ["R", "N","P", "G"],
    "list_2": ["T", "J", "B", "L", "C", "S", "V", "H"],
    "list_3": ["T", "D", "B", "M", "N", "L"],
    "list_4": ["R", "V", "P", "S", "B"],
    "list_5": ["G", "C", "Q", "S", "W", "M", "V", "H"],
    "list_6": ["W", "Q", "S", "C", "D", "B", "J"],
    "list_7": ["F", "Q", "L"],
    "list_8": ["W", "M", "H", "T", "D", "L", "F", "V"],
    "list_9": ["L", "P", "B", "V", "M", "J", "F"]

}

with open("movements.txt") as file:
    for line in file:
        numbers = line.split('move')[1].strip()
        number_of_blocks = int(numbers.split("from")[0].strip())
        beginning_list = int(line.split("from")[1].split("to")[0])
        ending_list = int(line.split("from")[1].split("to")[1])
        blocks = blocks_dict[f"list_{beginning_list}"][-number_of_blocks:]
        for block in blocks:
            blocks_dict[f"list_{beginning_list}"].pop()
            blocks_dict[f"list_{ending_list}"].append(block)

for list in blocks_dict:
    print(blocks_dict[list][-1])

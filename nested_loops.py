board = [ 

['x', '-', 'x'],  

['o', '-', '-'], 

['-', '-', '-'] 

] 


def nested_loops():
    for row in board:
        for item in row:
            print(item, end = "")
        print()

def main():
    nested_loops()

main()
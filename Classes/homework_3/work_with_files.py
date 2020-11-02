
if __name__ == '__main__':
    with open(file='write_line.txt', mode='w') as f:
        f.writelines("hello\ni`m\nusing\nwritelines\nmethod\n")

    with open('write_line.txt', 'r') as f:
        # result = f.readlines()
        result = iter(f.readlines())
        for line in result:
            print(f"What we have in file --> {line}")

from difflib import SequenceMatcher

with open('demo1.txt') as file_one, open('demo2.txt') as file_two:
    data_file1 = file_one.read()
    data_file2 = file_two.read()
    matches = SequenceMatcher(None, data_file1, data_file2).ratio()
    print(f'The plagiarized content are {matches*100}%')

from pathlib import Path

# Choose wordlist to use
#wordFilePath = "/usr/share/dict/words"
word_file_path = "testWordList.txt"

word_file_contents =  Path(word_file_path).read_text()
word_list = word_file_contents.splitlines()

print(type(word_list))
print(word_list)

def f(ltr):
    for w in word_list:
        print(w + ltr)
    
user_ltr = input("letter to append: ")

f(user_ltr)


# this_is_snake_case

print("hello world")




def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        words = file_contents.split() 
        print(len(words))

        def char_nums(words_input): 
            check_san = 0
            letter_count = {}
            for word in words_input:
                word = word.lower()    
                # print(word)
                for idxlet in range(0, len(word)):
                    letter = word[idxlet] 
                    if letter in letter_count.keys():
                        letter_count[letter] += 1
                    else:
                        letter_count[letter] = 1
                    # print(letter)
                    check_san += 1
                    #if check_san > 50:
                      #  exit
            return letter_count
        letter_dict = char_nums(words)
        print(letter_dict)
        
        # build letter list
        letter_list = []
        for entry in letter_dict:
            letter_list.append({"char": entry, "count": letter_dict[entry]})
    
        print(letter_list)
        
        def sort_on(dict_here):
            return dict_here["count"]
                
        letter_list.sort(reverse = True, key = sort_on)

        print(letter_list)
        print("Beginning count of letters")
        for item in letter_list: 
            if not item["char"].isalpha():
                continue
            print(f"The '{item['char']}' character was found {item['count']} times")
        
        print("done counting letters")


main()  

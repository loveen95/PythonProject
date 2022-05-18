

with open('vocabulary.txt', 'w', encoding="utf-8") as f:
    while True:
        english_word = input("영어 단어를 입력하세요: ")
        if english_word == 'q':
            break
        korean_word = input("한국어 뜻을 입력하세요: ")
        if korean_word == 'q':
            break
            
        f.write("{} : {}\n".format(english_word.strip(), korean_word.strip()))    

with open("vocabulary.txt","r") as f:
    for i in f:
        print(i.strip())


with open('vocabulary.txt', 'r') as f:
    for line in f:
        data = line.strip().split(": ")
        english_word, korean_word = data[0], data[1]
        
        # 유저 입력값 받기
        guess = input("{}: ".format(korean_word))
        
        # 정답 확인하기
        if guess == english_word:
            print("맞았습니다!\n")
        else:
            print("아쉽습니다. 정답은 {}입니다.\n".format(english_word))

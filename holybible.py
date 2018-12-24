
# 이지호 작성 #
# 공동번역 성서의 저작권은 모두 저작권자에게 있습니다. #

import sys
import re
import random

end = "끝났습니다."
error = "오류입니다."


def run():
    short = ['Gen', 'Exo', 'Lev', 'Num', 'Deu', 'Jos', 'Jdg', 'Rth', '1Sa', '2Sa', '1Ki', '2Ki', '1Ch', '2Ch', 'Ezr',
             'Neh', 'Est', 'Job', 'Psa', 'Pro', 'Ecc', 'Sol', 'Isa', 'Jer', 'Eze', 'Dan', 'Amo', 'Oba', 'Jon', 'Mic',
             'Nah', 'Hab', 'Zep', 'Hag', 'Zec', 'Mar', 'Luk', 'Joh', 'Act', 'Rom', '1Co', '2Co', 'Gal', 'Eph', 'Phi',
             'Col', '1Th', '2Th', '1Ti', '2Ti', 'Tit', 'Phm', 'Heb', 'Jam', '1Pe', '2Pe', '1Jo', '2Jo', '3Jo', 'Jod',
             'Rev']
    bookname = ['창세기', '출애굽기', '레위기', '민수기', '신명기', '여호수아', '판관기', '룻기', '사무엘상', '사무엘하',
                '열왕기상', '열왕기하', '역대기상', '역대기하', '에즈라', '느헤미야', '에스델', '욥기', '시편', '잠언',
                '전도서', '아가', '이사야', '에레미야', '애가', '에제키엘', '다니엘', '호에샤', '요엘', '아모스',
                '오바디야', '오냐', '미가', '나훔', '하바꾹', '스바니야', '하깨', '즈가리야', '말라기',
                '마태오의 복음서', '마르코의 복음서', '루가의 복음서', '요한의 복음서', '사도행전', '로마인에게 보낸 편지',
                '고린토인에게 보낸 첫째 편지', '고랜토인에게 보낸 둘째 편지', '갈라디아인에게 보낸 편지', '에페소인에게 보낸 편지',
                '필립비인들에게 보낸 편지', '골로사이인들에게 보낸 편지', '델살로니카인들에게 보낸 첫째 편지',
                '데살로니카인들에게 보낸 둘째 편지', '디모테오에게 보낸 첫째 편지', '디도에게 보낸 편지',
                '필레몬에게 보낸 편지', '히브리인들에게 보낸 편지', '야고보의 편지', '베드로의 첫째 편지',
                '베드로의 둘째 편지', '요한의 첫째 편지', '요한의 둘째 편지', '요한의 세째 편지', '유다의 편지', '요한의 묵시록']
    global selectbookname
    global k
    global line
    global number
    for i in range(len(short)):
        book = bookname[i]
        say = ("[%d] " % (i + 1))
        print(say + book, end=" ")
        if i % 5 == 0:
            print('''
            ''')
        if i == (len(short) - 1) and (i % 5) != 0:
            for p in range((len(short) - 1) % 5):
                print(say + book, end=" ")
    print("선택하실 책 번호를 선택하세요.")
    number = int(input())
    selectbookname = short[int(number - 1)]
    print(selectbookname)
    print('''
    [1] 성경 scrapper
    [2] 장 선택해서 읽기
    [3] 줄 선택해서 읽기
    [4] 성경 리더
    [5] 랜덤 줄 출력(모든 경전)
    무엇을 선택하시겠습니까?''')
    choice = int(input())
    if choice == 1:  # 성경 scrapper
        lines = ''
        anypnl = re.compile("\d:\d")
        while True:
            with open('공동번역.txt', 'r')as a:
                line = a.readline()
            checker = line.find('%s %s' % (selectbookname, anypnl))
            if not checker == -1:
                lines += line
            if line is False:
                break
        with open('result.txt', 'w') as b:
            b.write(lines)

    if choice == 2:  # 장 리더
        page = ''
        print('''몇 장입니까?''')
        k = int(input())
        with open('공동번역.txt', 'r')as a:
            while True:
                line = a.readline()
                checker = line.find('%s %d' % (selectbookname, k))
                closer = line.find('%s %d' % (selectbookname, k+1))
                if checker != -1:
                    page += '%s\n' % line
                if closer != -1:
                    break
                if not line:
                    break
        print("\n" * 5)
        print(page)
    if choice == 3:  # 줄 리더
        print('''몇 장 입니까?''')
        page = input()
        print('''몇 줄 입니까?''')
        line = input()
        with open('공동번역.txt', 'r') as a:
            while True:
                linesearcher = a.readline()
                linechecker = linesearcher.find("%s %s:%s" % (selectbookname, page, line))
                if linechecker != -1:
                    break
                if linesearcher == False:
                    break
        print(linesearcher)
    if choice == 4: # 성경 리더
        page = ''
        print('''몇 장부터 보시겠습니까?''')
        k = int(input())
        with open('공동번역.txt', 'r')as a:
            while True:
                line = a.readline()
                checker = line.find('%s %d' % (selectbookname, k))
                closer = line.find('%s %d' % (selectbookname, k+1))
                if checker != -1:
                    page += '%s\n' % line
                if closer != -1:
                    print(page)
                    print('''다음 장을 보려면 엔터를 눌러주세요.
                    다른 값을 입력하시면 종료됩니다.''')
                    k += 1
                    select = input()
                    if select == '':
                        continue
                    else:
                        break
    if choice == 5: # 랜덤 줄
        with open('공동번역.txt', 'r') as a:
            alllines = a.readlines()
            print(random.choice(alllines))

    if choice not in [1, 2, 3, 4, 5]:
        print(error)
        sys.exit()

run()

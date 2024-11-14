def pon():
    your = int(input('グー : 1\nチョキ : 2\n パー : 3\nあなたの手 >> '))
    if your > 3 or your < 1:
        while your > 3 or your < 1:
            print('半角数字1,2,3で入力してください。')
            your = int(input(' \nグー : 1\nチョキ : 2\n パー : 3\nあなたの手 >> '))
    else:
        pass
    if your == 1:
        return 'グー'
    elif your == 2:
        return 'チョキ'
    elif your == 3:
        return 'パー'
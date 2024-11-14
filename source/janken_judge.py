def judge(you, enemy):
    prin = 'null'
    if you == 'グー' :
        if enemy == 'チョキ':
            prin = '勝ち'
        elif enemy == 'パー':
            prin = '負け'
            
    elif you == 'チョキ' :
        if enemy == 'パー':
            prin = '勝ち'
        elif enemy == 'グー':
            prin = '負け'
            
    elif you == 'パー' :
        if enemy == 'グー':
            prin = '勝ち'
        elif enemy == 'チョキ':
            prin = '負け'
    
    return prin
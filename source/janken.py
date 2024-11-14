import computer as cp
import janken_judge as jd
import player as pl


def janken_main():
    cnt = 0
    for i in range(3):
        n = 0
        print(f'-----ラウンド{i+1}-----')
        
        while n < 1:
            pl_hand = pl.pon()
            cp_hand = cp.pon()
            if pl_hand == cp_hand:
                print('------あいこ------')
            else:
                n = 1
        
        WL = jd.judge(pl_hand,cp_hand)
        if WL == '勝ち':
            cnt += 1
        else:
            pass
        
        print(f'あなたの手 : {pl_hand}\nあいての手 : {cp_hand} \n<><><><><><><>\n あなたの{WL}\n<><><><><><><>')
        
    print(f'【最終結果】\nあなた : {cnt}勝\nあいて : {3-cnt}勝')
    if cnt < 2:
        print('あなたは敗北しました...')
    else:
        print('あなたの総合勝利です！！！！！！！！！！！！！！')
        
    
if __name__ == '__main__':
    janken_main()
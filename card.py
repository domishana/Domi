import player
import commonuse
from commonuse import attack_effect

class Card(): #カード
    def __init__(self, ename, jname, cost, clas, ctype, setname):
        self.ename = ename #カードの名称(英語)
        self.jname = jname #カードの名称(日本語)
        self.cost = cost #コスト
        self.clas = clas #カードの分類(基本カードとか王国カードとか)
        self.ctype = ctype #カードの種類
        self.setname = setname #拡張セット

    def played(self, user): #カードがプレイされた時の挙動
        pass

    def gained(self, user): #カードが獲得された時の挙動
        pass

    def trashed(self, user):  #カードが廃棄された時の挙動
        pass

    def reacted(self, user):
        pass
    
    def attack_reactable(self):
        return False
     
    def is_type(self, ctype):
        typec = commonuse.CardType.get_cardtype(ctype)
        return hasattr(self, typec)

    def is_action(self):
        return self.is_type('action')

    def is_treasure(self):
        return self.is_type('treasure')

    def is_victory(self):
        return self.is_type('victory')

    def is_curse(self):
        return self.is_type('curse')

    def is_reaction(self):
        return self.is_type('reaction')

    def is_attack(self):
        return self.is_type('attack')

    def is_victory_or_curse(self):
        return self.is_victory() or self.is_curse()

class TreasureCard(Card): #財宝カード
    def __init__(self, ename, jname, cost, clas, ctype, setname, value):
        super().__init__(ename, jname, cost, clas, ctype, setname)
        self.coins = value
        self.istreasure = 1 #財宝カードなら1

    def played(self, user): #財宝カードがプレイされると使用者の残り金数が増える
        user.pluscoins(self.coins)

class VictoryCard(Card): #勝利点カード
    def __init__(self, ename, jname, cost, clas, ctype, setname):
        super().__init__(ename, jname, cost, clas, ctype, setname)
        self.isvictory = 1 #勝利点カードなら1

    def vicpts(self, user):
        pass

class CurseCard(Card): #呪いカード
    def __init__(self, ename, jname, cost, clas, ctype, setname):
        super().__init__(ename, jname, cost, clas, ctype, setname)
        self.iscurse = 1 #呪いカードなら1

    def vicpts(self, user):
        pass

class ActionCard(Card): #アクションカード
    def __init__(self, ename, jname, cost, clas, ctype, setname):
        super().__init__(ename, jname, cost, clas, ctype, setname)
        self.isaction = 1 #アクションカードなら1

class ReactionCard(Card): #リアクションカード
    def __init__(self, ename, jname, cost, clas, ctype, setname):
        super().__init__(ename, jname, cost, clas, ctype, setname)
        self.isreaction = 1 #リアクションカードなら1

class AttackCard(Card): #アタックカード
    def __init__(self, ename, jname, cost, clas, ctype, setname):
        super().__init__(ename, jname, cost, clas, ctype, setname)
        self.isattack = 1 #アタックカードなら1

class Copper(TreasureCard): #銅貨
    def __init__(self):
        super().__init__("Copper", "銅貨", 0, "基本", "財宝", "基本", 1)

class Silver(TreasureCard): #銀貨
    def __init__(self):
        super().__init__("Silver", "銀貨", 3, "基本", "財宝", "基本", 2)

class Gold(TreasureCard): #金貨
    def __init__(self):
        super().__init__("Gold", "金貨", 6, "基本", "財宝", "基本", 3)

class Estate(VictoryCard): #屋敷
    def __init__(self):
        super().__init__("Estate", "屋敷", 2, "基本", "勝利点", "基本")

    def vicpts(self, user):
        return 1

class Duchy(VictoryCard): #公領
    def __init__(self):
        super().__init__("Duchy", "公領", 5, "基本", "勝利点", "基本")

    def vicpts(self, user):
        return 3

class Province(VictoryCard): #属州
    def __init__(self):
        super().__init__("Province", "属州", 8, "基本", "勝利点", "基本")

    def vicpts(self, user):
        return 6

class Curse(CurseCard): #呪い
    def __init__(self):
        super().__init__("Curse", "呪い", 0, "基本", "呪い", "基本")

    def vicpts(self, user):
        return -1

class Garden(VictoryCard): #庭園
    def __init__(self):
        super().__init__("Garden", "庭園", 4, "王国", "勝利点", "基本")

    def vicpts(self, deck):
        return deck.deck_count()//10

class Smithy(ActionCard): #鍛冶屋
    def __init__(self):
        super().__init__("Smithy", "鍛冶屋", 4, "王国", "アクション", "基本")

    def played(self, user):
        user.draw(3)

class Village(ActionCard): #村
    def __init__(self):
        super().__init__("Village", "村", 3, "王国", "アクション", "基本")

    def played(self, user):
        user.draw(1)
        user.plusactions(2)

class Woodcutter(ActionCard): #木こり
    def __init__(self):
        super().__init__("WoodCutter", "木こり", 3, "王国", "アクション", "基本")

    def played(self, user):
        user.plusbuys(1)
        user.pluscoins(2)

class Market(ActionCard): #市場
    def __init__(self):
        super().__init__("Market", "市場", 5, "王国", "アクション", "基本")

    def played(self, user):
        user.draw(1)
        user.plusactions(1)
        user.plusbuys(1)
        user.pluscoins(1)

class Laboratory(ActionCard): #研究所
    def __init__(self):
        super().__init__("Laboratory", "研究所", 5, "王国", "アクション", "基本")

    def played(self, user):
        user.draw(2)
        user.plusactions(1)

class Festival(ActionCard): #祝祭
    def __init__(self):
        super().__init__("Festival", "祝祭", 5, "王国", "アクション", "基本")

    def played(self, user):
        user.plusactions(2)
        user.plusbuys(1)
        user.pluscoins(2)

class CouncilRoom(ActionCard): #議事堂
    def __init__(self):
        super().__init__("Council Room", "議事堂", 5, "王国", "アクション", "基本")

    def played(self, user):
        user.draw(4)
        user.plusbuys(1)
        [x.draw(1) for x in user.other_players]


class Chancellor(ActionCard): #宰相
    def __init__(self):
        super().__init__("Chancellor", "宰相", 3, "王国", "アクション", "基本")

    def played(self, user):
        user.pluscoins(2)
        self.can_discard_all_deck(user)
    
    def can_discard_all_deck(self, user):
        print("山札をすべて捨て札にしますか")
        answer = user.answer_yn()
        if answer == 'y':
            user.deck.all_move_to(user.dispile)
            return
        if answer == 'n':
            return

class Feast(ActionCard): #祝宴
    def __init__(self):
        super().__init__("Feast", "祝宴", 4, "王国", "アクション", "基本")

    def played(self, user):
        self.trash_from_playarea(user)#これはどう考えても気持ち悪い。userのメソッドであるべき
        user.what_gain_undercost(5)
    
    def trash_from_playarea(self, user):
        user.playarea_pop(self)
        user.trashcard(self)


class Workshop(ActionCard): #工房
    def __init__(self):
        super().__init__("Workshop", "工房", 3, "王国", "アクション", "基本")

    def played(self, user):
        user.what_gain_undercost(4)


class Adventurer(ActionCard): #冒険者
    def __init__(self):
        super().__init__("Adventurer", "冒険者", 6, "王国", "アクション", "基本")

    def played(self, user):
        cards_list = self.revealed_until_open_two_treasure(user)
        tmp_treasure = cards_list[0]
        tmp_not_treasure = cards_list[1]

        user.add_hand(tmp_treasure)
        user.add_dispile(tmp_not_treasure)
    
    def revealed_until_open_two_treasure(self, user):
        tmp_treasure = commonuse.CardsHolder()
        tmp_not_treasure = commonuse.CardsHolder()
        
        while tmp_treasure.counting() < 2:
            if user.is_deck_empty() and user.is_dispile_empty():
                break
            tmp = user.reveal_from_deck(1)
            tmp = tmp[0]
            if tmp.is_treasure():
                tmp_treasure.add_cards(tmp)
            else:
                tmp_not_treasure.add_cards(tmp)
        return [tmp_treasure, tmp_not_treasure]


class Cellar(ActionCard): #地下貯蔵庫
    def __init__(self):
        super().__init__("Cellar", "地下貯蔵庫", 2, "王国", "アクション", "基本")

    def played(self, user):
        user.plusactions(1)
        choices = self.choice_discard(user)
        number = choices.counting()
        user.add_dispile(choices)
        user.draw(number)
    
    def choice_discard(self, user):
        choices = commonuse.CardsHolder()
        while True:
            print("捨て札にするカードを選んでください")
            discarded = user.pop_from_hand()
            if discarded == -1:
                break
            choices.add_cards(discarded)
        return choices
        
    

class Chapel(ActionCard): #礼拝堂
    def __init__(self):
        super().__init__("Chapel", "礼拝堂", 2, "王国", "アクション", "基本")

    def played(self, user):
        choices = self.choice_trashed_under_4(user)
        user.trashcard(choices)
    
    def choice_trashed_under_4(self,user):
        choices = commonuse.CardsHolder()
        for i in range(4):
            print("廃棄するカードを選んでください")
            trashed = user.pop_from_hand()
            if trashed == -1:
                break
            choices.add_cards(trashed)
        return choices


class Library(ActionCard): #書庫
    def __init__(self):
        super().__init__("Library", "書庫", 5, "王国", "アクション", "基本")

    def played(self, user):
        tmp_action = commonuse.CardsHolder()
        while True:
            if user.is_deck_empty() and user.is_dispile_empty():
                break
            if user.hand_count() >= 7:
                break
            tmp = user.reveal_from_deck(1)
            tmp = tmp[0]
            if tmp.is_action():
                self.is_action_add_hand(user, tmp, tmp_action)
            else:
                user.add_hand(tmp)
        user.add_dispile(tmp_action)

    def is_action_add_hand(self, user, tmp, tmp_action):
        print(tmp.jname)
        print("このカードを手札に加えますか")
        answer = user.answer_yn()
        if answer == 'y':
            user.add_hand(tmp)
        else:
            tmp_action.add_cards(tmp)
        return tmp_action


class Mine(ActionCard): #鉱山
    def __init__(self):
        super().__init__("Mine", "鉱山", 5, "王国", "アクション", "基本")

    def played(self, user):
        if not user.handcheck('treasure'):
            print("廃棄するカードがありません")
            return
        while True:
            print("廃棄する財宝カードを選んでください")
            trashed = user.choose_from_hand()
            if trashed == -1:
                continue
            if trashed.is_treasure():
                break
        number = user.cards.hand.index(trashed)
        user.hand_pop(number)
        user.trashcard(trashed)
        user.what_gain_undercost_treasure(trashed.cost + 3)
        #手札に加える処理ができない　後で書く　カードを獲得する動作を、獲得するカードを選ぶ段階と、獲得されるべき場所に放り込むメソッドに分けて実装する必要がありそう

class Remodel(ActionCard): #改築
    def __init__(self):
        super().__init__("Remodel", "改築", 4, "王国", "アクション", "基本")

    def played(self, user):
        if user.is_hand_empty():
            print("廃棄するカードがありません")
            return
        trashed = self.choice_trashed(user)
        user.trashcard(trashed)
        user.what_gain_undercost(trashed.cost + 2)
    
    def choice_trashed(self, user):
        while True:
            print("廃棄するカードを選んでください")
            trashed = user.pop_from_hand()
            if trashed == -1:
                continue
            break
        return trashed

class MoneyLender(ActionCard): #金貸し
    def __init__(self):
        super().__init__("MoneyLender", "金貸し", 4, "王国", "アクション", "基本")

    def played(self, user):
        if not user.is_card_in_hand('Copper'):
            print("廃棄するカードがありません")
            return
        trashed = self.pop_copper_from_hand(user)
        user.trashcard(trashed)
        user.pluscoins(3)
    
    def pop_copper_from_hand(self, user):
        number = user.search_card_in_hand('Copper')
        trashed = user.hand_pop(number)
        return trashed

class Moat(ActionCard, ReactionCard): #堀
    def __init__(self):
        super().__init__("Moat", "堀", 2, "王国", "アクション-リアクション", "基本")

    def played(self, user):
        user.draw(2)

    def reacted(self, user):
        user.protect_from_attack()
        print("堀を使用しました")
        
    def attack_reactable(self):
        return True

class Witch(ActionCard, AttackCard):
    def __init__(self):
        super().__init__("Witch", "魔女", 5, "王国", "アクション-アタック", "基本")
    
    @commonuse.attack_effect
    def played(self, user):
        user.draw(2)
        [x.gaincard(1) for x in user.other_players if not x.is_protected()]
        

class Spy(ActionCard, AttackCard):
    def __init__(self):
        super().__init__("Spy", "密偵", 4, "王国", "アクション-アタック", "基本")

    @commonuse.attack_effect
    def played(self, user):
        user.draw(1)
        user.plusactions(1)
        self.spy_decktop(user)
       
    def spy_decktop(self, user):
         for person in ([user] + user.other_players):
            if person.is_protected():
                continue
            revealed = person.reveal_from_deck(1)[0]
            self.is_discard_or_puton_deck(user, person, revealed)#引数多い。うまくない分け方な気がする。
    
    def is_discard_or_puton_deck(self, user, subject, cards):
        print(cards.jname)
        print("このカードを捨てますか/戻しますか(y/n)")
        answer = user.answer_yn()
        if answer == 'y':
            subject.add_dispile(cards)
        else:
            subject.add_deck(cards)
                
class Thief(ActionCard, AttackCard):
    def __init__(self):
        super().__init__("Thief", "泥棒", 4, "王国", "アクション-アタック", "基本")

    @commonuse.attack_effect
    def played(self, user):
        revealed = commonuse.CardsHolder()
        trasheds = commonuse.CardsHolder()
        
        self.players_reveal_two_cards(user, revealed, trasheds)
        self.what_treasures_gain(user, trasheds)
        user.trashcard(trasheds)
    
    def players_reveal_two_cards(self, user, revealed, trasheds):#何やっているのかひと目見て全くわからないメソッド。もうちょっと分割する。
        for one in user.other_players:
            if one.is_protected():
                continue
            
            revealed.add_cards(one.reveal_from_deck(2))
            revealed.print_cardlist()
            if not revealed.is_type_exist('treasure'):
                print("廃棄するカードがありません")
                one.add_dispile(revealed)
                continue
            while True:
                print("廃棄する財宝カードを選んでください")
                answer = int(input())
                trashed = revealed.pickup(answer)
                if trashed.is_treasure():
                    break
            trasheds.add_cards(trashed)
            revealed.remove(trashed)
            print(revealed.list)
            one.add_dispile(revealed)
            revealed.clear()
        
    def what_treasures_gain(self, user, treasures):
        while True:
            print("獲得する財宝カードを選んでください")
            treasures.print_cardlist()
            answer = int(input())
            if answer == -1:
                break
            gained = treasures.pop(answer)
            user.add_dispile(gained) #獲得時効果があるカードの獲得時効果が発動しない　やはりgaincardの挙動を見直す必要あり
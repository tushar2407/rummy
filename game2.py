import pygame 
import os
import time
import random
from itertools import combinations
pygame.init()
win_dec_unnested=[]
p1_win_dec_unnested=[]
#begin_voice=pygame.mixer.music.load('indian-rummy.mp3')
bg_music=pygame.mixer.music.load('PokerFace.mp3')
stock_pile=[]
discarded_pile=[]
display_width=1150
display_height=750
black=(0,0,0)
green=(50,205,50)
white=(255,255,255,60)
gameDisplay=pygame.display.set_mode((display_width,display_height),pygame.RESIZABLE)
pygame.display.set_caption('Rummy')
clock=pygame.time.Clock()

def loading(pos, size, progress):

    pygame.draw.rect(gameDisplay, (255,255,255), (*pos, *size), 1)
    innerPos  = (pos[0]+3, pos[1]+3)
    innerSize = ((size[0]-6) * progress, size[1]-6)
    pygame.draw.rect(gameDisplay, (255,255,255), (*innerPos, *innerSize))
    
def select(x,y,flag):
    x1,y1=pygame.mouse.get_pos()
    #print(x1,y1)
    if flag==1:
        pygame.draw.circle(gameDisplay,white,(x,y),10)

    elif x1>x and x1<x+70 and y1>y and y1<y+120:
        pygame.draw.circle(gameDisplay,(0,0,0),(x,y),10)
        if pygame.mouse.get_pressed()[0] and flag==0:
            pygame.draw.circle(gameDisplay,white,(x,y),10)
            flag=1
def select1(a):
    x,y=a[1][0],a[1][1]
    x1,y1=pygame.mouse.get_pos()
    if a[2]==1:
        pygame.draw.circle(gameDisplay,white,(x,y),10)
        #return 1
    elif x1>x and x1<x+70 and y1>y and y1<y+120:
        pygame.draw.circle(gameDisplay,(0,0,0),(x,y),10)
        if pygame.mouse.get_pressed()[0] and a[2]==0:
            pygame.draw.circle(gameDisplay,white,(x,y),10)
            a[2]=1
        #return 1
    #return 0
win_dec=[]
win_dec_1=[]
sets_list={}
win_list_type=[['A',1,2,3],[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7],[5,6,7,8],[6,7,8,9],
    [7,8,9,10],[8,9,10,'J'],[9,10,'J','Q'],[10,'J','K','Q'],['J','K','Q','A'],['K','Q','A',1],[1,2,'A','K']]
def comp_logic(cards):
    global win_dec
    win_dec=[]
    q={'A':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'10':[],'J':[],'K':[],'Q':[]}
    q_flag={'A':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'J':0,'K':0,'Q':0}
    #win_dec=[]
    for i in cards:
        if i[::-1][0]=='#':
            q[i[:len(i)-2]].append(i)
            q_flag[i[:len(i)-2]]+=1
            if q_flag[i[:len(i)-2]]>=3:
                win_dec.append(q[i[0]])
        else:
            q[i[:len(i)-1]].append(i)
            q_flag[i[:len(i)-1]]+=1
            if q_flag[i[:len(i)-1]]>=3:
                win_dec.append(q[i[0]])
    '''for i in q_flag:
        f=list(map(lambda j: j.strip('#')[:-1], cards.keys()))
        if i in f:
            pass
    '''
    srcc=q['A']
    for i,j in q_flag.items():
        if j>0:
            srcc=q[i][0]
            break 
    for i in q_flag.keys():
        if len(srcc.strip('#')[:-1])>=2:
            if q_flag[i]<q_flag[srcc.strip('#')[:-1]] and q_flag[i]>0 :
                srcc=i
    for i in win_dec:
        #for j in range(len(i)):
        x=list(map(lambda j: j.strip('#')[::-1][0],i))
        k=x.count('S')
        l=x.count('H')
        m=x.count('C')
        n=x.count('D')
        if k>=1 or l>=1 or m>=1 or n>=1:
            print('aaaa',i)
            #win_dec.remove(i)
            continue
            
    req_list=[]
    for i in win_dec:
        for j in i:
            #del comp_cards_images[j]
            req_list.append(j)
    w={'S':[],'H':[],'D':[],'C':[]}
    w_flag={'S':0,'H':0,'D':0,'C':0}
    #win_dec=[]
    s=0
    h=0
    d=0
    c=0
    if len(w['S'])>4:
        s=combinations(w['S'],4)
    if len(w['H'])>4:
        h=combinations(w['H'],4)
    if len(w['C'])>4:
        c=combinations(w['C'],4)
    if len(w['D'])>4:
        d=combinations(w['D'],4)
    if s:
        for i in s:
            if i in win_list_type:
                win_dec.append(i)
    if h:
        for i in h:
            if i in win_list_type:
                win_dec.append(i)
    if c:
        for i in c:
            if i in win_list_type:
                win_dec.append(i)
    if d:
        for i in d:
            if i in win_list_type:
                win_dec.append(i)
    for i in cards:
        if i not in req_list:
            if i[::-1][0]=='#' :
                #i=i[::-1]
                w[i[::-1][1]].append(i)
                w_flag[i[::-1][1]]+=1
                if w_flag[i[::-1][1]]==4 or len(w[i[::-1][1]])==4:
                    win_dec.append(w[i[::-1][1]])
            else:
                w[i[::-1][0]].append(i)
                w_flag[i[::-1][0]]+=1
                if w_flag[i[::-1][0]]==4 or len(w[i[::-1][0]])==4:
                    win_dec.append(w[i[::-1][0]])
    #dic={'A':1,'Q':10,'K':10,'J':10}
    c=[]
    if len(win_dec)>=1:
        #print('winnn')
        for i in win_dec:
            i.sort(key= lambda j: j.strip('#')[:-1])
            #c.append(list(map(lambda x:x.strip('#')[:-1],i)))
            #c.append(b)
            if '10' in list(map(lambda x:x[:2],i)) and 'K' not in list(map(lambda x:x[:1],i)) and 'J' not in list(map(lambda x:x[:1],i)) and 'Q' not in list(map(lambda x:x[:1],i)):
                x=list(map(lambda x:x[:2],i)).index('10')
                for j in range(len(i)):
                    if j>=x and j<len(i)-1:
                        i[j],i[j+1]=i[j+1],i[j]
            elif '10' in list(map(lambda x:x[:2],i)) and 'J' in list(map(lambda x:x[:1],i)):
                x=list(map(lambda x:x[:2],i)).index('10')
                y=list(map(lambda x:x[:1],i)).index('J')
                for j in range(len(i)):
                    if j>=x and j<y-1:
                        i[j],i[j+1]=i[j+1],i[j]
            elif '10' in list(map(lambda x:x[:2],i)) and 'J' not in list(map(lambda x:x[:1],i)) and 'K' in list(map(lambda x:x[:1],i)) :
                x=list(map(lambda x:x[:2],i)).index('10')
                y=list(map(lambda x:x[:1],i)).index('K')
                for j in range(len(i)):
                    if j>=x and j<y-1:
                        i[j],i[j+1]=i[j+1],i[j]
            elif '10' in list(map(lambda x:x[:2],i)) and 'J' not in list(map(lambda x:x[:1],i)) and 'K' not in list(map(lambda x:x[:1],i)) and 'Q' in list(map(lambda x:x[:1],i)):
                x=list(map(lambda x:x[:2],i)).index('10')
                y=list(map(lambda x:x[:1],i)).index('Q')
                for j in range(len(i)):
                    if j>=x and j<y-1:
                        i[j],i[j+1]=i[j+1],i[j]
            if 'A' in list(map(lambda x:x[:1],i)) and 'Q' not in list(map(lambda x:x[:1],i)):
                x=list(map(lambda x:x[:1],i)).index('A')
                for j in range(x,0,-1):
                    i[j],i[j-1]=i[j-1],i[j]
            elif 'A' in list(map(lambda x:x[:1],i)) and 'Q' in list(map(lambda x:x[:1],i)):
                x=list(map(lambda x:x[:1],i)).index('A')
                #y=list(map(lambda x:x[:1],i)).index('Q')
                for j in range(x,len(i)):
                    if j<len(i)-1:
                        i[j],i[j+1]=i[j+1],i[j]
        for i in win_dec:
            c.append(i)
        print(c,'c')
        for i in win_dec:
            if win_dec.count(i)>1:
                win_dec.remove(i)
        print(win_dec,'win_dec') 
        win_ctr=0
        if len(win_dec)>=2:
            for i in win_dec:
                if i in win_list_type:
                    win_ctr+=1
                    win_dec_1.append(i)
            if win_ctr>=2:
                pass #Declare turn 
    #win_list_type=[['A',1,2,3],[1,2,3,4],[2,3,4,5],[3,4,5,6],[4,5,6,7],[5,6,7,8],[6,7,8,9],
    #[7,8,9,10],[8,9,10,'J'],[9,10,'J','Q'],[10,'J','Q','K'],['J','Q','K','A'],['Q','K','A',1],['K','A',1,2]]
p1_win_dec=[]
p1_win_dec_1=[]
p1_sets_list={}
def p1_logic(cards):
    global p1_win_dec
    p1_win_dec=[]
    q={'A':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'10':[],'J':[],'K':[],'Q':[]}
    q_flag={'A':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'J':0,'K':0,'Q':0}
    #win_dec=[]
    for i in cards:
        if i[::-1][0]=='#':
            q[i[:len(i)-2]].append(i)
            q_flag[i[:len(i)-2]]+=1
            if q_flag[i[:len(i)-2]]>=3:
                p1_win_dec.append(q[i[0]])
        else:
            q[i[:len(i)-1]].append(i)
            q_flag[i[:len(i)-1]]+=1
            if q_flag[i[:len(i)-1]]>=3:
                p1_win_dec.append(q[i[0]])
    #for i in q_flag:
    #    f=list(map(lambda j: j.strip('#')[:-1], cards.keys()))
    #    if i in f:
    #        pass
    
    srcc=q['A']
    for i,j in q_flag.items():
        if j>0:
            srcc=q[i][0]
            break 
    for i in q_flag.keys():
        if len(srcc.strip('#')[:-1])>=2:
            if q_flag[i]<q_flag[srcc.strip('#')[:-1]] and q_flag[i]>0 :
                srcc=i
    for i in p1_win_dec:
        #for j in range(len(i)):
        x=list(map(lambda j: j.strip('#')[::-1][0],i))
        k=x.count('S')
        l=x.count('H')
        m=x.count('C')
        n=x.count('D')
        if k>=1 or l>=1 or m>=1 or n>=1:
            print('aaaa',i)
            #p1_win_dec.remove(i)
            continue
            
    p1_req_list=[]
    for i in p1_win_dec:
        for j in i:
            #del comp_cards_images[j]
            p1_req_list.append(j)
    w={'S':[],'H':[],'D':[],'C':[]}
    w_flag={'S':0,'H':0,'D':0,'C':0}
    #win_dec=[]
    s=0
    h=0
    d=0
    c=0
    if len(w['S'])>4:
        s=combinations(w['S'],4)
    if len(w['H'])>4:
        h=combinations(w['H'],4)
    if len(w['C'])>4:
        c=combinations(w['C'],4)
    if len(w['D'])>4:
        d=combinations(w['D'],4)
    if s:
        for i in s:
            if i in win_list_type:
                p1_win_dec.append(i)
    if h:
        for i in h:
            if i in win_list_type:
                p1_win_dec.append(i)
    if c:
        for i in c:
            if i in win_list_type:
                p1_win_dec.append(i)
    if d:
        for i in d:
            if i in win_list_type:
                p1_win_dec.append(i)
    for i in cards:
        if i not in p1_req_list:
            if i[::-1][0]=='#' :
                #i=i[::-1]
                w[i[::-1][1]].append(i)
                w_flag[i[::-1][1]]+=1
                if w_flag[i[::-1][1]]==4 or len(w[i[::-1][1]])==4:
                    p1_win_dec.append(w[i[::-1][1]])
            else:
                w[i[::-1][0]].append(i)
                w_flag[i[::-1][0]]+=1
                if w_flag[i[::-1][0]]==4 or len(w[i[::-1][0]])==4:
                    p1_win_dec.append(w[i[::-1][0]])
    #dic={'A':1,'Q':10,'K':10,'J':10}
    print(p1_win_dec,'p1_win_dec')
    c=[]
    if len(p1_win_dec)>=1:
        #print('winnn')
        for i in p1_win_dec:
            i.sort(key= lambda j: j.strip('#')[:-1])
            #c.append(list(map(lambda x:x.strip('#')[:-1],i)))
            #c.append(b)
            if '10' in list(map(lambda x:x[:2],i)) and 'K' not in list(map(lambda x:x[:1],i)) and 'J' not in list(map(lambda x:x[:1],i)) and 'Q' not in list(map(lambda x:x[:1],i)):
                x=list(map(lambda x:x[:2],i)).index('10')
                for j in range(len(i)):
                    if j>=x and j<len(i)-1:
                        i[j],i[j+1]=i[j+1],i[j]
            elif '10' in list(map(lambda x:x[:2],i)) and 'J' in list(map(lambda x:x[:1],i)):
                x=list(map(lambda x:x[:2],i)).index('10')
                y=list(map(lambda x:x[:1],i)).index('J')
                for j in range(len(i)):
                    if j>=x and j<y-1:
                        i[j],i[j+1]=i[j+1],i[j]
            elif '10' in list(map(lambda x:x[:2],i)) and 'J' not in list(map(lambda x:x[:1],i)) and 'K' in list(map(lambda x:x[:1],i)) :
                x=list(map(lambda x:x[:2],i)).index('10')
                y=list(map(lambda x:x[:1],i)).index('K')
                for j in range(len(i)):
                    if j>=x and j<y-1:
                        i[j],i[j+1]=i[j+1],i[j]
            elif '10' in list(map(lambda x:x[:2],i)) and 'J' not in list(map(lambda x:x[:1],i)) and 'K' not in list(map(lambda x:x[:1],i)) and 'Q' in list(map(lambda x:x[:1],i)):
                x=list(map(lambda x:x[:2],i)).index('10')
                y=list(map(lambda x:x[:1],i)).index('Q')
                for j in range(len(i)):
                    if j>=x and j<y-1:
                        i[j],i[j+1]=i[j+1],i[j]
            if 'A' in list(map(lambda x:x[:1],i)) and 'Q' not in list(map(lambda x:x[:1],i)):
                x=list(map(lambda x:x[:1],i)).index('A')
                for j in range(x,0,-1):
                    i[j],i[j-1]=i[j-1],i[j]
            elif 'A' in list(map(lambda x:x[:1],i)) and 'Q' in list(map(lambda x:x[:1],i)):
                x=list(map(lambda x:x[:1],i)).index('A')
                #y=list(map(lambda x:x[:1],i)).index('Q')
                for j in range(x,len(i)):
                    if j<len(i)-1:
                        i[j],i[j+1]=i[j+1],i[j]
        for i in p1_win_dec:
            c.append(i)
        print(c,'p1_c')
        print(p1_win_dec,'p1_win_dec') 
        win_ctr=0
        if len(p1_win_dec)>=2:
            for i in win_dec:
                if i in win_list_type:
                    win_ctr+=1
                    p1_win_dec_1.append(i)
            if win_ctr>=2:
                pass #Declare turn 



def discard_logic(cards):
    #win_dec=[]
    q={'A':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[],'10':[],'J':[],'K':[],'Q':[]}
    q_flag={'A':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'J':0,'K':0,'Q':0}
    #win_dec=[]
    for i in cards:
        if i[::-1][0]=='#':
            q[i[:len(i)-2]].append(i)
            q_flag[i[:len(i)-2]]+=1
            #if q_flag[i[:len(i)-2]]==4:
            #    win_dec.append(q[i[0]])
        else:
            q[i[:len(i)-1]].append(i)
            q_flag[i[:len(i)-1]]+=1
            #if q_flag[i[:len(i)-1]]==4:
            #    win_dec.append(q[i[0]])
    #dtu=[[i,j] for i,j in q_flag.items()]
    
    srcc=q['A'] # variable with the suit with least cards
    for i,j in q_flag.items():
        if j>0:
            srcc=q[i][0]
            break 
    for i in q_flag.keys():
        if len(srcc.strip('#')[:-1])>=2:
            if q_flag[i]<q_flag[srcc.strip('#')[:-1]] and q_flag[i]>0 :
                srcc=i
    count_list=['AC',0]
    for i,j in q.items():
        airs=list(map(lambda x:x.strip('#'),j))
        for k in airs:
            if airs.count(k)>1 and count_list[1]<airs.count(k):
                count_list=[k,airs.count(k)]
    if count_list[1]>0:
        print(count_list,'count_list')
        return count_list[0] 
    if srcc:
        print(srcc,'srcc')
        return srcc
def pick_up_logic(cards):
    pass
def points(cards):
    points=0
    remove_nest(win_dec)
    remove_nest(win_dec_1)
    print(win_dec_unnested,'win_dec_unnested')
    for i in cards.keys():
        if i[::-1][0]!='#' and i not in win_dec_unnested:
            if i[0]=='J' or i[0]=='K' or i[0]=='Q':
                points+=10
            elif i[0]=='A':
                points+=1
            elif int(i[:len(i)-1])>1 and int(i[:len(i)-1])<=10:
                points+=int(i[:len(i)-1])
        elif i[::-1][0]=='#' and i not in win_dec_unnested:
            if i[0]=='J' or i[0]=='K' or i[0]=='Q':
                points+=10
            elif i[0]=='A':
                points+=1
            elif int(i[:len(i)-2])>1 and int(i[:len(i)-2])<=10:
                points+=int(i[:len(i)-2])

    return points
def points_p1(cards):
    points=0
    p1_remove_nest(p1_win_dec)
    p1_remove_nest(p1_win_dec_1)
    print(p1_win_dec_unnested,'p1_win_dec_unnested')
    for i in cards.keys():
        if i[::-1][0]!='#' and i not in p1_win_dec_unnested:
            if i[0]=='J' or i[0]=='K' or i[0]=='Q':
                points+=10
            elif i[0]=='A':
                points+=1
            elif int(i[:len(i)-1])>1 and int(i[:len(i)-1])<=10:
                points+=int(i[:len(i)-1])
        elif i[::-1][0]=='#' and i not in p1_win_dec_unnested:
            if i[0]=='J' or i[0]=='K' or i[0]=='Q':
                points+=10
            elif i[0]=='A':
                points+=1
            elif int(i[:len(i)-2])>1 and int(i[:len(i)-2])<=10:
                points+=int(i[:len(i)-2])

    return points


def p1_remove_nest(l):
    global p1_win_dec_unnested
    for i in l:
        if type(i)==list:
            remove_nest(i)
        else:
            p1_win_dec_unnested.append(i)

#win_dec_unnested=[]
def remove_nest(l):
    global win_dec_unnested
    for i in l:
        if type(i)==list:
            remove_nest(i)
        else:
            win_dec_unnested.append(i)
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def text_objects1(text, font):
    textSurface = font.render(text, True, (255,255,255))
    return textSurface, textSurface.get_rect()
def message_display(text,x,y,size):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    largeText = pygame.font.SysFont('comicsans',size)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
def message_display1(text,x,y,size):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    largeText = pygame.font.SysFont('comicsans',size)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x,y)
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
card_back=pygame.image.load('Gray_back.jpg')
card_back=pygame.transform.scale(card_back,(80,120))
cards=['2C','3C','4C','5C','6C','7C','8C','9C','10C','KC','QC','JC','AC',
'2H','3H','4H','5H','6H','7H','8H','9H','10H','KH','QH','JH','AH',
'2D','3D','4D','5D','6D','7D','8D','9D','10D','KD','QD','JD','AD',
'2S','3S','4S','5S','6S','7S','8S','9S','10S','KS','QS','JS','AS']
p1_cards={}
comp_cards={}
for i in range(13):
    a=random.choice(cards)
    if a not in p1_cards.keys():
        p1_cards[a]=True
    else:
        while a in p1_cards:
            a=random.choice(cards)
        p1_cards[a]=True
for i in range(13):
    a=random.choice(cards)
    if a not in comp_cards.keys():
        comp_cards[a]=True
    else:
        while a in comp_cards:
            a=random.choice(cards)
        comp_cards[a]=True
for i in cards:
    if i not in comp_cards.keys():
        stock_pile.append(i)
for i in cards:
    if i not in p1_cards.keys():
        stock_pile.append(i)
print(p1_cards)
gamebg=pygame.image.load('gamebg.jpg')
gamebg=pygame.transform.scale(gamebg,(1200,750))
gameDisplay.blit(gamebg,(0,0))
#gameDisplay.fill(green)
x=10
p1_cards_images={}
comp_cards_images={}
flag=0
ctr=0
x_coordinates=[]
x_cards=[]
j=0
card_image_list=[i for i in range(14)]
for i in p1_cards.keys():
    #b=i+str(ctr)
    card_image_list[j]=pygame.image.load('{}.png'.format(i))
    card_image_list[j]=pygame.transform.scale(card_image_list[j],(80,120))
    p1_cards_images[i]=[card_image_list[j],[x,450],0,i]
    ctr+=1
    j+=1
    #gameDisplay.blit(b,(x,250))
    x_coordinates.append([x,450])
    x_cards.append([x,450])
    x+=80
x_coordinates.append([x,450])
j=0
x=10
ctr=0
for i in comp_cards.keys():
    #b=i+str(ctr)
    card_image_list[j]=pygame.image.load('{}.png'.format(i))
    card_image_list[j]=pygame.transform.scale(card_image_list[j],(80,120))
    comp_cards_images[i]=[card_image_list[j],[x,150],0,i]
    ctr+=1
    j+=1
    #print(x)
    #gameDisplay.blit(b,(x,250))
    x+=90
j=0
comp_cards_copy=comp_cards_images
p1_cards_copy=p1_cards_images
#x=10
ctr=0
card_image_list=[i for i in range(len(stock_pile))]
for i in range(len(stock_pile)):
    #b=i+str(ctr)
    card_image_list[j]=pygame.image.load('{}.png'.format(stock_pile[i]))
    card_image_list[j]=pygame.transform.scale(card_image_list[j],(80,120))
    stock_pile[i]=[card_image_list[j],[50,150],0,stock_pile[i]]
    ctr+=1
    j+=1
    #print(x)
    #gameDisplay.blit(b,(x,250))
    #x+=90
discarded_pile.append([stock_pile[0][0],[1000,150],0,stock_pile[0][3]])
stock_pile.pop(0)
print(p1_cards_images)
ctr=0
crashed=False
p1_cards_list=[i for i in p1_cards_images.keys()]
p1_card_flag=0
dicard_flag=0
pick_up_flag=0
start=0
move=0
qwerty=pygame.image.load('C:\\Users\\Tushar\\AppData\\Local\\Programs\\Python\\Python37-32\\game-rummy\\logo.jpg')
azerty=pygame.image.load('C:\\Users\\Tushar\\AppData\\Local\\Programs\\Python\\Python37-32\\game-rummy\\wallpaper.jpg')
qwerty=pygame.transform.scale(qwerty,(500,300))
azerty=pygame.transform.scale(azerty,(1200,900))

def showCards():
    global p1_card_flag
    for i in p1_cards_list:
        #print(card_image_list[j])
        x,y=p1_cards_images[i][1][0],p1_cards_images[i][1][1]

        gameDisplay.blit(p1_cards_images[i][0],(x,y))
        #select(x,y,p1_cards_images[i][2])
        x1,y1=pygame.mouse.get_pos()
        #print(x1,y1)
        if p1_cards_images[i.strip('#')][2]==1:
                pygame.draw.circle(gameDisplay,white,(x,y),10)
        if x1>x and x1<x+70 and y1>y and y1<y+120:
            if p1_cards_images[i][2]==1:
                pygame.draw.circle(gameDisplay,white,(x,y),10)
            else:
                pygame.draw.circle(gameDisplay,(0,0,0),(x,y),10)
                if pygame.mouse.get_pressed()[0] :
                    p1_cards_images[i][2]=1
                    pygame.draw.circle(gameDisplay,white,(x,y),10)
                    p1_card_flag+=1
    j=[0,0]
    if p1_card_flag==2:
        #print('heeeee')
        p1_card_flag=0
        i=0
        while i<len(p1_cards_list):
            if p1_cards_images[p1_cards_list[i]][2]==1:
                x,y=p1_cards_images[p1_cards_list[i]][1][0],p1_cards_images[p1_cards_list[i]][1][1]
                #print(x,y)
                p1_cards_images[p1_cards_list[i]][2]=0
                j[0]=i
                i+=1
                while p1_cards_images[p1_cards_list[i]][2]!=1:
                    i+=1
                j[1]=i
                #print(j[1])
                p1_cards_images[p1_cards_list[i]][2]=0
                x1,y1=p1_cards_images[p1_cards_list[i]][1][0],p1_cards_images[p1_cards_list[i]][1][1]
                #print(x1,y1)
                p1_cards_images[p1_cards_list[j[0]]][1]=[x1,y1]
                p1_cards_images[p1_cards_list[j[1]]][1]=[x,y]
                p1_cards_list[j[0]],p1_cards_list[j[1]]=p1_cards_list[j[1]],p1_cards_list[j[0]]
                j=[0,0]
                time.sleep(0.2)
                break
            i+=1
ctr123=0
print(len(comp_cards_images.keys()),'begin cards in comp dec')
pygame.mixer.music.load('PokerFace.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.5)
while not crashed:

    #x=10
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            crashed=True
    gameDisplay.blit(gamebg,(0,0))
    if start==0:
        gameDisplay.fill((0,0,0))
        message_display1('Indian Rummy',display_width/2,display_height/2-100,90)
        message_display1('Loading...',display_width/2,display_height/2+100,90)

        for i in range(100):
            loading((display_width/2-100,display_height/2),(200,20),i/100)
            pygame.display.update()
            time.sleep(0.1)
        #time.sleep(5)
        gameDisplay.fill(green)
        gameDisplay.blit(azerty,(0,0))
        #pygame.mixer.music.load('indian-rummy.mp3')
        #pygame.mixer.music.play()
        #pygame.mixer.music.unload()
        start+=1
        #time.sleep(1)
        message_display('Shuffling the deck....',display_width/2,700,20)
        time.sleep(1)
        pygame.display.update()
        gameDisplay.fill(green)
        #message_display('Indian Rummy',display_width/2,100,90)
        gameDisplay.blit(azerty,(0,0))

        #time.sleep(1)
        pygame.display.update()
        gameDisplay.fill(green)
        #message_display('Indian Rummy',display_width/2,100,90)
        gameDisplay.blit(azerty,(0,0))

        message_display('Distributing Cards....',display_width/2,700,20)
        time.sleep(1)
        pygame.display.update()
        gameDisplay.fill(green)
        #message_display('Indian Rummy',display_width/2,100,90)
        gameDisplay.blit(azerty,(0,0))

        message_display('Your game starts in 5 seconds....',display_width/2,700,20)
        time.sleep(5)
    gameDisplay.blit(gamebg,(0,0))
    #gameDisplay.fill(green)
    #print(p1_cards_list)
    showCards()
    gameDisplay.blit(card_back,(50,150))
    gameDisplay.blit(discarded_pile[0][0],[1000,150])
    if move==0 and pick_up_flag==0:
        ty=pygame.image.load('image-removebg-preview.png')
        ty=pygame.transform.scale(ty,(700,320))
        gameDisplay.blit(ty,(250,100))
        showCards()
        message_display1('Computer is making a move',display_width/2,650,30)
        time.sleep(1)
        pygame.display.update()
        gameDisplay.blit(gamebg,(0,0))
        #gameDisplay.fill(green)
        showCards()
        gameDisplay.blit(discarded_pile[0][0],(1000,150))
        gameDisplay.blit(card_back,(50,150))
        z=random.choice([stock_pile,discarded_pile])
        if z[0][3] not in comp_cards_images.keys():
            comp_cards_images[z[0][3]]=[z[0][0],[900,150],0,z[0][3]]
            z.pop(0)
        else:
            comp_cards_images[z[0][3]+'#']=[z[0][0],[900,150],0,z[0][3]]
            z.pop(0)
        gameDisplay.blit(ty,(250,100))
        showCards()
        pygame.display.update()
        gameDisplay.blit(gamebg,(0,0))
        #computer discarding a card 
        #gameDisplay.fill(green)
        #v=list(comp_cards_images.keys())
        #z=random.choice(v)
        if len(discard_logic(comp_cards_images))>=2:
            z=discard_logic(comp_cards_images)
            print(z,'z')
            discarded_pile.insert(0,comp_cards_images[z])
        else:
            v=list(comp_cards_images.keys())
            z=random.choice(v)
        del comp_cards_images[z]
        gameDisplay.blit(card_back,(50,150))
        if discarded_pile:
            gameDisplay.blit(discarded_pile[0][0],(1000,150))
        else:
            pygame.draw.rect(gameDisplay,(255,255,255,0),(1000,150,80,120))

            #pygame.rect
        move=1
        showCards()
        gameDisplay.blit(ty,(250,100))
        gameDisplay.blit(card_back,(50,150))
        if discarded_pile:
            gameDisplay.blit(discarded_pile[0][0],(1000,150))
        else:
            pygame.draw.rect(gameDisplay,(255,255,255,0),(1000,150,80,120))
        pygame.display.update()
        gameDisplay.blit(gamebg,(0,0))
        #gameDisplay.fill(green)
        showCards()
        gameDisplay.blit(ty,(250,100))
        gameDisplay.blit(card_back,(50,150))
        gameDisplay.blit(discarded_pile[0][0],(1000,150))
        #select(50,150,0)
        select1(stock_pile[0])
        select1(discarded_pile[0])
        time.sleep(0.2)
        pick_up_flag=1
        print(len(comp_cards_images.keys()),'cards in comp dec start')
        #ctr123+=1
    if pick_up_flag==1 and move==1:
        message_display('Pick a card',display_width/2,650,30)
        flag=0
        while not flag and not crashed: 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    crashed=True
            gameDisplay.blit(gamebg,(0,0))
            #gameDisplay.fill(green)
            ty=pygame.image.load('image-removebg-preview.png')
            ty=pygame.transform.scale(ty,(700,320))
            gameDisplay.blit(ty,(250,100))
            showCards()
            message_display1('Pick a card',display_width/2,650,30)
            gameDisplay.blit(card_back,(50,150))
            gameDisplay.blit(discarded_pile[0][0],(1000,150))
            pygame.display.update()
            select1(stock_pile[0])
            x1,y1=pygame.mouse.get_pos()
            if discarded_pile[0][2]==1:
                    #print('whie')
                    pygame.draw.circle(gameDisplay,white,(1000,150),10)
            if x1>1000 and x1<1120 and y1>150 and y1<150+70:
                #print('erer')
                if discarded_pile[0][2]==1:
                    pygame.draw.circle(gameDisplay,white,(1000,150),10)
                else:
                    #print('brgbr')
                    pygame.draw.circle(gameDisplay,(0,0,0),(1000,150),10)
                    if pygame.mouse.get_pressed()[0] :
                        #print('yesss')
                        discarded_pile[0][2]=1
                        pygame.draw.circle(gameDisplay,white,(1000,150),10)
            if stock_pile[0][2]==1 :
                #p1_cards_list.append(stock_pile[0][3])
                if stock_pile[0][3] not in p1_cards_images.keys():
                    for i in x_coordinates:
                        if i not in x_cards:
                            p1_cards_images[stock_pile[0][3]]=[stock_pile[0][0],i,0,stock_pile[0][3]]
                            p1_cards_list.append(stock_pile[0][3])
                            print(i)
                            x_cards.append(i)
                            #ctr123+=1
                else:
                    for i in x_coordinates:
                        if i not in x_cards:
                            p1_cards_images[stock_pile[0][3]+'#']=[stock_pile[0][0],i,0,stock_pile[0][3]+'#']
                            p1_cards_list.append(stock_pile[0][3]+'#')
                            print(i)
                            x_cards.append(i)
                            #ctr123+=1
                stock_pile.pop(0)
                pick_up_flag=0
                flag=1
                ctr123+=1
            if discarded_pile[0][2]==1 :
                #p1_cards_list.append(discarded_pile[0][3])
                if discarded_pile[0][3] not in p1_cards_images.keys():
                    for i in x_coordinates:
                        if i not in x_cards:
                            p1_cards_images[discarded_pile[0][3]]=[discarded_pile[0][0],i,0,discarded_pile[0][3]]
                            p1_cards_list.append(discarded_pile[0][3])
                            print(i)
                            x_cards.append(i)
                else:
                    for i in x_coordinates:
                        if i not in x_cards:
                            p1_cards_images[discarded_pile[0][3]+'#']=[discarded_pile[0][0],i,0,discarded_pile[0][3]]
                            p1_cards_list.append(discarded_pile[0][3]+'#')
                            print(i)
                            x_cards.append(i)
                discarded_pile.pop(0)
                pick_up_flag=0
                flag=1
                ctr123+=1
        gameDisplay.blit(gamebg,(0,0))
        #gameDisplay.fill(green)
        showCards()
        gameDisplay.blit(card_back,(50,150))
        if not discarded_pile:
            gameDisplay.blit(card_back,(50,150))
        else:
            gameDisplay.blit(discarded_pile[0][0],(1000,150))
        #time.sleep(1)
        pygame.display.update()
            
    if pick_up_flag==0 and move==1:
        ty=pygame.image.load('image-removebg-preview.png')
        ty=pygame.transform.scale(ty,(700,320))
        gameDisplay.blit(ty,(250,100))
        message_display1('Discard one card',display_width/2,650,30)
        showCards()
        gameDisplay.blit(card_back,(50,150))
        if discarded_pile:
            gameDisplay.blit(discarded_pile[0][0],(1000,150))
        else:
            pygame.draw.rect(gameDisplay,white,(1000,150,80,120))
        pygame.display.update()
        flag=0
        while not flag and not crashed: 
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    crashed=True
            for i in p1_cards_list:
                x,y=p1_cards_images[i][1][0],p1_cards_images[i][1][1]
                x1,y1=pygame.mouse.get_pos()
                if x1>x and x1<x+70 and y1>y and y1<y+120:
                    if p1_cards_images[i][2]==1:
                        pygame.draw.circle(gameDisplay,white,(x,y),10)
                    else:
                        pygame.draw.circle(gameDisplay,(0,0,0),(x,y),10)
                        if pygame.mouse.get_pressed()[0] :
                            p1_cards_images[i][2]=1
                            x_cards.remove(p1_cards_images[i][1])
                            pygame.draw.circle(gameDisplay,white,(x,y),10)
                            discarded_pile.insert(0,p1_cards_images[i])
                            p1_cards_list.remove(i)

                            del p1_cards_images[i]
                            flag=1
                            ctr123+=1
                            #p1_card_flag+=1
            pick_up_flag=0
            move=0
            #ctr123+=1
    select(1000,150,0)
    #p1_cards_copy=p1_cards_images
    comp_logic(comp_cards_copy)
    print(ctr123)
    if ctr123>=20:
        print(ctr123)
        gameDisplay.fill((242,38,19))
        message_display('Game Over',display_width/2,display_height/2,30)
        #p1_logic(p1_cards_images)
        showCards()
        x=10
        for i in comp_cards_images.keys():
            #print(card_image_list[j])
            #x,y=p1_cards_images[i][1][0],p1_cards_images[i][1][1]
            gameDisplay.blit(comp_cards_images[i][0],(x,150))
            x+=80
        p1_logic(p1_cards_images)
        message_display('COM Points :'+str(points(comp_cards_images)),display_width/2,(display_height/2)-40,30)
        message_display('YOUR Points :'+str(points_p1(p1_cards_images)),display_width/2,(display_height/2)+40,30)
        time.sleep(10)
        crashed=True
    print(len(comp_cards_images.keys()),'cards in comp dec')
    #pygame.mixer.music.fadeout(100)
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    pygame.display.update()
    clock.tick(120)
quit()
#background music credits : Poker Face by Lady Gaga
#Image courtsey: Google Images
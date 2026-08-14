import cube
from move_parser import move
def solve_oll():
    u_turns = 0
    if cube.u1.color==cube.u2.color==cube.u3.color==cube.u4.color==cube.u6.color==cube.u7.color==cube.u8.color==cube.u9.color:
        oll_solved = True
    else:
        oll_solved = False
    while not oll_solved:
        if cube.u1.color==cube.u2.color==cube.u3.color==cube.u4.color==cube.u6.color==cube.u7.color==cube.u8.color==cube.u9.color:
            oll_solved = True
        #yellow cross already complete, 7 cases
        if(cube.u2.color==cube.u4.color==cube.u6.color==cube.u8.color=='y'):
            if cube.u7.color=='y':
                if cube.f3.color==cube.r3.color==cube.b3.color=='y':
                    move("r u r' u r u2 r'")
                    oll_solved = True
                elif cube.u9.color==cube.b1.color==cube.b3.color=='y':
                    move("r2 d' r u2 r' d r u2 r")
                    oll_solved = True
                elif cube.u3.color==cube.f3.color==cube.l1.color=='y':
                    move("f' l x u r' u' l' x' f r")
                    oll_solved = True
            elif cube.u3.color=='y':
                if cube.r1.color==cube.f1.color==cube.l1.color=='y':
                    move("r u2 r' u' r u' r'")
                    oll_solved = True
                elif cube.u9.color==cube.f1.color==cube.b3.color=='y':
                    move("l x u r' u' l' x' f r f'")
                    oll_solved = True
            else:
                if cube.l1.color==cube.l3.color=='y':
                    if cube.r1.color==cube.r3.color=='y':
                        move("r u r' u r u' r' u r u2 r'")
                        oll_solved = True
                    elif cube.f3.color==cube.b1.color=='y':
                        move("r u2 r2 u' r2 u' r2 u2 r")
                        oll_solved = True
        #cases where yellow edges form 'bar', 15 cases
        elif cube.u4.color==cube.u6.color=='y':
            if cube.u9.color==cube.u3.color=='y':
                if cube.u1.color=='y':
                    move("r u r' u' m u r u' l' x'")
                    oll_solved = True
                else:
                    if cube.f1.color=='y':
                        move("r u r' u' r' f r f'")
                        oll_solved = True
                    else:
                        move("f r u r' u' f'")
                        oll_solved = True
            elif cube.u9.color==cube.u1.color=='y':
                if cube.l3.color=='y':
                    move("r' f r u r' u' f' u r")
                    oll_solved = True
            elif cube.u9.color=='y':
                if cube.f1.color=='y':
                    move("r' f r u r' f' r f u' f'")
                    oll_solved = True
                elif cube.l3.color=='y':
                    move("l' x' u' l x r' u' r u l' x' u l x")
                    oll_solved = True
            elif cube.u3.color==cube.u1.color=='y':
                if cube.l3.color=='y':
                    move("f r u r' u' r' f' l x u r u' l' x'")
                    oll_solved = True
                else:
                    move("u' r' u' r' f r f' u r u")
                    oll_solved = True
            elif cube.u3.color==cube.u7.color=='y':
                if cube.r1.color=='y':
                    move("l f' l' u' l u f u' l'")
                    oll_solved = True
            elif cube.u3.color=='y':
                if cube.l1.color=='y':
                    move("l x u l' x' r u r' u' l x u' l' x'")
                    oll_solved = True
            elif cube.u7.color=='y':
                if cube.f3.color=='y':
                    move("l x u' l' x' u' l x u l' x' f' u f")
                    oll_solved = True
            #no corners oriented
            elif cube.u1.color!='y' and cube.u3.color!='y' and cube.u7.color!='y' and cube.u9.color!='y':
                if cube.l3.color==cube.r1.color=='y':
                    if cube.l1.color=='y':
                        move("f r u r' u' r f' l x u r' u' l' x'")
                        oll_solved = True
                    else:
                        move("f r u r' u f' u' f u' f'")
                        oll_solved = True
                elif cube.f3.color==cube.b1.color=='y':
                    if cube.l1.color=='y':
                        move("f s r u r' u' r u r' u' f' s'")
                        oll_solved = True
                    else:
                        move("u r u2 r2 u' r u' r' u2 f r f'")
                        oll_solved = True
        #no edges oriented, 8 cases
        elif cube.u2.color!='y' and cube.u4.color!='y' and cube.u6.color!='y' and cube.u8.color!='y':
            #no corners oriented
            if cube.u1.color!='y' and cube.u3.color!='y' and cube.u7.color!='y' and cube.u9.color!='y':
                if cube.l1.color==cube.l3.color=='y':
                    if cube.f3.color=='y':
                        move("f r u r' u' s r u r' u' f' s'")
                        oll_solved = True
                    else:
                        move("r u2 r2 f r f' u2 r' f r f'")
                        oll_solved = True
            #all corners solved
            elif cube.u1.color==cube.u3.color==cube.u7.color==cube.u9.color=='y':
                move("r m u r' u' m2 u r u' r' u' m")
                oll_solved = True
            elif cube.u1.color==cube.u3.color=='y':
                if cube.l3.color==cube.r1.color=='y':
                    move("m' u r u r' u' r m r2 f r f'")
                    oll_solved = True
                else:
                    move("r m u r' u r u2 r2 m2 u' r u' r' u2 r m")
                    oll_solved = True
            elif cube.u1.color==cube.u9.color==cube.l3.color=='y':
                move("r u r' u r' f r f' u2 r' f r f'")
                oll_solved = True
            elif cube.u9.color==cube.l3.color==cube.b3.color==cube.r3.color=='y':
                move("f s r u r' u' f' s' u' f r u r' u' f'")
                oll_solved = True
            elif cube.u3.color==cube.r1.color==cube.f1.color==cube.l1.color=='y':
                move("f s r u r' u' f' s' u f r u r' u' f'")
                oll_solved = True
        #edges form bend-shape, with edges u2 and u4 oriented, 12 cases
        elif cube.u2.color==cube.u4.color=='y':
            #all corners solved
            if cube.u1.color==cube.u3.color==cube.u7.color==cube.u9.color=='y':
                move("r m u r' u' m' u r u' r'")
                oll_solved = True
            elif cube.u1.color==cube.u9.color==cube.f1.color==cube.r3.color=='y':
                move("f r u' r' u' r u r' f'")
                oll_solved = True
            elif cube.u1.color==cube.u7.color==cube.r1.color==cube.r3.color=='y':
                move("f u r u' r' f'")
                oll_solved = True
            elif cube.u3.color==cube.u7.color==cube.r1.color==cube.b3.color=='y':
                move("r u r' u r u' r' u' r' f r f'")
                oll_solved = True
            elif cube.u7.color==cube.u9.color=='y':
                if cube.l1.color==cube.r3.color=='y':
                    move("f r' f r2 u' r' u' r u r' f2")
                    oll_solved = True
                else:
                    move("r u r' u r u2 r' f r u r' u' f'")
                    oll_solved = True
            elif cube.u3.color==cube.b3.color==cube.l3.color==cube.f3.color=='y':
                move("r m u r' u r' f r f' r u2 r' m'")
                oll_solved = True
            elif cube.u7.color==cube.b3.color==cube.r3.color==cube.f3.color=='y':
                move("r m u r' u r u2 r' m'")
                oll_solved = True
            elif cube.u9.color==cube.b1.color==cube.l1.color==cube.f1.color=='y':
                move("r u r' u' r' f r2 u r' u' f'")
                oll_solved = True
            #no corners solved
            else:
                if cube.f1.color==cube.r1.color==cube.r3.color==cube.b3.color=='y':
                    move("r' f r2 b' r2 f' r2 b r'")
                    oll_solved = True
                elif cube.f1.color==cube.f3.color==cube.b1.color==cube.b3.color=='y':
                    move("r m u2 r' u' r u r' u' r u' r' m'")
                    oll_solved = True
                elif cube.l1.color==cube.l3.color==cube.f3.color==cube.b1.color=='y':
                    move("f r u r' u' r u r' u' f'")
                    oll_solved = True
        #edges form bend-shape, with edges u4 and u8 oriented, 8 cases
        elif cube.u4.color==cube.u8.color=='y':
            if cube.u1.color==cube.u3.color==cube.f1.color==cube.f3.color=='y':
                move("r' u' r u' r' u2 r f r u r' u' f'")
                oll_solved = True
            elif cube.u1.color==cube.u7.color==cube.f3.color==cube.b1.color=='y':
                move("y' s r u r' u' f' s' u' f y")
                oll_solved = True
            elif cube.u1.color==cube.u9.color==cube.f1.color==cube.r3.color=='y':
                move("r' u' r u' r' u r u x' r u' r' u x")
                oll_solved = True
            elif cube.u1.color==cube.f1.color==cube.r1.color==cube.b1.color=='y':
                move("r' m' u' r u' r' u2 r m")
                oll_solved = True
            elif cube.u3.color==cube.b3.color==cube.l3.color==cube.f3.color=='y':
                move("r u r' u r' f r f' r u2 r'")
                oll_solved = True
            elif cube.u9.color==cube.b1.color==cube.l1.color==cube.f1.color=='y':
                move("u' f r u r' u' f' u f r u r' u' f'")
                oll_solved = True
            else:
                if cube.f1.color==cube.r1.color==cube.r3.color==cube.b3.color=='y':
                    move("r b' r2 f r2 b r2 f' r")
                    oll_solved = True
                elif cube.f1.color==cube.f3.color==cube.b1.color==cube.b3.color=='y':
                    move("r' m' u2 r u r' u' r u r' u r m")
                    oll_solved = True
        #edges form bend-shape, with edges u2 and u6 oriented, 4 cases
        elif cube.u2.color==cube.u6.color=='y':
            if cube.u3.color==cube.u9.color==cube.l1.color==cube.l3.color=='y':
                move("f' u' l' u l f")
                oll_solved = True
            elif cube.u7.color==cube.u9.color==cube.l1.color==cube.r3.color=='y':
                move("r' f r f' r u2 r' u' f' u' f")
                oll_solved = True
            elif cube.u3.color==cube.l1.color==cube.f1.color==cube.r1.color=='y':
                move("r m u2 r' u' r u' r' m'")
                oll_solved = True
            elif cube.f1.color==cube.r1.color==cube.r3.color==cube.b3.color=='y':
                move("r' u' r' f r f' r' f r f' u r")
                oll_solved = True
        #edges form bend-shape, with edges u6 and u8 oriented, 3 cases
        elif cube.u6.color==cube.u8.color=='y':
            if cube.u1.color==cube.u9.color==cube.f1.color==cube.r3.color=='y':
                move("r u2 r2 f r f' r u2 r'")
                oll_solved = True
            elif cube.u3.color==cube.u9.color==cube.f1.color==cube.b3.color=='y':
                move("s r u r' u' r' f r f' s'")
                oll_solved = True
            elif cube.u9.color==cube.r3.color==cube.b3.color==cube.l3.color=='y':
                move("r' m' u2 r u r' u r m")
                oll_solved = True
        #rotate u-face to re-analyze case
        if not oll_solved:
            move("u")
            u_turns+=1
            print(f"u-turn #{u_turns}")
            if u_turns>=4:
                print("No case detected")
                break

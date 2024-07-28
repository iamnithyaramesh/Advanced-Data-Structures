def stable_marriage():
    no_of_women=int(input('No of men'))
    no_of_men=int(input('No of women'))
    list_of_women=[]
    list_of_men=[]
    pairings=[]
    for i in range(no_of_women):
        list=[]
        name=input('Enter name')
        list.append(name)
        list.append('None')
        list_of_men.append(list)

    for j in range(no_of_men):
        list=[]
        name=input('Enter name')
        list.append(name)
        list.append('None')
        list_of_women.append(list)
    
    dominance=input("Enter M for Male/Enter F for Female")
    if dominance=='M':
        print('List of available women',list_of_women)
        for man in list_of_men:
            priority_list=[]
            for women in list_of_women:
                priority=int(input(f'Enter priority from 1 to {len(list_of_women)}'))
                priority_list.append({priority:'No'})
            man[1]=priority_list
        print('List of available men',list_of_men)
        for woman in list_of_women:
            priority_list=[]
            for men in list_of_men:
                priority=int(input(f'Enter priority from 1 to {len(list_of_women)}'))
                priority_list.append({priority:'No'})
            woman[1]=priority_list
        print(list_of_women)
        for man in list_of_men:
            for rank in man[1]:
                for women in list_of_women:
                    for x in women[1]:
                     if int(x.keys()[0])+1==rank and women[1].items()=='No':
                        pairings.append(man[0],women[0])
        print(pairings)

    else:
        print('List of available men',list_of_men)
        for woman in list_of_women:
            priority_list=[]
            for men in list_of_men:
                priority=int(input(f'Enter priority from 1 to {len(list_of_women)}'))
                priority_list.append({priority:'No'})
            woman[1]=priority_list
        print('List of available women',list_of_women)
        for man in list_of_men:
            priority_list=[]
            for women in list_of_women:
                priority=int(input(f'Enter priority from 1 to {len(list_of_women)}'))
                priority_list.append({priority:'No'})
            man[1]=priority_list
        print(list_of_men)
        for woman in list_of_women:
            for rank in woman[1]:
                for men in list_of_men:
                    if men[1]+1==rank and men[1].items()=='No':
                        pairings.append(woman,men)
        print(pairings)
    
    

stable_marriage()

        



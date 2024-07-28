def stable_marriage(men_preferences, women_preferences):
    n = len(men_preferences)
    engaged = {}
    men_available = list(men_preferences.keys())

    while men_available:
        man = men_available[0]
        woman = men_preferences[man][0]

        if woman not in engaged:
            engaged[woman] = man
            men_available.remove(man)
        else:
            current_man = engaged[woman]
            if women_preferences[woman].index(man) < women_preferences[woman].index(current_man):
                engaged[woman] = man
                men_available.remove(man)
                men_available.append(current_man)

    return engaged

# Test the algorithm
men_preferences = {
    'John': ['Mary', 'Lisa', 'Kate'],
    'Mike': ['Lisa', 'Kate', 'Mary'],
    'Steve': ['Kate', 'Mary', 'Lisa']
}

women_preferences = {
    'Mary': ['Mike', 'Steve', 'John'],
    'Lisa': ['John', 'Steve', 'Mike'],
    'Kate': ['Steve', 'John', 'Mike']
}

engaged_couples = stable_marriage(men_preferences, women_preferences)

for woman, man in engaged_couples.items():
    print(f"{man} is engaged to {woman}")
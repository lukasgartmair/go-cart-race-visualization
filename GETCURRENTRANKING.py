def GetCurrentRanking(all_race_cars):
    
    covered_distance = [t.covered_distance for t in all_race_cars]

    covered_distance.sort(reverse=True)
    # fastest time will be first

    for c in all_race_cars:

        for (x,r) in enumerate(covered_distance):
            if c.covered_distance == r:
                c.rank = x
                
    

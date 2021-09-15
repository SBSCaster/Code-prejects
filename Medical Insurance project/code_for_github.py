"""
    Caster's Medical Insurance portfolio project
    """

# "With open()" creates a useful block that my project will be written in. 
# The With method will allow my code to close files after the block end
# I also use readlines() in a for loop, to pass and organize the data into managable lists
with open('insurance.csv') as scam:
    age = []
    sex = []
    bmi = []
    children = []
    smoker = []
    region = []
    charges = []
    for line in scam.readlines():
        middle_man = line.split(',')
        age.append(middle_man[0])
        sex.append(middle_man[1])
        bmi.append(middle_man[2])
        children.append(middle_man[3])
        smoker.append(middle_man[4])
        region.append(middle_man[5])
        charges.append(middle_man[6])

        """
        (I wanted to put this class on a separate file and import it. May do in edits)
        For my project, I will be making a class, with methods to compare, and anaylze the 
        data in insurance.csv. My methods are rather self-descriptive, but I will leave
        comment snippets for each
            """
    class ScammersInsight():
        def __init__(self, age, sex, bmi, children, smoker, region, charges):
            self.age = age
            self.sex = sex
            self.bmi = bmi
            self.children = children
            self.smoker = smoker
            self.region = region
            self.charges = charges

        # calculates average age of ages in csv
        def average_age(self):
            running_total = 0
            for num in age:
                if num != 'age':
                    running_total += float(num)
            return (running_total/(len(self.age) - 1))

        # calculates how many smokers to nonsmokers
        def too_many_smokers(self):
            running = 0
            not_running = 0
            for cig in smoker:
                if cig == 'yes':
                    not_running += 1
                else:
                    running += 1
            #print(f'There are {not_running} smokers, and {running} non-smokers. Roughly {round(not_running/running*100, 2)}% of people do smoke, according to this data')
            return (not_running, running) 

        # Average cost

        def average_cost(self):
            running = 0
            for cost in self.charges:
                if cost != 'charges\n':
                    running += float(cost)
            return (f'The average cost of this sca- insurance is roughly ${round(running/(len(self.charges)-1))}')

        """
        This is where things start becoming a bit more interesting. Calculating the 
        average cost for smokers, compared to non_smokers. 
        My plan is to slightly modify my too_many_smokers method, to incorporate
        it into this method.
            """
        def how_much_more_for_smokers(self):
            smokers = self.too_many_smokers()[0]
            non_smokers = self.too_many_smokers()[1]
            running_average = 0
            not_running_average = 0
            status_cost = list(zip(self.smoker, self.charges))
            for index in range(len(status_cost)):
                if status_cost[index][0] != 'smoker':
                    charge = status_cost[index][1]
                    if status_cost[index][0] == 'yes':
                        not_running_average += float(charge[:-2])
                    else:
                        running_average += float(charge[:-2])
            print(f'It cost on average ${round((not_running_average/smokers) - (running_average/non_smokers), 2)} more for smokers')
            return (round((not_running_average/smokers)), round(running_average/non_smokers)) 

        def kids_diction(self):
            status_children = list(zip(self.smoker, self.children))
            smoker_children_dict = {'Smokers with kids': [0, 0], 'Smokers without kids': [0, 0], 'Nonsmokers with kids': [0, 0], 'Nonsmokers without kids': [0, 0]}
            for index in range(len(status_children)):
                if status_children[index][0] != 'smoker':
                    if status_children[index][0] == 'yes' and float(status_children[index][1]) >= 1:
                        smoker_children_dict['Smokers with kids'][0] += 1
                        smoker_children_dict['Smokers with kids'][1] += float(self.charges[index])
                    elif status_children[index][0] == 'yes':
                        smoker_children_dict['Smokers without kids'][0] += 1
                        smoker_children_dict['Smokers without kids'][1] += float(self.charges[index])
                    elif status_children[index][0] == 'no' and float(status_children[index][1]) >= 1:
                        smoker_children_dict['Nonsmokers with kids'][0] += 1
                        smoker_children_dict['Nonsmokers with kids'][1] += float(self.charges[index])
                    else:
                        smoker_children_dict['Nonsmokers without kids'][0] += 1
                        smoker_children_dict['Nonsmokers without kids'][1] += float(self.charges[index])
            return smoker_children_dict

        def the_most_screwed(self):
            with_without_kids = self.kids_diction()
            smokers_with_kid = with_without_kids['Smokers with kids'][1]/with_without_kids['Smokers with kids'][0]
            smokers_without_kid = with_without_kids['Smokers without kids'][1]/with_without_kids['Smokers without kids'][0]
            nonsmokers_with_kid = with_without_kids['Nonsmokers with kids'][1]/with_without_kids['Nonsmokers with kids'][0]
            nonsmokers_without_kid = with_without_kids['Nonsmokers without kids'][1]/with_without_kids['Nonsmokers without kids'][0]
            print(f'Smokers with kids are paying {round(smokers_with_kid)} on average')
            print(f'Smokers without kids are paying {round(smokers_without_kid)} on average')
            print(f'Nonsmokers with kids are paying {round(nonsmokers_with_kid)} on average')
            print(f'Nonsmokers without kids are paying {round(nonsmokers_without_kid)} on average')
            return 'The conclusion to this project, is simply, do not smoke. Insurance hella expensive'


        




            
    insight = ScammersInsight(age, sex, bmi, children, smoker, region, charges)
    print(insight.the_most_screwed()) 
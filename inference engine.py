from pyswip import Prolog
prolog = Prolog()
prolog.consult("KnowledgeBase/FoodDoctor.pl")
print(list(prolog.query("is_allergen(chicken, Y)")))

# input
allergy_to = ['sesame']
food_name = 'ayam goreng mcd'
ingredient_list = ['chicken', 'sesame', 'salt']
# don't forget to lower case the string

# inference engine
# get list of food or substances,allergen_list that have the user allergy type
# check the ingredient_list either exist in the  allergen_list or not
# if yes, store what is detected,update the conflict_boolean,get the allergen type,
# if not proceed'

# output
conflict_boolean = [0 for i in range(len(allergy_to))]
extra_message = list # example : albumin is in egg category, is a haram product

if __name__ == '__main__':
    print("hello man")


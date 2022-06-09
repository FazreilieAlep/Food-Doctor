from pyswip import Prolog
import re


def processAllergen(user):
    prolog = Prolog()
    prolog.consult("C:/Users/FAZREILIE/PycharmProjects/FoodDoctorV2/KnowledgeBase/FoodDoctor.pl") # change this directory first
    foodname = user.food_name# user input
    ingredient = user.ingredient  # user input
    fooddesc = foodname.lower() + ', ' + ingredient.lower()

    # get the allergen list
    allergen_category = user.allergens  # user input
    aller_list = list()
    haram_dat = list()
    for allerCat in allergen_category:
        if allerCat != 'haram':
            prologQuery = 'is_allergen(X,' + allerCat + ').'
            l = list(prolog.query(prologQuery))
            temp_aller_list = [d['X'] for d in l]
            [aller_list.append(t) for t in temp_aller_list]
        else:
            temp_haram = processHaram(fooddesc,prolog)
            haram_dat.append(allergen_category.index('haram'))
            haram_dat.append(temp_haram[0])
            haram_dat.append(temp_haram[1])

    # determine either the food ingredient contains allergen or not
    conflict_boolean = [False for i in range(len(allergen_category))]  # output
    info = ''  # output
    extraInfo = ''
    for aller in aller_list:
        if bool(re.search(aller, fooddesc, re.IGNORECASE)):
            prologQuery = 'is_allergen(' + str(aller) + ',Y).'
            detected = list(prolog.query(prologQuery))
            info += aller + ' is in the ' + detected[0]['Y'] + ' allergen category\n'
            # update bool
            if not conflict_boolean[allergen_category.index(detected[0]['Y'])]:
                conflict_boolean[allergen_category.index(detected[0]['Y'])] = True

                # get extra info
                prologQuery2 = 'extra_info(' + detected[0]['Y'] + ',Y).'
                l2 = list(prolog.query(prologQuery2))
                temp_extraInfo_list = [d['Y'] for d in l2]
                for extra in temp_extraInfo_list:
                    extraInfo += extra + '\n'

    info += extraInfo + '\n'

    info += '\n' + haram_dat[2]
    conflict_boolean[haram_dat[0]] = haram_dat[1]
    # print(aller_list)
    # print(info)
    # print(conflict_boolean)
    return [conflict_boolean, info]


def processHaram(food_desc, prolog):
    haram_boolean = False
    info = ''
    prologQuery = 'is_haram(X,_).'
    l = list(prolog.query(prologQuery))
    haram_list = [t['X'] for t in l]

    for haram in haram_list:
        if bool(re.search(haram, food_desc, re.IGNORECASE)):
            prologQuery2 = 'is_haram(' + haram +',Y).'
            detected = list(prolog.query(prologQuery2))
            info += haram + ': ' + detected[0]['Y'] + '\n'
            if haram_boolean != True:
                haram_boolean = True

    return [haram_boolean, info]


# if __name__ == '__main__':
    # prolog = Prolog()
    # prolog.consult("KnowledgeBase/FoodDoctor.pl")
    # print('This is an allergy checker and haram detector Expert System')
    # print('-----------------------------------------------------------')
    # output = processAllergen()


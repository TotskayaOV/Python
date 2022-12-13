def f (list_1):
    result1 = not sum(list_1)
    result2 = not list_1[0] and not list_1[1] and not list_1[2]
    result = result1 == result2
    return result

predicators = [False, False, False]
result = f(predicators)
if result == True:
    predicators = [True, False, False]
    result = f(predicators)
    if result == True:
        predicators = [False, True, False]
        result = f(predicators)
        if result == True:
            predicators = [False, False, True]
            result = f(predicators)
            if result == True:
                predicators = [True, True, False]
                result = f(predicators)
                if result == True:
                    predicators = [True, False, True]
                    result = f(predicators)
                    if result == True:
                        predicators = [False, True, True]
                        result = f(predicators)
                        if result == True:
                            predicators = [True, True, True]
                            result = f(predicators)
                            if result == True:
                                print('Утверждение истинно')
else:
    print('Утверждение ложно')

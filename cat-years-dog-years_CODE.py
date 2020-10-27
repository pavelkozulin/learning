def human_years_cat_years_dog_years(human_years):
    '''
    подаем "возраст человека"
    получаем "возраст человека,возраст кота, возраст собаки"

    соотношения:
    ### Cat Years
    15 cat years for first year
    +9 cat years for second year
    +4 cat years for each year after that
    ### Dog Years
    15 dog years for first year
    +9 dog years for second year
    +5 dog years for each year after that

    >>> human_years_cat_years_dog_years(1)
    1, 15, 15
    >>> human_years_cat_years_dog_years(2)
    2, 24, 24
    >>> human_years_cat_years_dog_years(10)
    10, 56, 64
    '''
    if human_years == 1:
        cat_years = dog_years = 15
    elif human_years == 2:
        cat_years = dog_years = 24
    else:
        cat_years = 24 + (human_years - 2) * 4
        dog_years = 24 + (human_years - 2) * 5
    return(human_years, cat_years, dog_years)


'''Main module of gittutorial.

Everyone who is joining in tutorial will edit this module.
It is recommended to explain your module in the docstring at the top, here.
'''

__all__ = ['print_favorites', 'print_what_working_on']


def print_favorites() -> None:
    '''Print your favorite things.

    Please explain in the docstring what this function is.
    '''
    # "list[str]" clarifies that "favorites" contains strings.
    favorites: list[str] = ['Git', 'Tennis']

    print('Your favorite things:')
    for fav in favorites:
        print(f'- {fav}')


def print_what_working_on() -> None:
    '''Print what you are working on.'''
    works: list[str] = ['JWST and ALMA observations of high redshift galaxies']

    print('What are you working on?:')
    for w in works:
        print(f'- {w}')

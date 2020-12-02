"""Functions for displaying user interface"""


def start_menu():
    print('''Hello. You entered to the database with different trains where you can
     find out list ot their passengers, routes and some other information about them.
          To delete row from the table press                - 1
          To add row to the table press                     - 2
          To edit information in the table press            - 3
          To print chosen table                             - 4
          Exit - press                                      - 5\n\n''')

    return int(input('Enter the number: '))


def table_identification():
    print('''Choose the table with which you want work\n
              Table: train                - 1
              Table: route                - 2
              Table: passenger            - 3\n\n''')

    return int(input('Enter the number: '))


def del_row():
    return int(input('Enter keyword of the table(number/id): '))


def add_row(count):
    if count == 1:
        return (int(input('Enter train id: ')),
                int(input('Enter number of cars: ')),
                int(input('Enter year in which it was made: ')))
    elif count == 2:
        return (int(input('Enter route number: ')),
                input('Enter ending station: '))
    elif count == 3:
        return (int(input('Enter passenger id: ')),
                input('Enter passenger name: '))


def update_row(count):
    if count == 1:
        return (int(input('Enter new train id: ')),
                int(input('Enter number of cars: ')),
                int(input('Enter year in which it was made: ')),
                int(input('Enter previously train id: ')))
    elif count == 2:
        return (int(input('Enter new route number: ')),
                input('Enter ending station: '),
                int(input('Enter previously route number: ')))
    elif count == 3:
        return (int(input('Enter new passenger id: ')),
                input('Enter passenger name: '),
                int(input('Enter previously passenger id: ')))

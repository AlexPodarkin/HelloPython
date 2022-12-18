import view as v
import model as mod

def controller():
    choice = ''
    while choice != 5:
        choice = v.menu()
        if choice == 1:
            mod.add_workers()
        elif choice == 2:
            mod.search_workers()
        elif choice == 3:
            mod.del_workers()
        elif choice == 4:
            mod.csv_to_json()
    
    else:
        print('Работа программы окончена!')




import model
import view


while True:
    query = view.start_menu()
    if query == 1:
        count = view.table_identification()
        if count == 1:
            param_1 = view.del_row()
            model.delete_elem(0, param_1)
        elif count == 2:
            param_1 = view.del_row()
            model.delete_elem(1, param_1)
        elif count == 3:
            param_1 = view.del_row()
            model.delete_elem(2, param_1)
    elif query == 2:
        count = view.table_identification()
        if count == 1:
            param_1, param_2, param_3 = view.add_row(count)
            model.add_elem(0, param_1, param_2, param_3)
        elif count == 2:
            param_1, param_2 = view.add_row(count)
            model.add_elem(1, param_1, param_2, 1)
        elif count == 3:
            param_1, param_2 = view.add_row(count)
            model.add_elem(2, param_1, param_2, 1)
    elif query == 3:
        count = view.table_identification()
        if count == 1:
            param_1, param_2, param_3, param_4 = view.update_row(count)
            model.update_elem(0, param_1, param_2, param_3, param_4)
        elif count == 2:
            param_1, param_2, param_4 = view.update_row(count)
            model.update_elem(1, param_1, param_2, 1, param_4)
        elif count == 3:
            param_1, param_2, param_4 = view.update_row(count)
            model.update_elem(2, param_1, param_2, 1, param_4)
    elif query == 4:
        count = view.table_identification()
        if count == 1:
            model.print_table(count)
        elif count == 2:
            model.print_table(count)
        elif count == 3:
            model.print_table(count)
        elif count == 4:
            model.print_table(count)
        elif count == 5:
            model.print_table(count)
    elif query == 5:
        break

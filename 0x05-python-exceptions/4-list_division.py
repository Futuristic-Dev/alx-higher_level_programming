#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_div = []

    for x in range(list_length):
        div = 0

        try:
            div = my_list_1[x] / my_list_2[x]
        except(ValueError, ZeroDivisionError):
            print("division by 0")
            div = 0
        except (TypeError):
            print("Wrong type")
            div = 0
        except (IndexError):
            print("out of range")
            div = 0

        finally:
            list_div.append(div)

        return list_div

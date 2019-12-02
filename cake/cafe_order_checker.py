take_out_list = []
din_in_list = [2, 4, 6]
service_order_list = [2,4,6,7]


def check_service_order():

    take_out_index = 0
    take_out_max = len(take_out_list)
    dine_in_index = 0
    dine_in_max = len(din_in_list)

    for i in range(len(service_order_list)):
        if take_out_index == take_out_max and dine_in_index == dine_in_max:
            return False
        elif dine_in_index == dine_in_max:
            if take_out_list[take_out_index] != service_order_list[i]:
                return False
            else:
                take_out_index += 1
        elif take_out_index == take_out_max:
            if din_in_list[dine_in_index] != service_order_list[i]:
                return False
            else:
                dine_in_index += 1
        else:
            if din_in_list[dine_in_index] == service_order_list[i]:
                dine_in_index += 1
            elif take_out_list[take_out_index] == service_order_list[i]:
                take_out_index += 1
            else:
                return False
    return True

print(check_service_order())
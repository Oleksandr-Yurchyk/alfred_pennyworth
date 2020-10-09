from typing import List, Dict, Union, Callable

# We will work with such dicts
ST = Dict[str, Union[str, int]]
# And we will put this dicts in list
DT = List[ST]


def task_1_fix_names_start_letter(data: DT) -> DT:
    # Solve using for loop
    lst = []
    for student in data:
        if student.get('name') is not None:
            student['name'] = student['name'][0].upper() + student['name'][1:]
        lst.append(student)
    return lst

    # I can`t finish this task using List- or DictComprehension
    # lst = [student['name'][0].upper() + student['name'][1:] for student in data]


def task_2_remove_dict_fields(data: DT, redundant_keys: List[str]) -> DT:
    # Delete keys using ListComprehension
    [student.pop(redundant_keys[i]) for student in data for i in range(len(redundant_keys))]
    return data

    # Delete keys using for loop
    # lst = []
    # for student in data:
    #     for i in range(len(redundant_keys)):
    #         student.pop(redundant_keys[i])
    #         del student[redundant_keys[i]]
    #     lst.append(student)
    # return lst


def task_3_find_item_via_value(data: DT, value) -> DT:
    # Solve using filter function
    return list(filter(lambda v: v['name'] in value, data))

    # Solve using for loop
    # for student in data:
    #     for k, v in student.items():
    #         if student[k] == value:
    #             lst.append(student)
    # return lst


def task_4_return_lambda_sum_2_ints():          # I think this func don`t need  '-> DT'
    return lambda x, y: x + y


def task_5_append_str_to_list_and_return(input_data: List, elem: str):
    lst = [i for i in input_data]
    lst.append(elem)
    return lst


def task_6_insert_function_result_into_string(func: Callable):
    return f'start {func()} finish'


def task_7_insert_2_vars_into_string(age: float, habit: str):
    age = int(age * 10) / 10
    if len(habit) > 10:
        habit = habit[0:10]
    return f"I have {age} years and I love {habit:10}"

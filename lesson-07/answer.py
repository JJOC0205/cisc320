from dataclasses import dataclass
@dataclass
class Student:
    lowest_page: str
    latest_page: str
    tot_score: int
    num_subs: int  
def mutate_student(student_string,student):
    as_list = student_string.split(" ")
    if as_list[1].upper() == 'P':
        if int(student.lowest_page) > int(as_list[2]) or int(student.lowest_page == 0):
            student.lowest_page = as_list[2]
        student.latest_page = as_list[2]
    elif as_list[1] == 'S':
        student.num_subs += 1
        student.tot_score += int(as_list[2])
    

def calc_logs(lines: list[str]):
    logs = {}
    for i in range(1, (int(lines[0]))+1):
        new_arr = lines[i].split(" ")
        new_key = new_arr[0]
        if new_key not in logs:
            logs[new_key] = Student(0,0,0,0)
        mutate_student(lines[i], logs[new_key])
            
    logs = sorted(logs.items(), key= lambda item: int(item[1].latest_page))
    logs = dict(logs)
#    as_list = []
    for keys, value in logs.items():
        consts = str((str(keys) + " " + str(value.lowest_page) + " " + str(value.latest_page) + " "))
        if value.num_subs and value.lowest_page and value.latest_page:
            to_print = consts + str(((value.tot_score) // value.num_subs))
            print(to_print)
#            as_list.append(to_print)
#    return as_list
            
if __name__=="__main__":
    filename = input()

    with open(filename) as data_file:
        lines:list[str] = data_file.readlines()

    calc_logs(lines)
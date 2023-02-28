from dataclasses import dataclass
@dataclass
class Student:
    lowest_page: str
    latest_page: str
    tot_score: int
    num_subs: int  
def mutate_student(student_string,student):
    as_list = student_string.split(" ")
    if as_list[1].upper == 'P':
        if int(student.lowest_page) > int(as_list[2]) or int(student.lowest_page == 0):
            student.lowest_page = as_list[2]
        student.latest_page = as_list[2]
    elif as_list[1] == 'S':
        student.num_subs += 1
        student.tot_score += int(as_list[2])
    

def calc_logs(lines: list[str]):
    logs = {}
    for i in range(1, int(lines[0])):
        newarr = lines[i].split(" ")
        newkey = newarr[0]
        if newkey not in logs:
            logs[newkey] = Student(0,0,0,0)
        mutate_student(lines[i], logs[newkey])
            
    logs = sorted(logs.items(), key= lambda item: int(item[1].latest_page))
    logs = dict(logs)
    for keys, value in logs.items():
        consts = (str(keys) + " " + str(logs[keys].lowest_page) + " " + str(logs[keys].latest_page) + " ")
        if logs[keys].num_subs and logs[keys].latest_page and logs[keys].lowest_page:
            print(consts + str(((logs[keys].tot_score) // logs[keys].num_subs)))

            
if __name__=="__main__":
    filename = input()

    with open(filename) as data_file:
        lines:list[str] = data_file.readlines()

    calc_logs(lines)
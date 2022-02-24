import os

path_files = {
    "a": os.path.join("inputs", "a_an_example.in.txt"),
    "b": os.path.join("inputs", "b_better_start_small.in.txt"),
    "c": os.path.join("inputs", "c_collaboration.in.txt"),
    "d": os.path.join("inputs", "d_dense_schedule.in.txt"),
    "e": os.path.join("inputs", "e_exceptional_skills.in.txt"),
    "f": os.path.join("inputs", "f_find_great_mentors.in.txt"),
}

def read_file(file_path):
    with open(file_path) as file:
        content = file.read()
    return content

def separate_first_line(content):
    # find the index of the first '\n'
    index = content.find('\n')
    first_line = content[:index]
    content = content[index+1:]
    return first_line, content

def split_first_line(line):
    c,p = map(lambda x:int(x),line.split(' '))
    return c,p

def read_contributors(content, C):
    
    pass

def read_projects(content, P):
    pass

def line_content(line):
    #???? why?
    values = line.split(' ')
    first_value = int(values[0])
    line = values[1:] 
    return first_value, line



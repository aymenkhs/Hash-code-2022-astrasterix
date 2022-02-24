import os

outputs_files = ['a', 'b', 'c', 'd', 'e', 'f']

def write_file(outputs_file, to_do_projects):
    file_path = os.path.join("outputs", outputs_file)
    string = ""
    string += str(len(to_do_projects))
    string += "\n"
    for project in to_do_projects:
        string += project.name
        string += "\n"
        for role in project.roles:
            string += project.asigned_to[role].name
            string += " "
        string = string[:-1]
        string += "\n"
    string = string[:-1]        

    with open(file_path, "w") as file:
        file.write(string)

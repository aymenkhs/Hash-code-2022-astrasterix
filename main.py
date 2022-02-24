import argparse
import pdb

import input
import output

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="""name of file can be 'a' or 'b' or 'c' or 'd' or 'e'""")
    return parser.parse_args()

class Colaborateur:#N collaborators(Contributors)


    def __init__(self, name, skills):
        self.name = name
        #skills: {skill_name:level}   
        self.skills = skills
        #self.projects
        self.assigned = False
        # if the assigned is true maybe add the project name
        # to see in which proj he's working
        self.project_name = "" 


class Projet:#M projects

    def __init__(self, name, days, score, best_before, roles, level_roles):
        self.name = name
        #days aka duration
        self.days = days
        self.score = score
        self.best_before = best_before
        # {role:min_level}
        # role c'est la techno!!
        self.roles = roles

        # assigned_to {role:, role2{}}
        self.asigned_to = {}
        self.level_roles = level_roles
        
        self.list_skills_requirement = [] 
    
    def can_fill_role(self, colaborator):
        pass
        # check si collab a minimumu skills

    def exist_mentor(self, colaborator, role):
        """check if a mentor exists for a  collaborator."""
        pass
        # parcourir list des gens faisant partie du projet
        # check  si parmi eux il y'a quelqu'un qui 
        # a le role demandé au niveau minimum 
        # dans ce cas le colaborateur peut etre assigne avec 
        # mentor

def main():
    args = parse_arguments()
    if args.file not in ('a','b','c','d','e','f'):
        raise ValueError("argument file (-f) must be equal to 'a' or 'b' or 'c' or 'd' or 'e'")
    
    # rest of the code

    # read file
    content = input.read_file(input.path_files[args.file])

    # separate the first line
    first_line, content = input.separate_first_line(content)

    # get the content from the first line
    C, P = input.split_first_line(first_line)

    lines = content.split("\n")

    # get contribs
    contributors = []
    
    i = 0
    for _ in range(C):
        name, nb_skils = lines[i].split(' ')
        nb_skils = int(nb_skils)
        i+=1
        skills = {}
        for _ in range(nb_skils):
            skill, level = lines[i].split(' ')
            i+=1
            skills[skill] = int(level)
        contributors.append(Colaborateur(name, skills))

    projects = []
    # get projects
    for _ in range(P):
        name, D, S, B, R = lines[i].split(' ')
        # R,D,S,B = map(lambda x:int(x),[R,D,S,B])
        R = int(R)
        D = int(D)
        S = int(S)
        B = int(B)
        i+=1
        roles = []
        roles_level = {}
        for _ in range(R):
            role, level = lines[i].split(' ')
            i+=1
            roles.append(role)
            roles_level[role] = int(level)
        projects.append(Projet(name, D, S, B, roles, roles_level ))


    import pdb; pdb.set_trace()
    # represent data

    # solution
    to_do_projects = solution1()

    # output
    output.write_file(args.file, to_do_projects)

    # i do prefer using a bunch of other functions and call them from here, 
    # that way we will manage the "cas par cas" thing that you talked about

def solution1(projects, collaborateurs):
    """Solution for the input 1."""
    # nous voullons parcourir chaque projet
    # et check si on a les candidats nécessaire 
    # pour qu'on puisse demarrer le truc

    to_do_projects = []

    for project in projects:
        
        project_roles = {}
        project_doable = True

        for role in project.roles:
            found = False

            for collaborateur in collaborateurs:
                # collaborateur can't work on more then 1 (role)tech on a project
                if not collaborateur.assign and role in collaborateur.skills:
                    if collaborateur.skills[role] >= project.level_roles[role]:
                        found = True
                        collaborateur.assign = True
                        break

            if found:
                project_roles[role] = collaborateur
            else:
                
                # this means that the project can't be asigned
                project_doable = False
                break
                # ignore project
                for asigned_role in project_roles:
                    project_roles[asigned_role].assign = False
                    

        if project_doable:
            #ajouterasigned_toe des doua
            project.asignde_to = project_roles
            to_do_projects.append(project)
    
    return to_do_projects
        


                


def solution2():
    """Solution for the input 1."""
    pass



if __name__ == '__main__':
    main()
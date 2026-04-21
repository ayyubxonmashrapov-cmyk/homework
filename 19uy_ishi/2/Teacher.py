class Teacher:
    def __init__(self, name: str, science: str):
        self.name = name
        self.science = science  
        self.groups = []

    def add_teacher_group(self, group: str):
        self.groups.append(group)


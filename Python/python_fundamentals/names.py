students = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def student_list():
    for i in range(len(students)):
        print students[i]["first_name"], students[i]["last_name"]

student_list()

users = {
    'Students': [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': "Michael", 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': "Puryear"}
    ]
}



def list():
    for key in users.keys():
        print key
        for i in range(len(users[key])):
            print i+1, "-", users[key][i]["first_name"].upper(), users[key][i]["last_name"].upper(), "-", ((len(users[key][i]["first_name"])) + (len(users[key][i]["last_name"])))

list()

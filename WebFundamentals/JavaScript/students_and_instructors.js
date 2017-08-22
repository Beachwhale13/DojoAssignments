var students = [
  {first_name: "Michael", last_name: "Jordan"},
  {first_name: "John", last_name: "Rosales"},
  {first_name: "Mark", last_name: "Guillen"},
  {first_name: "KB", last_name: "Tonel"}
]

for (var i = 0; i < students.length; i++){
  console.log(students[i]["first_name"], students[i]["last_name"]);
}


//optional

var users = {
  "Students": [
    {first_name: "Michael", last_name: "Jordan"},
    {first_name: "John", last_name: "Rosales"},
    {first_name: "Mark", last_name: "Guillen"},
    {first_name: "KB", last_name: "Tonel"}
  ],
  "Instructors": [
    {first_name: "Michael", last_name: "Choi"},
    {first_name: "Martin", last_name: "Puryear"}
  ]
}

for (var types in users){
  console.log (types);
  for (var i = 0; i < users[types].length; i++){
    console.log(users[types][i]["first_name"], users[types][i]["last_name"], "-", ((users[types][i]["first_name"].length) + (users[types][i]["last_name"].length)));
  }
}

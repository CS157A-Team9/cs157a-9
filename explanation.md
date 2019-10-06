# Explanation for each entity set and relationship

### Department
Department's primary key is `code` and has an attribute name

### Course
Course's primary key is `number` and has attributes name, description and prereq. It belongs to `Department`.

### User
User's primary key is `id` and has attributes of a normal user. For example, name, email, password, and access control.

### Student
Student is a `User` and has attributes major, minor, and GPA.

### Course History
Course history has aggregation relationship with `Student` and has attributes grade, semester, and year.

### Professor
Professor is a `User` and has attributes bio, contact info, and office hours

### Section
Section's primary key is `id` and has attributes status, semester, and time. It is instructed by `Professor` and is located in `Room`.

### Room 
Room's primary key is `number` and it has attribute capacity. It belongs to `Building`.

### Building
Building's primary key is `code` and it has attribute name.

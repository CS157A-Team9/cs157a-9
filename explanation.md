# Explanation for each entity set and relationship

### Department
Department's primary key is `code`(CS, ENG, MATH, etc.) and has an attribute name. 

### Course
Course's primary key is `number` and has attributes name, description. It belongs to `Department`. Also, a particular course might have other prerequisite courses. Therefore, there is a prereq table dedicate to this purpose. To identify a course, we need to use the department code and the course number as Course is a weak entity. Each course belongs to one specific department.

### User
User's primary key is `id` and has attributes of a normal user. For example, name, email, password, and access control.

### Student
Student is a `User` and has unique attributes major, minor, and GPA. Student can enroll in many courses and receive a grade for the class. 

### Course History
Course history has aggregation relationship with `Student` and has attributes grade, semester, and year. Each course history only belongs to one Student entity.

### Professor
Professor is a `User` and has unique attributes bio, contact info, and office hours. 

### Section
A college course often times has many sections. Section is a child of Course. Section's primary key is `id` and has attributes status, semester, and time. It is instructed by `Professor` and is located in `Room`.

### Room 
Room's primary key is `number` and it has attribute capacity. It belongs to `Building` and therefore is a weak entity. We need to combine the building code and the room number in order to identify a specific room. 

### Building
Building's primary key is `code` and it has attribute name.

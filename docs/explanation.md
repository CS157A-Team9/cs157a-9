# Explanation for each entity set and relationship

### Building
Building's primary key is `code` and it has attribute name.

### Course
Course's primary key is `number` and has attributes name, description and units. It belongs to `Department`. Also, a particular course might have other prerequisite courses. Therefore, there is a prereq table dedicated to this purpose. To identify a course, we need to use the department code and the course number as Course is a weak entity. Each course belongs to one specific department.

### Department
Department's primary key is `code`(CS, ENG, MATH, etc.) and has an attribute name.

### Enrollment
Enrollment is a relationship between `Student` and `Section`. It has attributes credits, grade and status.

### Professor
Professor is a `User` and has unique attributes bio, contact info, and office hours. Each professor belongs to exactly one `Department`.

### Room 
Room's primary key is `number` and it has attribute capacity. It belongs to `Building` and therefore is a weak entity. We need to combine the building code and the room number in order to identify a specific room.

### Section
A college course often times has many sections. Section is a child of `Course`. Section's primary key is `id` and has attributes number, status, semester, schedule, start_date, end_date, start_time, end_time. It is instructed by `Professor` and is located in `Room`.

### Student
Student is a `User` and has unique attributes major_1, major_2, minor, and GPA. Students can enroll in many courses and receive a grade for the class.

### User
User's primary key is `id` and has attributes of a normal user. For example, name, email, password, and access control.

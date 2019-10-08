# Schema
## Entity
USER( id, password, email, last_name, first_name, is_staff, is_superuser, is_active, username, last_login, date_joined)

STUDENT(major_1, major_2, minor, GPA)

COURSE_HISTORY(semester, year, grade)

PROFESSOR(bio, contact_info, office_hours)

DEPARTMENT(code, name)

COURSE(number, name, description)

SECTION(id, status, time, semester)

BUILDING(code, name)

ROOM(number, capacity)

## Relationship
has(STUDENT, STUDENT, COURSE_HISTORY)

enrolls(STUDENT, COURSE, grade)

instructs(PROFESSOR, SECTION)

in(PROFESSOR, DEPARTMENT)

classBelong(DEPARTMENT, DEPARTMENT, COURSE)

locates(SECTION, ROOM, BUILDING)

roomBelong(BUILDING, BUILDING, ROOM)

prereq(DEPARTMENT, COURSE, DEPARTMENT, COURSE)

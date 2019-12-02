# Schema

## Entity

BUILDING(code, name)

COURSE(number, name, description, units)

DEPARTMENT(code, name)

PROFESSOR(bio, contact_info, office_hours)

ROOM(number, capacity)

SECTION(id, status, semester, schedule, start_date, end_date, start_time, end_time)

STUDENT(major_1, major_2, minor, GPA)

USER(id, password, email, last_name, first_name, is_staff, is_superuser, is_active, username, last_login, date_joined)

## Relationship

enrolls(STUDENT, SECTION, grade, credits, status)

instructs(PROFESSOR, SECTION)

in(PROFESSOR, DEPARTMENT)

classBelong(DEPARTMENT, DEPARTMENT, COURSE)

locates(SECTION, ROOM, BUILDING)

roomBelong(BUILDING, BUILDING, ROOM)

prereq(DEPARTMENT, COURSE, DEPARTMENT, COURSE)

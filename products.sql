CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT,
    department TEXT,
    credits INTEGER
);

INSERT INTO courses (course_id, course_name, department, credits) VALUES
(101, 'Matematika', 'Science', 3),
(102, 'Fizika', 'Science', 4),
(103, 'Tarix', 'Humanities', 2),
(104, 'Dasturlash', 'Computer Science', 5),
(105, 'Ingliz tili', 'Languages', 3);

select * from courses

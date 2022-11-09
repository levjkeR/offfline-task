CREATE TABLE students (
  id INTEGER PRIMARY KEY,
  student_name VARCHAR(255) Not NULL
) ;

CREATE TABLE visiting_date (
  student_id INTEGER Not NULL,
  visiting_date Datetime Not NULL
) ;

INSERT INTO students
VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Eve'),
(4, 'Diffie');

INSERT INTO visiting_date
VALUES
('1','2022-01-13'),
('2','2022-01-13'),
('1','2022-01-15'),
('3','2022-01-15'),
('4','2022-01-15'),
('1','2022-02-01'),
('3','2022-02-01'),
('4','2022-02-01'),
('3','2022-02-10'),
('4','2022-02-10'),
('1','2022-02-11'),
('2','2022-02-11'),
('3','2022-02-11'),
('1','2022-02-12'),
('2','2022-02-14'),
('3','2022-02-15'),
('1','2022-03-25'),
('2','2022-03-25'),
('3','2022-03-25');

SELECT a.student_name, feb_count FROM students as a,
(SELECT student_id, COUNT() as feb_count FROM visiting_date
WHERE strftime('%m', visiting_date) == '02'
GROUP BY student_id) as b
WHERE a.id=b.student_id and b.feb_count > 2
ORDER BY feb_count DESC

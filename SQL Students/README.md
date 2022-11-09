# SQL Students
____
### Задание
 Как решите задачку: у вас есть 2 таблицы - студенты с id и именем и график посещения ими определенных занятий.  
 Необходимо вывести имена и количество посещений для тех студентов, которые посетили занятия в феврале как минимум 3 раза, отсортировав их по убыванию.  
 Время решения: *~5-7* минут
____
### Решение

```sql
SELECT a.student_name, feb_count FROM students as a,
(SELECT student_id, COUNT() as feb_count FROM visiting_date
WHERE strftime('%m', visiting_date) == '02'
GROUP BY student_id) as b
WHERE a.id=b.student_id and b.feb_count > 2
ORDER BY feb_count DESC
```
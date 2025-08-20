-- 📄 Примеры команд SQL (подсказки):
-- ===========================
-- Как создать таблицу:
-- CREATE TABLE table_name (
--     column1 datatype,
--     column2 datatype,
--     ...
-- );

-- Как вставить данные:
-- INSERT INTO table_name (column1, column2) VALUES ('value1', 'value2');

-- Как обновить данные:
-- UPDATE table_name SET column1 = 'new_value' WHERE some_condition;

-- Как добавить новый столбец:
-- ALTER TABLE table_name ADD COLUMN column_name datatype;

-- Как удалить таблицу:
-- DROP TABLE table_name;

-- ===========================
-- 📋 Задания (выполняйте TODO):
-- ===========================


-- ✅ TODO 1: Создайте таблицу "Employees" с полями:
-- Name (TEXT), Position (TEXT), Department (TEXT), Salary (NUMERIC)

-- 📝 Напишите здесь CREATE TABLE
-- Пример:
-- CREATE TABLE Employees (
--     ...
-- );

CREATE TABLE Employees (
    Name VARCHAR(100),
    Position VARCHAR(100),
    Department VARCHAR(100),
    Salary DECIMAL(10, 2)
);

-- ✅ TODO 2: Вставьте несколько записей в таблицу "Employees"

-- 📝 Напишите здесь INSERT INTO
-- Пример:
-- INSERT INTO Employees (...) VALUES (...), (...), (...);
INSERT INTO Employees (Name, Position, Department, Salary)
VALUES
    ('Иван Петров', 'Developer', 'IT', 4500.00),
    ('Анна Сидорова', 'Manager', 'Sales', 5500.00),
    ('Сергей Иванов', 'Analyst', 'Finance', 4800.00),
    ('Елена Кузнецова', 'Manager', 'HR', 5200.00),
    ('Дмитрий Смирнов', 'Developer', 'IT', 4700.00);

-- ✅ TODO 3: Измените должность одного из сотрудников на более высокую

-- 📝 Напишите здесь UPDATE
-- Пример:
-- UPDATE Employees SET ... WHERE ...;
UPDATE Employees
SET Position = 'Senior Developer', Salary = 5200.00
WHERE Name = 'Иван Петров';

-- ✅ TODO 4: Добавьте новое поле "HireDate" (DATE) в таблицу "Employees"

-- 📝 Напишите здесь ALTER TABLE
-- Пример:
-- ALTER TABLE Employees ADD COLUMN ...;
ALTER TABLE Employees
ADD HireDate DATE;

-- ✅ TODO 5: Добавьте дату приема на работу для всех сотрудников

-- 📝 Напишите здесь UPDATE для каждого сотрудника
-- Пример:
-- UPDATE Employees SET HireDate = '...' WHERE Name = '...';
UPDATE Employees
SET HireDate = '01.01.2020'
WHERE Name = 'Иван Петров';

UPDATE Employees
SET HireDate = '20.11.2019'
WHERE Name = 'Анна Сидорова';

UPDATE Employees
SET HireDate = '01.08.1998'
WHERE Name = 'Сергей Иванов';

UPDATE Employees
SET HireDate = '31.08.2021'
WHERE Name = 'Елена Кузнецова';

UPDATE Employees
SET HireDate = '28.02.2020'
WHERE Name = 'Дмитрий Смирнов';

-- ✅ TODO 6: Найдите всех сотрудников с должностью "Manager"

-- 📝 Напишите здесь SELECT
-- Пример:
-- SELECT * FROM Employees WHERE ...;
SELECT * FROM Employees
WHERE Position = 'Manager';

-- ✅ TODO 7: Найдите всех сотрудников с зарплатой больше 5000

-- 📝 Напишите здесь SELECT
-- Пример:
-- SELECT * FROM Employees WHERE ...;
SELECT * FROM Employees
WHERE Salary > 5000;

-- ✅ TODO 8: Найдите всех сотрудников, которые работают в отделе "Sales"

-- 📝 Напишите здесь SELECT
-- Пример:
-- SELECT * FROM Employees WHERE ...;
SELECT * FROM Employees
WHERE Department = 'Sales';
-- ✅ TODO 9: Найдите среднюю зарплату всех сотрудников

-- 📝 Напишите здесь SELECT AVG(...)
-- Пример:
-- SELECT AVG(...) FROM Employees;
SELECT AVG(Salary) AS AverageSalary
FROM Employees;

-- ✅ TODO 10: Удалите таблицу "Employees"

-- ⚠️ ВНИМАНИЕ: Эта команда удалит таблицу и все данные!
-- Выполняйте её только после того, как закончите все задания выше.

-- 📝 Напишите здесь DROP TABLE
-- Пример:
-- DROP TABLE Employees;
DROP TABLE Employees;

-- 🎯 *Задание с повышенным уровнем сложности:*
-- Реализуйте задачи 6–9 в виде ХРАНИМЫХ ФУНКЦИЙ или ПРОЦЕДУР.

-- Подсказка:
-- CREATE FUNCTION или CREATE PROCEDURE
-- BEGIN ... END

-- Пример вызова:
-- CALL имя_процедуры();

-- 📝 Напишите здесь свои CREATE FUNCTION / PROCEDURE
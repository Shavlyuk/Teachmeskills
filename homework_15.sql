-- 📘 TeachMeSkills: Домашнее задание по SQL
-- Тема: Создание таблиц, связи и JOIN
--
-- 📌 Примеры:
-- Создать таблицу:
-- CREATE TABLE example (
--     id INT PRIMARY KEY,
--     name VARCHAR(255)
-- );
--
-- Вставить данные
-- INSERT INTo example (id, name) VALUES (1, 'Пример')
--
-- Пример INNER JOIN:
-- SELECT a.id, b.name FROM table_a a
-- INNER JOIN table_b b ON a.id = b.a_id;
--
-- Пример агрегатной функции:
-- SELECT author_id, SUM(quantity) FROM sales
-- JOIN books ON sales.book_id = books.id
-- GROUP BY author_id;
--
-- 💡 Вопросы для самоконтроля:
-- 1. Чем отличается INNER JOIN от LEFT JOIN?
-- 2. Почему внешний ключ важен для целостности данных?
-- 3. Для чего нужен GROUP BY?

-- 📋 Задача 1: Создание и заполнение таблиц
-- TODO: Создайте таблицу authors с полями id, first_name, last_name
--       (используйте PRIMARY KEY для поля id)

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL
);

-- TODO: Создайте таблицу books с полями id, title, author_id, publication_year
--       (PRIMARY KEY — id, FOREIGN KEY — author_id, ссылается на authors)

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INTEGER NOT NULL,
    publication_year INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE CASCADE
);

-- TODO: Создайте таблицу sales с полями id, book_id, quantity
--       (PRIMARY KEY — id, FOREIGN KEY — book_id, ссылается на books)

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    book_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    sale_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);

-- TODO: Добавьте нескольких авторов в таблицу authors
--       (INSERT INTO authors ...)

INSERT INTO authors (first_name, last_name) VALUES
('Лев', 'Толстой'),
('Фёдор', 'Достоевский'),
('Антон', 'Чехов'),
('Александр', 'Пушкин'),
('Михаил', 'Булгаков');

-- TODO: Добавьте несколько книг в таблицу books, указывая авторов из authors

INSERT INTO books (title, author_id, publication_year) VALUES
('Война и мир', 1, 1869),
('Анна Каренина', 1, 1877),
('Преступление и наказание', 2, 1866),
('Братья Карамазовы', 2, 1880),
('Вишнёвый сад', 3, 1904),
('Евгений Онегин', 4, 1833),
('Мастер и Маргарита', 5, 1967),
('Собачье сердце', 5, 1925);
('Книга, чей автор неизвестен', NULL, 2025)

-- TODO: Добавьте записи о продажах книг в таблицу sales

INSERT INTO sales (book_id, quantity, sale_date) VALUES
(1, 5, '2025-01-15'),
(1, 3, '2025-01-20'),
(2, 4, '2025-01-18'),
(3, 6, '2025-01-22'),
(4, 2, '2025-01-25'),
(5, 7, '2025-01-19'),


-- 📋 Задача 2: Использование JOIN
-- TODO: Используйте INNER JOIN, чтобы получить список всех книг и их авторов
-- 💡 Пример:
-- SELECT books.title, authors.first_name, authors.last_name
-- FROM books
-- INNER JOIN authors ON books.author_id = authors.id;

SELECT
    b.id,
    b.title,
    a.first_name,
    a.last_name,
    b.publication_year
FROM books b
INNER JOIN authors a ON b.author_id = a.id
ORDER BY b.title;

-- TODO: Используйте LEFT JOIN, чтобы получить список всех авторов и их книг
--       (включая авторов без книг)
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, books.title
-- FROM authors
-- LEFT JOIN books ON books.author_id = authors.id;

SELECT
    a.id AS "ID автора",
    a.first_name || ' ' || a.last_name AS "Автор",
    b.id AS "ID книги",
    b.title AS "Название книги",
    b.publication_year AS "Год издания"
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
ORDER BY a.last_name, a.first_name, b.publication_year;

-- TODO: Используйте RIGHT JOIN, чтобы получить список всех книг и их авторов
--       (включая книги без автора)
-- 💡 Пример:
-- SELECT books.title, authors.first_name, authors.last_name
-- FROM books
-- RIGHT JOIN authors ON books.author_id = authors.id;

SELECT
    b.id AS "ID книги",
    b.title AS "Название книги",
    b.publication_year AS "Год издания",
    a.id AS "ID автора",
    a.first_name || ' ' || a.last_name AS "Автор"
FROM authors a
RIGHT JOIN books b ON a.id = b.author_id
ORDER BY b.title;

-- 📋 Задача 3: Множественные JOIN
-- TODO: Используйте INNER JOIN, чтобы связать authors, books и sales и получить
--       список всех книг, их авторов и продаж
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, books.title, sales.quantity
-- FROM sales
-- INNER JOIN books ON sales.book_id = books.id
-- INNER JOIN authors ON books.author_id = authors.id;

SELECT
    a.first_name || ' ' || a.last_name AS "Автор",
    b.title AS "Название книги",
    b.publication_year AS "Год издания",
    s.quantity AS "Количество продаж",
    s.sale_date AS "Дата продажи",
    s.id AS "ID продажи"
FROM authors a
INNER JOIN books b ON a.id = b.author_id
INNER JOIN sales s ON b.id = s.book_id
ORDER BY a.last_name, a.first_name, b.title, s.sale_date;

-- TODO: Используйте LEFT JOIN, чтобы связать authors, books и sales и получить
--       список всех авторов, их книг и продаж (включая авторов без книг и книги без продаж)
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, books.title, sales.quantity
-- FROM authors
-- LEFT JOIN books ON books.author_id = authors.id
-- LEFT JOIN sales ON sales.book_id = books.id;

SELECT
    a.id AS "ID автора",
    a.first_name || ' ' || a.last_name AS "Автор",
    b.id AS "ID книги",
    b.title AS "Название книги",
    b.publication_year AS "Год издания",
    s.id AS "ID продажи",
    s.quantity AS "Количество продаж",
    s.sale_date AS "Дата продажи"
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
LEFT JOIN sales s ON b.id = s.book_id

-- 📋 Задача 4: Агрегация данных с использованием JOIN
-- TODO: Используйте INNER JOIN и агрегатные функции, чтобы определить общее
--       количество проданных книг каждого автора
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sales
-- FROM sales
-- INNER JOIN books ON sales.book_id = books.id
-- INNER JOIN authors ON books.author_id = authors.id
-- GROUP BY authors.id;

SELECT
    a.id AS "ID автора",
    a.first_name || ' ' || a.last_name AS "Автор",
    COUNT(DISTINCT b.id) AS "Количество книг",
    COUNT(s.id) AS "Количество транзакций продаж",
    SUM(s.quantity) AS "Общее количество проданных книг",
    ROUND(AVG(s.quantity), 2) AS "Среднее количество за продажу",
    MAX(s.sale_date) AS "Последняя продажа"
FROM authors a
INNER JOIN books b ON a.id = b.author_id
INNER JOIN sales s ON b.id = s.book_id
GROUP BY a.id, a.first_name, a.last_name


-- TODO: Используйте LEFT JOIN и агрегатные функции, чтобы определить общее
--       количество проданных книг каждого автора, включая авторов без продаж
-- 💡 Пример:
-- SELECT authors.first_name, authors.last_name, COALESCE(SUM(sales.quantity),0) AS total_sales
-- FROM authors
-- LEFT JOIN books ON books.author_id = authors.id
-- LEFT JOIN sales ON sales.book_id = books.id
-- GROUP BY authors.id;

SELECT
    a.id AS "ID автора",
    a.first_name || ' ' || a.last_name AS "Автор",
    COUNT(DISTINCT b.id) AS "Количество книг",
    COUNT(s.id) AS "Количество транзакций продаж",
    COALESCE(SUM(s.quantity), 0) AS "Общее количество проданных книг",
    COALESCE(ROUND(AVG(s.quantity), 2), 0) AS "Среднее количество за продажу",
    MAX(s.sale_date) AS "Последняя продажа",
    CASE
        WHEN COUNT(s.id) = 0 THEN 'Нет продаж'
        WHEN COUNT(s.id) <= 2 THEN 'Мало продаж'
        ELSE 'Активные продажи'
    END AS "Статус продаж"
FROM authors a
LEFT JOIN books b ON a.id = b.author_id
LEFT JOIN sales s ON b.id = s.book_id
GROUP BY a.id, a.first_name, a.last_name
ORDER BY COALESCE(SUM(s.quantity), 0) DESC, a.last_name;

-- 🚀 Удачи! Не бойтесь пробовать разные JOIN и GROUP BY, чтобы лучше понять, как они работают!
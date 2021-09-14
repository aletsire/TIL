-- 주석
/* 여러불 주석
    기본 문법(변하지 않는 것은 대문자로)
    변하는 부분은 소문자

 */


-- 데이터 전체 조회 SELECT
select * from examples;

-- 테이블 생성
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

CREATE TABLE countries (
room_num TEXT,
check_in TEXT,
check_out TEXT,
grade TEXT,
price INTEGER
);

INSERT INTO countries VALUES
('B203', '2019-12-31', '2020-01-03', 'suite', 900),
('1102', '2020-01-04', '2020-01-08', 'suite',850),
('303', '2020-01-01', '2020-01-03', 'deluxe', 500),
('807', '2020-01-04', '2020-01-07', 'superior', 300);

ALTER TABLE countries RENAME TO hotels;

SELECT room_num, price FROM hotels ORDER BY price DESC LIMIT 2;

SELECT grade, COUNT(*) FROM hotels  GROUP by grade ORDER BY COUNT(*) DESC;

select * from hotels where room_num LIKE 'B%' OR grade='deluxe';

SELECT * FROM hotels WHERE check_in='2020-01-04' AND NOT room_num LIKE 'b%' ORDER BY price;

--테이블 삭제
DROP TABLE classmates;

CREATE TABLE classmates (
name TEXT,
age INT,
address TEXT
);

-- 데이터 입력
INSERT INTO classmates (name,age,address) VALUES('홍길동',23,'서울')
INSERT INTO classmates VALUES
('홍길q', 30, '서울'),
('홍길d', 32, '울'),
('홍길w', 31, '서'),
('홍길z', 33, '서울루');

SELECT * FROM classmates;
SELECT rowid, name FROM classmates;
SELECT rowid, name FROM classmates LIMIT 1;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
SELECT rowid, name FROM classmates WHERE address='서울';
SELECT DISTINCT age FROM classmates; -- 중복없이

--primary키 표시
SELECT rowid, * FROM classmates;
--테이블 삭제
DROP TABLE classmates;
--데이터 삭제
DELETE from classmates where rowid=3;


CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

-- 데이터 수정
UPDATE classmates SET
name='홍길덩',
address='제주더'
where rowid=5;

CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

SELECT * FROM users WHERE age>='30';
SELECT first_name FROM users WHERE age>='30';
select age, last_name from users where age >= 30 AND last_name = 'KIM'
-- 주석
/* 여러불 주석
    기본 문법(변하지 않는 것은 대문자로)
    변하는 부분은 소문자

 */


-- 데이터 전체 조회 SELECT
select * from examples;

-- 테이블 생성
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

--테이블 삭제
DROP TABLE classmates;

CREATE TABLE classmates (
name TEXT,
age INT,
address TEXT
);

-- 데이터 입력
INSERT INTO classmates (name,age,adress) VALUES('홍길동',23,'서울')
INSERT INTO classmates VALUES
('홍길q', 30, '서울'),
('홍길d', 32, '울'),
('홍길w', 31, '서'),
('홍길z', 33, '서울루');

SELECT * FROM classmates;
SELECT rowid, name FROM classmates;
SELECT rowid, name FROM classmates LIMIT 1;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
SELECT rowid, name FROM classmates WHERE address='서울';
SELECT DISTINCT age FROM classmates; -- 중복없이

--primary키 표시
SELECT rowid, * FROM classmates;
--테이블 삭제
DROP TABLE classmates;
--데이터 삭제
DELETE from classmates where rowid=3;


CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

-- 데이터 수정
UPDATE classmates SET
name='홍길덩',
address='제주더'
where rowid=5;

CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

SELECT * FROM users WHERE age>='30';
SELECT first_name FROM users WHERE age>='30';
select age, last_name from users where age >= 30 AND last_name = 'KIM'

SELECT COUNT(*) FROM users;
-- 주석
/* 여러불 주석
    기본 문법(변하지 않는 것은 대문자로)
    변하는 부분은 소문자

 */


-- 데이터 전체 조회 SELECT
select * from examples;

-- 테이블 생성
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT
);

--테이블 삭제
DROP TABLE classmates;

CREATE TABLE classmates (
name TEXT,
age INT,
address TEXT
);

-- 데이터 입력
INSERT INTO classmates (name,age,adress) VALUES('홍길동',23,'서울')
INSERT INTO classmates VALUES
('홍길q', 30, '서울'),
('홍길d', 32, '울'),
('홍길w', 31, '서'),
('홍길z', 33, '서울루');

SELECT * FROM classmates;
SELECT rowid, name FROM classmates;
SELECT rowid, name FROM classmates LIMIT 1;
SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
SELECT rowid, name FROM classmates WHERE address='서울';
SELECT DISTINCT age FROM classmates; -- 중복없이

--primary키 표시
SELECT rowid, * FROM classmates;
--테이블 삭제
DROP TABLE classmates;
--데이터 삭제
DELETE from classmates where rowid=3;


CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);

-- 데이터 수정
UPDATE classmates SET
name='홍길덩',
address='제주더'
where rowid=5;

CREATE TABLE users (
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
age INTEGER NOT NULL,
country TEXT NOT NULL,
phone TEXT NOT NULL,
balance INTEGER NOT NULL
);

SELECT * FROM users WHERE age>='30';
SELECT first_name FROM users WHERE age>='30';
select age, last_name from users where age >= 30 AND last_name = '김';
SELECT AVG(age) FROM users WHERE age>=30;
SELECT first_name, MAX(balance) FROM users;
SELECT AVG(balance) FROM users WHERE age>=30;

SELECT * FROM users WHERE age LIKE '2_'; -- 데이터 타입이 INT여도 적용가능
SELECT * FROM users WHERE phone LIKE '02-%';
SELECT * FROM users WHERE first_name LIKE '%준';
SELECT * FROM users WHERE phone LIKE '%5114%';

SELECT * FROM users ORDER BY balance, last_name DESC LIMIT 10;

SELECT last_name, COUNT(*) FROM users GROUP by last_name;
SELECT last_name, COUNT(*) AS name_count FROM users GROUP by last_name;

CREATE TABLE articles (
title TEXT NOT NULL,
content TExt NOT NULL
);

INSERT INTO articles VALUES ('1번제목', '1번내용')

ALTER TABLE articles RENAME TO news;

SELECT * from news;

ALTER TABLE news ADD COLUMN created_at TEXT;
INSERT into news VALUES ('제목', '내용', datetime('now'));

ALTER TABLE news ADD COLUMN subtitle TEXT NOT NULL DEFAULT '임시제목';

create table members(
	member_id  	integer primary KEY,
	first_name	text NOT NULL,
	last_name	text NOT NULL,    
	email 		text NOT NULL
);

create table authors(
	author_id  	integer primary KEY,
    first_name	text NOT NULL,
	last_name	text NOT NULL
);

create table books(
	book_id  	integer primary KEY,
	title	 	text NOT NULL,
    year		integer not null check (year > 0),
	genre 		text NOT NULL
);

create table loans(
	loan_id     integer primary KEY,
	member_id	integer NOT NULL,
	book_id     integer NOT NULL,
    foreign key (member_id) references members(member_id),
	foreign key (book_id) references books(book_id)
);

create table book_authors(
	book_id  	integer NOT NULL,
    author_id  	integer NOT NULL,
    primary key (book_id, author_id),
	foreign key (book_id) references books(book_id),
	foreign key (author_id) references authors(author_id)
);

-- Testing:

INSERT INTO books VALUES
(1, 'Gateway', 1987, 'Sci-Fi'),
(2, 'Beyond the Blue Event', 1997, 'Sci-Fi'),
(3, 'Golden Son', 2007, 'Sci-Fi'),
(4, 'Morning Star', 2008, 'Sci-Fi'),
(5, 'Dark Age', 2009, 'Sci-Fi');

INSERT INTO authors VALUES
(1, 'Frederik', 'Pohl'),
(2, 'Pierce', 'Brown');

INSERT INTO members VALUES
(1, 'Gloria', 'Lex', 'gloria@lexicon.com'),
(2, 'Jacob', 'Lex', 'jacob@lexicon.com'),
(3, 'Max', 'Lex', 'max@lexicon.com');

INSERT INTO book_authors VALUES
(1, 1),
(2, 1),
(3, 2),
(4, 2),
(5, 2);

select * from book_authors;

INSERT into loans VALUES
(1, 1, 5),
(2, 3, 1);

select * from loans;

select member.first_name, book.title, author.first_name, author.last_name, loan.loan_id from loans loan 
join members member on member.member_id = loan.member_id
join books book on book.book_id = loan.book_id
join book_authors bk on bk.book_id = loan.book_id
join authors author on author.author_id = bk.author_id;


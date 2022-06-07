show databases;
create database sistema_pampulha;
use sistema_pampulha;
show tables;
create table santos (
	id integer not null auto_increment primary key,
	nome varchar(60),
	data date	
	);
    
INSERT INTO santos (nome, data)
VALUES ('Nossa Senhora da Defesa',"2022-01-18"),('São Sebastião',"2022-01-20"),
('Santa Inês',"2022-01-21"),('Dom Bosco',"2022-01-31");

select * from santos;
    
create table igrejas (
	id integer not null primary key auto_increment,
    id_santo integer,
    nome varchar(60),
    endereco varchar(250),
    responsavel varchar(60),
    telefone varchar(11)
);

ALTER TABLE igrejas ADD CONSTRAINT fk_igrejas_id_santo FOREIGN KEY ( id_santo ) REFERENCES santos (id);


select * from igrejas;

drop table igrejas;
drop table santos;

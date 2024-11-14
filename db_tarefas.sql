CREATE DATABASE db_tarefas;

USE db_tarefas;

CREATE TABLE tbl_usuarios (
    usu_codigo INT AUTO_INCREMENT PRIMARY KEY,
    usu_name VARCHAR(100) NOT NULL,
    usu_email VARCHAR(100) NOT NULL
);

CREATE TABLE tbl_tarefas (
    tar_codigo INT AUTO_INCREMENT PRIMARY KEY,
    tar_descricao VARCHAR(100) NOT NULL,
    tar_setor VARCHAR(100) NOT NULL,
    tar_prioridade VARCHAR(100) NOT NULL,
    tar_status VARCHAR(100) NOT NULL,
    tar_data DATE,
    usu_codigo INT NOT NULL	
);

ALTER TABLE tbl_tarefas
ADD CONSTRAINT fk_usu_codigo FOREIGN KEY (usu_codigo) REFERENCES tbl_usuarios(usu_codigo);
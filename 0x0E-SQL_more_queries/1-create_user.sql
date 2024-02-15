-- a script that creates the MySQL server user user_0d_1 and have all privileges
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY user_0d_1_pwd;
GRANT ALL PRIVILEGE ON * . * TO user_0d_1@localhost;

# Add User to MySQL DB

Log into db

```
mysql -u root -p
```

Create user 

```
create user '[username]'@'[user ip]' IDENTIFIED BY '[password]';
```

If desired we can create a database,

```
create database [databaseName];
```

and authorize the user to use it

```
GRANT ALL ON [databaseName].* FROM '[username]'@'[user ip]';
```

Implement changes

```
FLUSH PRIVILEGES;
```

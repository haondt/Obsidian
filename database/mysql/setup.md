# MySQL Server Setup

Create a [ubuntu container](../../baremetal/ubuntu.md).

Install mysql and run included security script

```
apt install mysql-server
mysql_secure_installation
```

* Do not set up VALIDATE PASSWORD plugin
* Do not change password for root
* Do remove anonymous users
* Do disallow remote root login
* Do remove test database and access to it
* Do reload privilege tables now

Initialize mysql data directory

```
mysqld --initialize
```

Check service status

```
systemctl status mysql
```

Change data directory by first logging into the db as root

```
mysql -u root -p
```

enter password, then you should be greeted by the sql prompt, `mysql>`. Check the current data directory with

```
select @@datadir;
```

Exit the db

```
exit
```

Stop the service (and optionally double check to ensure it is stopped

```
sudo systemctl stop mysql
sudo systemctl status mysql
```

Copy the directory with `rsync -av`, where the `-a` flag will preserve permissions and other directory properties,
while `-v` will provide verbose output. Be sure not to put a trailing backslash on the directories.
We want rsync to transfer the directory onto the mountpoint, not the contents of the directory.

```
sudo rsync -av /var/lib/mysql /[ssd_raid]
```

You can double check that the move was successful by verifying the contents of the output folder

```
mysql@MySQL:~$ tree /[ssd_raid] -L 2 
/[ssd_raid]
└ mysql
	├ auto.cnf
	├ debian-5.7.flag
	├ ib_buffer_pool
	├ ibdata1
	├ ib_logfile0
	├ ib_logfile1
	├ mysql
	├ performance_schema
	└ sys

4 directories, 6 files
```

Keep the old location as a backup

```
sudo mv /var/lib/mysql /var/lib/mysql.bak
```

Edit the mysql configuration file

```
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
```

Change

```
...
datadir         = /var/lib/mysql
...
```

to your new mount point

```
...
datadir         = /[ssd_raid]/mysql
...
```

Edit the AppArmor control rules to allow MySQL to write to the new directory

```
sudo vim /etc/apparmor.d/tunables/alias
```

Add the following alias rule to the bottom of the file

```
...
alias /var/lib/mysql/ -> /[ssd_raid]/mysql/,
```

Restart apparmor

```
sudo systemctl restart apparmor
```

MySQL looks for a directory or symbolic link that matches two default paths. Create a directory structure to pass this check

```
sudo mkdir /var/lib/mysql/mysql -p
```

Start MySQL and verify the status

```
sudo systemctl start mysql
sudo systemctl status mysql
```

Verify the new data directory

```
mysql -u root -p
select @@datadir;
exit
```

Remove the backup directory

```
sudo rm -Rf /var/lib/mysql.bak
```

Give MySQL one more restart for good measure

```
sudo systemctl start mysql
sudo systemctl status mysql
```

Allow any ip to connect to  the server (can still create ip-based authorization for each user in the db though)

```
sudo vim /etc/mysql/my.cnf
```

The following square brackets do not indicate a value that you should replace.

If the line `[mysqld]` is already in the file, just add the line under there, otherwise add the following to the bottom of the file

```
...
[mysqld]
bind-address = '*'
```

You're done! See [here](./adduser.md) for how to add a user to the database.

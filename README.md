## Python Flask with MySQL

Basic Flask app that lets you store records to MySQL, search from MySQL and also display the number of records on the MySQL Table.

### Setup Dependencies:

```
yum install python-setuptools -y
easy_install pip
```

### Download, Install Requirements:

```bash
pip install -r requirements.txt
```

### MySQL Configuration: 

```
vi application.py
```

Update mysql uri to match your database:
` mysql://user:pass@host.domain.com/mydb `


### Run Application:

```
python application.py
```

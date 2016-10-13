pyldaplite
==========

Simple python-ldap handy wrapper

```python
#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pyldaplite import PyLDAPLite

base_dn = 'DC=CORP,DC=COMPANY,DC=ORG'
server = 'dcserver'
username = 'domain\\username'
password = 'password'

l = PyLDAPLite(server=server, base_dn=base_dn)
# or secure mode
# l = PyLDAPLite(server='ldaps://' + server, base_dn=base_dn)
l.connect(username, password)

# NT account
users = l.search_name('ntname', limit=0)
for user in users:
    print(user[0])

# User Full Name
users = l.search_display('display name', limit=0)
for user in users
    print(user[0])

# Email
users = l.search_email('aaa@example.com', limit=0)
for user in users
    print(user[0])

# Phone
users = l.search_phone('123456789', limit=0)
for user in users
    print(user[0])

# Mobile
users = l.search_mobile('12345678901', limit=0)
for user in users
    print(user[0])

# employee number
users = l.search_number('12345', limit=0)
for user in users
    print(user[0])

# you can search by defined filter
filter_value = 'employeeNumber=12345'
users = l.search_by(filter_value, limit=0)
for user in users:
    print(user[0])

# do not forget to close the connection
l.close()
```


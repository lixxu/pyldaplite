pyldaplite
==========

Simple LDAP package for Python use

```python
from pyldaplite import PyLDAPLite

base_dn = 'DC=CORP,DC=COMPANY,DC=ORG'
server = 'dcserver'
username = 'domain\\username'
password = 'password'

l = PyLDAPLite(server=server, base_dn=base_dn)
l.connect(username, password)
users = l.search_name('ntname')
for user in users:
    print(user[0])

users = l.search_display('display name')
for user in users
    print(user[0])

# you can search by other keyword
filter_value = 'employeeNumber=10000'
users = l.search_by(filter_value)
for user in users:
    print(user[0])

# do not forget to close the connection
l.close()
```


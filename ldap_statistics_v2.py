from ldap3 import Server, Connection, SUBTREE

# LDAP server details
LDAP_SERVER = 'localhost'
LDAP_USER = 'cn=admin,dc=my-domain,dc=com'
LDAP_PASSWORD = 'admin_password'
BASE_DN = 'dc=my-domain,dc=com'

# Connect to the LDAP server
server = Server(LDAP_SERVER)
conn = Connection(server, LDAP_USER, LDAP_PASSWORD, auto_bind=True)

# Define a function to get statistics
def get_statistics(base_dn):
    stats = {'total': 0, 'levels': {}}
    stack = [(base_dn, 1)]

    while stack:
        dn, level = stack.pop()
        conn.search(dn, '(objectClass=*)', SUBTREE, attributes=['ou', 'cn'])
        level_count = len(conn.entries)
        stats['total'] += level_count
        if level not in stats['levels']:
            stats['levels'][level] = 0
        stats['levels'][level] += level_count

        for entry in conn.entries:
            stack.append((entry.entry_dn, level + 1))

    return stats

# Get and print the statistics
statistics = get_statistics(BASE_DN)
print(f"Total objects: {statistics['total']}")
for level, count in statistics['levels'].items():
    print(f"Level {level}: {count} objects")

#!/usr/bin/python3
#!/usr/bin/python3

# INET4031
# Zakaria Abdi
# Script with interactive dry-run capability

import os
import re
import sys

def main():
    dry_run = input("Do you want to run in dry-run mode? (y/n): ").strip().lower()

    for line in sys.stdin:
        match = re.match("^#", line)
        fields = line.strip().split(":")

        if match or len(fields) != 5:
            if dry_run == 'y':
                print("SKIPPED LINE (comment or malformed):", line.strip())
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        print(f"==> Creating account for {username}...")
        cmd = f"/usr/sbin/adduser --disabled-password --gecos '{gecos}' {username}"
        if dry_run == 'y':
            print("DRY RUN:", cmd)
        else:
            os.system(cmd)

        print(f"==> Setting the password for {username}...")
        cmd = f"/bin/echo -ne '{password}\n{password}' | /usr/bin/sudo /usr/bin/passwd {username}"
        if dry_run == 'y':
            print("DRY RUN:", cmd)
        else:
            os.system(cmd)

        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = f"/usr/sbin/adduser {username} {group}"
                if dry_run == 'y':
                    print("DRY RUN:", cmd)
                else:
                    os.system(cmd)

if __name__ == "__main__":
    main()

#!/usr/bin/python3

# INET4031
# Zakaria Abdi
# Date Created: 03/24/2025
import os
import re
import sys

# Main function to process input and create users
def main():
    for line in sys.stdin:
        # Skip lines that begin with a '#' character (treated as comments)
        match = re.match("^#", line)

        # Strip whitespace and split each line by colon into fields
        fields = line.strip().split(':')

        # Skip line if it's commented OR doesn't have exactly 5 fields
        if match or len(fields) != 5:
            continue

        # Extract user details from fields
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])  # Format: First Last,,, (for GECOS field)
        groups = fields[4].split(',')  # Support for multiple groups separated by commas

        # Simulate user creation command
        print("==> Creating account for %s..." % username)
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)
        print("DRY RUN: %s" % cmd)
        # os.system(cmd)

        # Simulate setting the user’s password
        print("==> Setting the password for %s..." % username)
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)
        print("DRY RUN: %s" % cmd)
        # os.system(cmd)

        # If group is not "-", assign the user to specified group(s)
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                print("DRY RUN: %s" % cmd)
                # os.system(cmd)

# Run the script
if __name__ == '__main__':
    main()

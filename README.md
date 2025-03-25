# inet_4031_adduser_script
# INET4031 Add Users Script and User List

## Program Description

This script provides an automated way to add user accounts and assign them to groups on a Linux system. Instead of manually using the `adduser`, `passwd`, and `adduser [user] [group]` commands for each user, this script reads from a predefined input file and runs the same commands automatically.

System administrators normally use commands like:
- `adduser username`
- `passwd username`
- `adduser username groupname`

This script performs those same tasks programmatically using Python and the `os.system()` function. It helps reduce the time and potential for errors that come from creating multiple user accounts manually.

## Program User Operation

This script is designed to run from the command line and reads user information from a separate input file. The script supports both a **dry-run** mode for testing and a **live mode** that actually adds users and groups.

To run the script:
1. Clone the repository to your Ubuntu server.
2. Make sure the script is executable.
3. Prepare the input file.
4. Run the script in either dry-run or live mode.

### Input File Format

The input file should contain one user per line, using the following format:

# Command Execution

To run the script, you must make it executable first:

```bash
chmod +x create-users.py

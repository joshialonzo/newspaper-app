# Linux Users

Create a new Linux user

```bash
# useradd: command
# -m: add a whole folder for this user
# -s /bin/bash: make bash its default shell
# -G sudo: add the user to the group sudo
# john: name of the user
useradd -m -s /bin/bash -G sudo john
```

Change the password of a user

```bash
# passwd: command
# john: user
passwd john
```

See the list of Linux users

```bash
cat /etc/passwd
```
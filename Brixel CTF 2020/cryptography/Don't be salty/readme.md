# Don't be salty

Brixel CTF 2020

>Our l33t hackers hacked a bulletin board and gained access to the database. We need to find the admin password.
>
>The user's database info is:
>
>**Username**:admin
>
>**Passwordhash**:d269ce15f9c44bc3992a5f4e5f273e06
>
>We know from the source code that the salt is put AFTER the password, then hashed. We also know the user likes to use lowercase passwords of only 5 characters long.
>
>The flag is the plaintext password
>
>This flag is not in the usual format, you can enter it with or without the brixelCTF{flag} format

Well I started to do the same thing but with no result. I then knew to start a hashcat brute with the rockyou list. This is the command I used and the format in my hashes.txt.

> Hashes.txt
> ==========
> 2bafea54caf6f8d718be0f234793a9be:04532@#!!
>
> Command
> =======
> .\hashcat.exe -m 10 -a 0 .\hashes.txt .\rockyou.txt

Ignore the fact that I use windows and have wsl, but I do boot into parrot if needed. After launching the brute, I got the flag.

> 2bafea54caf6f8d718be0f234793a9be : 04532@#!! : **brute**
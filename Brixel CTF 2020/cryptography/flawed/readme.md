# flawed

Brixel CTF 2020

>Our l33t hackers hacked a bulletin board and gained access to the database. We need to find the admin password.
>
>The user's database info is:
>
>**Username**:admin
>
>**Passwordhash**:d269ce15f9c44bc3992a5f4e5f273e06
>
>The flag is the plaintext password
>
>This flag is not in the usual format, you can enter it with or without the brixelCTF{flag} format

Well I have dealt with too much md5 hashes to know the length based on sight. Just use any md5 decrypt to get the flag.

> <https://hashes.com/en/tools/hash_identifier>

Inputting the fields we have from the description, I got the flag.

> d269ce15f9c44bc3992a5f4e5f273e06 - **notsecure** - Possible algorithms: MD5
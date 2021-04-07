# android app
Brixel CTF 2020

>This little android app requires a password, can you find it?
>
>the flag is the password

As we have an apk, before we want to emulate it, let's see if we can find the flag in the source code.

We use a program called jadx

> <https://github.com/skylot/jadx>

In appinventor, we can go through the classes and find the flag in Screen1.class

<code><img src="https://zyphen.is-inside.me/ifGzP858.png"></code>


This is the flag.

> brixelCTF{th3_4ndr0ids_y0u_4r3_l00k1ng_f0r}
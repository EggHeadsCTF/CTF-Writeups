# Lost evidence

Brixel CTF 2020

>A buddy of mine is in serious trouble. He works for the feds and accidentally deleted a pendrive containing crucial evidence
>
>Can you get it back and tell us what the evidence is?
>
>
>We need to know what the suspect bought
>
>
>The flag is in this format: brixelCTF{name_of_product_bought}

When you open the archive, you are presented with a .img file. I generally analyze and scour these files with 7zip as to see information packed in somewhat organized files as seen in the image below. 

<code><img src="https://zyphen.is-inside.me/xzYDCk18.png"></code>

>NOTE: As I currently know of, you cannot use Winrar to open img files, I have tried in the past and I will try again but I do not believe so.

I looked through all of these files in a text editor, and there is just nothing to be seen. So its now time to use a tool. I scoured the web for one called DMDE and after their useful tutorial on the app, I was able to import the IMG and get across to two files remaining on this system. Two Audio Files.

<code><img src="https://zyphen.is-inside.me/KtUVvKVb.png"></code>

I proceeded to extract and when I launched, I immediately noted it was a DMTF audio challenge from here on out. I used my favourite site for these kinds of challenges. 

> <http://dialabc.com/sound/detect/index.html>

After going through one audio we got the message and object for the flag. Both of the audios were the exact same, no worries. 

> 212 555 4240  |  546669  | 1609 | 533266 | 5000 | 1 | 8449903336667770844330222666222244466330227778844 | THX FOR THE **COCAINE** BRUH
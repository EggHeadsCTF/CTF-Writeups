# login5

Brixel CTF 2020

>Ok, THIS time it should be fine! if you find this one he is going to quit trying.
>
>http://timesink.be/login4/index.html

Please stop making more. Lets put him to rest. Open up Developer tools and look at the script tag to get our flag.

```html
<script type="text/javascript">
var _0x2c58=['getElementById','Incorrect\x20password','Password\x20Verified','length','substr','the_password','abcdefghijklmnopqrstuvwxyz1234567890!{}'];(function(_0x47871f,_0x1326ab){var _0x2c58be=function(_0x58abc9){while(--_0x58abc9){_0x47871f['push'](_0x47871f['shift']());}};_0x2c58be(++_0x1326ab);}(_0x2c58,0x91));var _0x58ab=function(_0x47871f,_0x1326ab){_0x47871f=_0x47871f-0x192;var _0x2c58be=_0x2c58[_0x47871f];return _0x2c58be;};function verify(){var _0x41653e=_0x58ab;password=document[_0x41653e(0x194)](_0x41653e(0x192))['value'],alphabet=_0x41653e(0x193),newpassword=alphabet[_0x41653e(0x198)](0x1,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0x11,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0x8,0x1),newpassword=newpassword+alphabet['substr'](0x17,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0x4,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0xb,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0x2,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0x13,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0x5,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](alphabet[_0x41653e(0x197)]-0x2,0x1),newpassword=newpassword+alphabet['substr'](alphabet[_0x41653e(0x197)]-0x4,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0x1,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0x5,0x1),newpassword=newpassword+alphabet['substr'](0x14,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0x12,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0x2,0x1),newpassword=newpassword+alphabet['substr'](0x0,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0x13,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0x8,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](alphabet[_0x41653e(0x197)]-0x4,0x1),newpassword=newpassword+alphabet[_0x41653e(0x198)](0xd,0x1),newpassword=newpassword+alphabet['substr'](alphabet[_0x41653e(0x197)]-0x1,0x1),password==newpassword?alert(_0x41653e(0x196)):alert(_0x41653e(0x195));}
</script>
```

Now that is a lot. Its definitely obfuscated so lets just use the console and print out the two variables, password and newpassword. First lets prettify it and get the verify function. 

> <https://beautifier.io/>

```javascript
function verify() {
  var _0x41653e = _0x58ab;
  (password = document[_0x41653e(0x194)](_0x41653e(0x192))["value"]),
    (alphabet = _0x41653e(0x193)),
    (newpassword = alphabet[_0x41653e(0x198)](0x1, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0x11, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0x8, 0x1)),
    (newpassword = newpassword + alphabet["substr"](0x17, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0x4, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0xb, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0x2, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0x13, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0x5, 0x1)),
    (newpassword =
      newpassword +
      alphabet[_0x41653e(0x198)](alphabet[_0x41653e(0x197)] - 0x2, 0x1)),
    (newpassword =
      newpassword + alphabet["substr"](alphabet[_0x41653e(0x197)] - 0x4, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0x1, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0x5, 0x1)),
    (newpassword = newpassword + alphabet["substr"](0x14, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0x12, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0x2, 0x1)),
    (newpassword = newpassword + alphabet["substr"](0x0, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0x13, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0x8, 0x1)),
    (newpassword =
      newpassword +
      alphabet[_0x41653e(0x198)](alphabet[_0x41653e(0x197)] - 0x4, 0x1)),
    (newpassword = newpassword + alphabet[_0x41653e(0x198)](0xd, 0x1)),
    (newpassword =
      newpassword + alphabet["substr"](alphabet[_0x41653e(0x197)] - 0x1, 0x1)),
    password == newpassword ? alert(_0x41653e(0x196)) : alert(_0x41653e(0x195));

console.log(newpassword)
console.log(password)
}
```

Our flag is printed.

> brixelctf{0bfuscati0n}

# Browsercheck

Brixel CTF 2020

>I found this weird website, but it will only allow 'ask jeeves crawler' to enter?
>
>Can you get me in?
>
>http://timesink.be/browsercheck/

At the start we see the following.

> Access denied! Ask Jeeves crawler allowed only!

Searching up online for the askjeeves useragent, we get the following.

> <https://developers.whatismybrowser.com/useragents/parse/716287-ask-jeeves-crawler>
>
> Mozilla/2.0 (compatible; Ask Jeeves/Teoma; +http://sp.ask.com/docs/about/tech_crawling.html)

Put that useragent into the emulated device section of your developer tools and after a refresh, we get the flag.

<code><img src="https://zyphen.is-inside.me/4TWCsZVd.png"></img></code>

This is our flag.

> brixelCTF{askwho?}

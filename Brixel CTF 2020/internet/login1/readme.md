# login1

Brixel CTF 2020

>My buddy is trying to become a web developer, he made this little login page. Can you get the password?
>
>http://timesink.be/login1/index.html

Open up Developer tools and look at the script tag to get our flag.

```html
<script type="text/javascript">
	function verify() {
		password = document.getElementById("the_password").value;
		if(password == "brixelCTF{w0rst_j4v4scr1pt_3v3r!}")
		{
			alert("Password Verified");
		}
		else 
		{
		alert("Incorrect password");
		}
	}
</script>
```

That is our flag.

> brixelCTF{w0rst_j4v4scr1pt_3v3r!}
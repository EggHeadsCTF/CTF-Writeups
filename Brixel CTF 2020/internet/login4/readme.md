# login4

Brixel CTF 2020

>Whow, another one! You're good! So I told my buddy how you managed to get the password last time, and he fixed it. Could you check again please?
>
>http://timesink.be/login4/index.html

Open up Developer tools and look at the script tag to get our flag.

```html
<script type="text/javascript">
	function verify() {
		username = document.getElementById("the_username").value;
		password = document.getElementById("the_password").value;
		if(username == atob(readTextFile("username.txt")))
		{
			if(password == atob(readTextFile("password.txt")))
			{
				alert("Password Verified");
			} else {
				alert("Incorrect password");
			}
		}else{
			alert("Incorrect username");
		}
		
	}
    function readTextFile(filePath) 
    {      
		var result = null;
		var xmlhttp = new XMLHttpRequest();
		xmlhttp.open("GET", filePath, false);
		xmlhttp.send();
		if (xmlhttp.status==200) {
			result = xmlhttp.responseText;
		}
		return result;
    } 
</script>
```

It's the same thing, but this time there is a base64 decode we have to do.

> <http://timesink.be/login4/password.txt>

That is our flag.

> brixelCTF{even_base64_wont_make_you_secure}
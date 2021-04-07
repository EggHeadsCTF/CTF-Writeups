# login3

Brixel CTF 2020

>Nice! you found another one! He changed it up a bit again, could you try again?
>
>http://timesink.be/login3/index.html

Open up Developer tools and look at the script tag to get our flag.

```html
<script type="text/javascript">
	function verify() {
		username = document.getElementById("the_username").value;
		password = document.getElementById("the_password").value;
		if(username == readTextFile("username.txt"))
		{
			if(password == readTextFile("password.txt"))
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

It seems that it is reading a open file on the directory, so lets navigate to password.txt.

> <http://timesink.be/login3/password.txt>

That is our flag.

> brixelCTF{n0t_3v3n_cl05e_t0_s3cur3!}
# login2

Brixel CTF 2020

>Cool, you found the first password! He secured it more, could you try again?
>
>http://timesink.be/login2/index.html

Open up Developer tools and look at the script tag to get our flag.

```html
<script type="text/javascript">
	function verify() {
		password = document.getElementById("the_password").value;
		split = 6;
		if (password.substring(0, split) == 'brixel') 
		{
			if (password.substring(split*6, split*7) == '180790') 
			{
				if (password.substring(split, split*2) == 'CTF{st') 
				{
					if (password.substring(split*4, split*5) == '5cr1pt') 
					{
						if (password.substring(split*3, split*4) == 'd_j4v4') 
						{
							if (password.substring(split*5, split*6) == '_h3r3.') 
							{
								if (password.substring(split*2, split*3) == '1ll_b4') 
								{
									if (password.substring(split*7, split*8) == '54270}') 
									{
										alert("Password Verified")
									}
								}
							}
						}
					}
				}
			}
		}
		else 
		{
		alert("Incorrect password");
		}
	}
</script>
```

It is a bit more difficult but put it in order in terms of splits and that is our flag.

> brixelCTF{std_j4v45cr1pt_h3r3.18079054270}
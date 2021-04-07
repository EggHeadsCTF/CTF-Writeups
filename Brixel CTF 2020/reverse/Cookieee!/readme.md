# Cookieee!
Brixel CTF 2020

>This stupid cookie clicker game...
>
>Legend has it there is a reward when you reach 10000000 or more clicks
>
>Can you think of a way to get that many clicks?

When taking a look at this challenge, its immediately noticible it's a Unity executable. With Unity executables in capture the flag events, it's generally with two options. Assets and or CSharp decompiling. Let's go to CSharp decompiling as its simpler.

We use a program called dnSpy to see the Assembly-CSharp.dll file.

> <https://github.com/dnSpy/dnSpy>

In dnSpy, we could go to the functions list and see two classes.

<code><img src="https://zyphen.is-inside.me/7C0QROKE.png"></code>

Lets take a look at the cookieScript to understand what is happening.

```cs
public class cookieScript : MonoBehaviour
{
	private void Start()
	{
		GameObject.Find("score").GetComponent<Text>().text = this.myScore.ToString();
		this.thisCamera = Camera.main;
	}

	private void Update()
	{
		if (this.myScore >= 10000000)
		{
			SceneManager.LoadScene("scene2");
		}
		if (Input.GetKeyDown("escape"))
		{
			Application.Quit();
		}
	}

	private void OnMouseDown()
	{
		this.myScore++;
		GameObject.Find("score").GetComponent<Text>().text = this.myScore.ToString();
		base.gameObject.transform.position = new Vector3((float)Random.Range(-6, 6), (float)Random.Range(-5, 5));
		base.gameObject.GetComponent<Animator>().Play("cookieani");
	}

	public int myScore;

	public Camera thisCamera;
}
```
> I took out uneeded information

It resets myScore to 0 every launch, as it should, but if looked at the Update method, it seems to load a new scene once the score is past 10000000. I assumed this might be where the endGameScript came in.

```cs
public class endGameScript : MonoBehaviour
{
	private void Start()
	{
		GameObject.Find("endGame").GetComponent<Text>().text = string.Concat(new string[]
		{
			this.alphabet.Substring(28, 1),
			this.alphabet.Substring(14, 1),
			this.alphabet.Substring(13, 1),
			this.alphabet.Substring(6, 1),
			this.alphabet.Substring(17, 1),
			this.alphabet.Substring(0, 1),
			this.alphabet.Substring(19, 1),
			this.alphabet.Substring(20, 1),
			this.alphabet.Substring(11, 1),
			this.alphabet.Substring(0, 1),
			this.alphabet.Substring(19, 1),
			this.alphabet.Substring(8, 1),
			this.alphabet.Substring(14, 1),
			this.alphabet.Substring(13, 1),
			this.alphabet.Substring(18, 1),
			this.alphabet.Substring(67, 1),
			this.alphabet.Substring(62, 1),
			this.alphabet.Substring(31, 1),
			this.alphabet.Substring(11, 1),
			this.alphabet.Substring(0, 1),
			this.alphabet.Substring(6, 1),
			this.alphabet.Substring(62, 1),
			this.alphabet.Substring(63, 1),
			this.alphabet.Substring(62, 1),
			this.alphabet.Substring(1, 1),
			this.alphabet.Substring(17, 1),
			this.alphabet.Substring(8, 1),
			this.alphabet.Substring(23, 1),
			this.alphabet.Substring(4, 1),
			this.alphabet.Substring(11, 1),
			this.alphabet.Substring(28, 1),
			this.alphabet.Substring(45, 1),
			this.alphabet.Substring(31, 1),
			this.alphabet.Substring(65, 1),
			this.alphabet.Substring(12, 1),
			this.alphabet.Substring(55, 1),
			this.alphabet.Substring(12, 1),
			this.alphabet.Substring(52, 1),
			this.alphabet.Substring(17, 1),
			this.alphabet.Substring(24, 1),
			this.alphabet.Substring(66, 1)
		});
	}

	private string alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 =.{}!";
}
```
> I took out a lot more uneeded information

Here we see two main strings, alphabet, and the concatenation string. Now that we have this in mind, lets start to figure out what they said.

```cs
class MainClass {
  public static void Main (string[] args) {
    string alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 =.{}!";
    string test = String.Concat(new string[]
		{
			alphabet.Substring(28, 1),
			alphabet.Substring(14, 1),
			alphabet.Substring(13, 1),
			alphabet.Substring(6, 1),
			alphabet.Substring(17, 1),
			alphabet.Substring(0, 1),
			alphabet.Substring(19, 1),
			alphabet.Substring(20, 1),
			alphabet.Substring(11, 1),
			alphabet.Substring(0, 1),
			alphabet.Substring(19, 1),
			alphabet.Substring(8, 1),
			alphabet.Substring(14, 1),
			alphabet.Substring(13, 1),
			alphabet.Substring(18, 1),
			alphabet.Substring(67, 1),
			alphabet.Substring(62, 1),
			alphabet.Substring(31, 1),
			alphabet.Substring(11, 1),
			alphabet.Substring(0, 1),
			alphabet.Substring(6, 1),
			alphabet.Substring(62, 1),
			alphabet.Substring(63, 1),
			alphabet.Substring(62, 1),
			alphabet.Substring(1, 1),
			alphabet.Substring(17, 1),
			alphabet.Substring(8, 1),
			alphabet.Substring(23, 1),
			alphabet.Substring(4, 1),
			alphabet.Substring(11, 1),
			alphabet.Substring(28, 1),
			alphabet.Substring(45, 1),
			alphabet.Substring(31, 1),
			alphabet.Substring(65, 1),
			alphabet.Substring(12, 1),
			alphabet.Substring(55, 1),
			alphabet.Substring(12, 1),
			alphabet.Substring(52, 1),
			alphabet.Substring(17, 1),
			alphabet.Substring(24, 1),
			alphabet.Substring(66, 1)
		});

    Console.WriteLine(test);
  }
  
}
```

This is the solve code and it gives us the flag. 

> Congratulations! Flag = brixelCTF{m3m0ry}
using System;
using System.Collections;

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
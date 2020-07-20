# Object Oriented Programming
## Challenge Description
File: src.zip

## Solution
This is an obfuscated Java problem. We're given 15 java files with names like "fg" and "gl" and "xp", and one more called Main.java. A quick inspection shows the two-letter java files don't have any interesting functionality, just methods like

```
public String xn() { 
 return "sj";
}

public String xj() { 
 return "jk";
}

public String fx() { 
 return "hc";
}
```

All the interesting stuff is in Main.java, in `executeCodeThatDoesSomethingThatYouProbablyNeedToFigureOut`. It takes 2 letters of the user input, uses it as a class, and another 2 letters and uses them as a method. It calls that method to get two more letters, and uses that as another method; and then again. The final two letters are the result. After concatenating these together, the result should equal the goal string, `scanner.getClass().getPackageName().replace(".", "")`. So let's write code to do that in reverse.

Dropping this in `Main.main`:

```
String goalString = scanner.getClass().getPackageName().replace(".", "");
		System.out.println("Goal = " + goalString);
		
		Hashtable<String, String> invParts = new Hashtable<>();
		String[] classes = new String[]{"bv","cd","fg","gl","gq","gx","iy","mo","pr","qa","qg","vh","wz","xp","xq"};
		
		char xorKey = new EncryptionKeyInstantiator().getEncryptionKeyFactory().getEncryptionKey();
		
		for(String clazz : classes){
			Class<?> clz = Class.forName(clazz);
			Object object = clz.getConstructors()[0].newInstance();
			Method[] methods = clz.getDeclaredMethods();
			for(Method m : methods){
				try {
					String out = (String)m.invoke(object);
					String out2 = (String)clz.getDeclaredMethod(out).invoke(object);
					String out3 = (String)clz.getDeclaredMethod(out2).invoke(object);
					
					String in_enc = clazz + m.getName();
					System.out.println(in_enc+" ~=> "+out3);
					char[] in_arr = in_enc.toCharArray();
					for(int i=0;i<4;i++)
						in_arr[i] = (char)(in_arr[i] ^ xorKey);
					String in = new String(in_arr);
					invParts.put(out3, in);
					
					System.out.println(in+" ==> "+out3);
				} catch(Exception e){
					System.out.println(e);
				}
			}
		}
		
		String ans = "";
		for(int i=0; i<goalString.length(); i+=2){
			String bit = goalString.substring(i, i+2);
			String bot = invParts.get(bit);
			System.out.println(bit +" ==> "+bot);
			ans += bot;
		}
		System.out.println(ans);
```

and then `javac Main.java && java Main`, we get `Nice. Flag: rgbCTF{enterprisecodeee}`.

### Author
[timeroot](https://github.com/timeroot)
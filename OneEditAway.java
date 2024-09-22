/* Input: 2 strings
 * Output: true or false depending on whether the strings are one edit away
 * 
 * Example 1: 'hello' and 'hell' will return true
 * Examples 2: 'hello' and hellooo' will return false
 */

import java.util.Scanner;

public class OneEditAway {

	private String word1, word2;

	public OneEditAway(String first, String second) {
		word1 = first;
		word2 = second;
	}

	public boolean check() {
		boolean result = false;
		if(word1.length() == word2.length()) {
			int counter = 0;
			for(int i = 0; i < word1.length(); i++) {
				if(word1.charAt(i) != (word2.charAt(i))) {
					counter++;
				}
			}
			if(counter < 2) {
				result = true;
			}
		}
		if(word1.length() == (word2.length() + 1)) {
			String temp;
			for(int i = 0; i < word2.length() + 1; i++) {
				temp = word1.substring(0, i) + word1.substring(i + 1);
				if(word2.equals(temp)) {
					result = true;
				}
			}
		}
		if((word1.length() + 1) == word2.length()) {
			String temp;
			for(int i = 0; i < word1.length() + 1; i++) {
				temp = word2.substring(0, i) + word2.substring(i + 1);
				if(word1.equals(temp)) {
					result = true;
				}
			}
		}
		return result;
	}

	public static void main(String[] args) {
		String word1, word2;
		Scanner scnr = new Scanner(System.in);
		System.out.println("Enter your first word: ");
		word1 = scnr.next();
		System.out.println("Enter your second word: ");
		word2 = scnr.next();
		OneEditAway t = new OneEditAway(word1, word2);
		System.out.println(t.check());
	}
}
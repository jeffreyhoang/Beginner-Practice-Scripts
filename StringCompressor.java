import java.util.Scanner;

public class StringCompressor {
	String word;

	public StringCompressor(String word) {
		this.word = word;
	}

	public void compress() {
		StringBuilder result = new StringBuilder("");
		int counter = 1;
		char character = word.charAt(0);
		for(int i = 1; i < word.length(); i++) {
			if(character == word.charAt(i)) {
				counter++;
			}
			else {
				result.append(character + counter);
				character = word.charAt(i);
				counter = 1;
			}
		}
		result.append(character + counter);

		if(result.length() < word.length()) {
			System.out.println(result);
		}
		else {
			System.out.println(word);
		}
	}

	public static void main(String[] args) {
		Scanner scnr = new Scanner(System.in);
		System.out.print("Type in a word to compress: ");
		String word = scnr.next();
		StringCompressor obj1 = new StringCompressor(word);
		obj1.compress();
	}
}
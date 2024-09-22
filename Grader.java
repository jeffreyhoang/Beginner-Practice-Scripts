/* 
Given a homework score out of 100 points with 25% weights, a midterm score out of 100 with 25% weight, 
and a final score out of 200 with 50% weight, this script returns the weighted total and whether the student 
passed or failed the class  
*/

import java.util.Scanner;

public class Grader {

	double homework;
	double midterm;
	double finalGrade;
	double weightedGrade;

	public Grader() {
		homework = -1.0;
		midterm = -1.0;
		finalGrade = -1.0;
	}

	public void calculateWeighted() {
		Scanner scnr = new Scanner(System.in);
		System.out.print("Enter your homework grade: ");
		homework = scnr.nextDouble();
		while(homework < 0 || homework > 100) {
			System.out.println("[ERR] Invalid input. A homework grade should be in [0, 100].");
			System.out.print("Enter your homework grade: ");
			homework = scnr.nextDouble();
		}
		System.out.print("Enter your midterm grade: ");
		midterm = scnr.nextDouble();
		while(midterm < 0 || midterm > 100) {
			System.out.println("[ERR] Invalid input. A midterm grade should be in [0, 100].");
			System.out.print("Enter your midterm grade: ");
			midterm = scnr.nextDouble();
		}
		System.out.print("Enter your final grade: ");
		finalGrade = scnr.nextDouble();
		while(finalGrade < 0 || finalGrade > 200) {
			System.out.println("[ERR] Invalid input. A final grade should be in [0, 200].");
			System.out.print("Enter your final grade: ");
			finalGrade = scnr.nextDouble();
		}
		weightedGrade = (homework * 0.25) + (midterm * 0.25) + ((finalGrade / 200) * 100 * 0.5);
		System.out.printf("[INFO] Student's weighted total is %.2f%%.\n", weightedGrade);
	}

	public void pass() {
		if(weightedGrade >= 50) {
			System.out.println("Student PASSED the class.");
		}
		else {
			System.out.println("Student FAILED the class.");
		}
	}

	public static void main(String[] args) {
		Grader student = new Grader();
		student.calculateWeighted();
		student.pass();
	}
}
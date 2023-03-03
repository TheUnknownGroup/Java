import java.util.Scanner;
public class Main
{
    public static void main(String[] args) {
        
        String question1 = "This question has how many words?";
        String question2 = "What is the chemical symbol for Iron";
        String question3 = "How many states are there in the USA?";
        
        int answer1 = 6;
        String answer2 = "Fe"; 
        int answer3 = 50;
        
        int points = 0;
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.println(question1);
        int userInput1 = scanner.nextInt();
        
        if (userInput1 == answer1) {
            points++;
            System.out.println("Congrats, You got this question correct! You have " + points + " points!");
        } else {
            System.out.println("Oh Sorry, You got this wrong. You have " + points + " points.");
        }
        
        System.out.println("------");
        System.out.prtinln(question2);
        String userInput2 = scanner.next();
        
        if(userInput2.equals(answer2)) {
            points++;
            System.out.println("Congrats, You got this question correct! You have " + points + " points!");
        } else {
            System.out.println()
        }
    }
}

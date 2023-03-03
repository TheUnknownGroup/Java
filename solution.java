import java.util.Scanner;
public class Solution
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
            System.out.println("Congrats, You got this question correct! You have " + points + " point!");
        } else {
            points--;
            System.out.println("Oh Sorry, You got this wrong. You have " + points + " points.");
        }
        
        System.out.println("------");
        System.out.println(question2);
        String userInput2 = scanner.next();
        
        if(userInput2.equals(answer2)) {
            points++;
            System.out.println("Congrats, You got this question correct! You have " + points + " points!");
        } else {
            points--;
            System.out.println("Oh Sorry, You got this wrong. You have " + points + " points.");
        }
        
        System.out.println("------");
        System.out.println(question3);
        int userInput3 = scanner.nextInt();
        
        if(userInput3 == answer3) {
            points++;
            System.out.println("Congrats, You go this question correct! You have " + points + " points!");
        } else {
            points--;
            System.out.println("Oh Sorry, You got this wrong. You have " + points + " points.");
        }
        System.out.println("------");
        System.out.println("Here are your points: "+points+".");
        if (points == 3) {
            System.out.println("You did great!");
        } else if(points == 2) {
            System.out.println("You did ok, you only got 1 wrong!");
        } else if(points == 1) {
            System.out.println("You still did ok, you only got 2 wrong.");
        } else if(points == 0) {
            System.out.println("You got none of them right, please try again later.");
        } else if(points < 0){
            System.out.println("HOW DID YOU GET NEGATIVE POINTS??????");
        }
    }
}

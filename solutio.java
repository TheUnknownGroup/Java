import java.util.Scanner;
public class solutio
{
  public static void main(String[] args){
    /* Trivia Questions! */

    //points
    String line ="------";
    String correct ="Congrats, You got this question correct! You gained a point!";
    String wrongr ="Whoops, you got this question wrong. You lost a point.";
    String p3 ="You got all of the questions correct!";
    String p2 ="You only got 1 question wrong!";
    String p1 ="You got 2 questions wrong. It's alright, just try harder next time.";
    String p0 ="You got all of the questions wrong...How?";
    String po1 ="HOW DID YOU GET NEGATIVE POINTS???!!!!";
    String pointsNumber ="Here are your points: ";
    //Questions & beginning
    String welcome="Welcome! This is a trivia game. Would you like to continue?";
    String question1="What is the element name for Fe";
    String question2="What are the positive atoms?";
    String question3="What are the negative atoms?";
    
    String answer1="Iron";
    String answer2="Protons";
    String answer3="Electrons";
    String welcomeYes="Yes";

    int points=0;
    
    Scanner input = new Scanner(System.in);
      System.out.println(welcome);
      String userInputWelcome = input.next();

      if (userInputWelcome.equals(welcomeYes)){
        System.out.println("You have picked 'Yes', you will now proceed to the questions area.");
        System.out.println(line);
        System.out.println(question1);
      } else {
        System.out.println("You you didn't type 'Yes' so, you will not continue with the following questions. Thank you for taking the time to go to this survey.");
        System.exit(0);
      }
      String userInput1 = input.next();
      
      if (userInput1.equals(answer1)){
        points++;
        System.out.println(correct);
      } else {
        points--;
        System.out.println(wrongr);
      }

      System.out.println(line);
      System.out.println(question2);
      String userInput2 = input.next();
      
      if(userInput2.equals(answer2)) {
        points++;
        System.out.println(correct);
      } else {
        points--;
        System.out.println(wrongr);
      }
      
      System.out.println(line);
      System.out.println(question3);
      String userInput3 = input.next();

      if(userInput3.equals(answer3)) {
        points++;
        System.out.println(correct);
      } else {
        points--;
        System.out.println(wrongr);
      }

      System.out.println(line);
      System.out.println(pointsNumber +points);
      
      if(points == 3) {
        System.out.println(p3);
      } else if(points == 2) {
        System.out.println(p2);
      } else if(points == 1) {
        System.out.println(p1);
      } else if(points == 0) {
        System.out.println(p0);
      } else if(points < 0) {
        System.out.println(po1);
      }
  }
}

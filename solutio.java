import java.util.Scanner;
public class solutio
{
  public static void main(String[] args){
    
    String welcome="Welcome! This is a trivia game. Would you like to continue?";
    String question1="What is the element name for Fe";
    String question2="What are the positive atoms?";
    String question3="What are the negative atoms?";
    
    String answer1="Iron";
    String answer2="Protons";
    String answer3="Electrons";
    String welcomeYes="Yes";

    int points=0;
    
    Scanner scanner = new Scanner(System.in);
    
    System.out.println(welcome);
    int userInputWelcome = scanner.next();

    if (userInputWelcome.equals(welcomeYes)){
      System.out.println("You have picked 'Yes', you will now proceed to the questions area.");
    } else {
      System.out.println("You have picked 'No', you will not continue with the following questions.");  
    }

    System.out.println(question1);
    int userInput1 = scanner.next();
    
    if (userInput1.equals(answer1)){
      points++;
      System.out.println("");
    } else {
      points--;
      System.out.println("");
    }
    
  }
}

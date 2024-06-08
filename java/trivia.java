import java.util.Scanner;

public class trivia
{
    @SuppressWarnings({ "resource", "unused" })
    public static void main(String[] args){
        /* Trivia Game */

        String line="------";

        String welcome="Welcome! Would you like to continue?";
        
        String question1="What is 2+2?";

        int points = 0;

        Scanner input = new Scanner(System.in);
        System.out.println(welcome);
        String userInputWelcome = input.next();

        if(userInputWelcome.equals("Yes")) {
            System.out.println("Then lets get on with the journey!");
        } else if(userInputWelcome.equals("yes")) {
            System.out.println("Then lets get on with the journey!");
        } else if(userInputWelcome != "Yes") {
            System.out.println("THIS IS A INTEGER??");
            System.exit(1);
        } else if(userInputWelcome != "yes") {
            System.out.println("THIS IS A INTEGER??");
            System.exit(1);
        }
        
        System.out.println(line+"\n"+question1);
        int userInput1 = input.nextInt();

        if (userInput1 == 4){
            points += 1;
            System.out.println("Well done! You got this correct!");
        } else if(userInput1 != 4) {
            System.out.println("HOW IN THE WORLD DID YOU HAPPEN TO GET 2+2 WRONG?????????");
        }
        
    }
}


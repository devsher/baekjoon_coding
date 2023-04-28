import java.util.Scanner;
/**
 * .
 * 
 * @author (샤러브디노브 셰르저드) 
 * 학번 (2020330107)
 * 과제#1
 */
public class MyCalculator
{
  
    public static void main (String[]args)
    {
        Scanner scan = new Scanner(System.in);
        System.out.println("첫번째 숫자를 입력하세요>>");
        String num1 = scan.nextLine();
        System.out.println("기호를 입력하세요>>");
        String rule = scan.nextLine();
        System.out.println("두번째 숫자를 입력하세요>>");
        String num2 = scan.nextLine();
        int number1 = Integer.parseInt(num1);
        int number2 = Integer.parseInt(num2);
        int result;
        switch (rule)
        {
            case "+":
              result = number1 + number2;
              System.out.println(number1+"+" + number2 +"의 계산 결과는"+ result);
              break;
            case "-":
              result = number1 - number2;
              System.out.println(number1+"-" + number2 +"의 결과는 "+ result);
              break;
            case "*":
              result = number1 * number2;
              System.out.println(number1+"*" + number2 +"의 결과는  "+ result);
            break;
            case "/":
                
                result = number1 / number2;
                System.out.println(number1+"/" + number2 +"의 결과는  "+ result);
            
            default:
                 System.out.println("0에 나눌 수 없습니다.");
                 break;
            
             
            }
            scan.close();
            
            
        
    
    }
    
    
}

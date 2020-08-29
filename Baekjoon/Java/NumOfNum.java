package Java;

import java.util.Scanner;

public class NumOfNum {
    public static void main(String[] args) throws NumberFormatException {
        Scanner scan = new Scanner(System.in);
        int[] num = {0,0,0,0,0,0,0,0,0,0};
        int a=0, b=0, c=0;
        a = scan.nextInt();
        b = scan.nextInt();
        c = scan.nextInt();
        char[] s = Integer.toString(a*b*c).toCharArray();
        for (int i=0; i<s.length; i++) {
            num[s[i]-'0']++;
        }

        for (int i=0; i<10; i++) {
            System.out.println(num[i]);
        }
    }
}
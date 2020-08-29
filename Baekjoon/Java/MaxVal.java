package Java;

import java.util.Scanner;

public class MaxVal {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int mval = 0, idx = 0;

        for (int i=0; i<9; i++){
            int in = scan.nextInt();
            if (in > mval) {
                mval = in;
                idx = i+1;
            }
        }

        System.out.println(mval+"\n"+idx);
    }
}
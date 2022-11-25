import java.util.Scanner;

class MyThread extends Thread {
    public MyThread(String name){
        super(name);
    }
    @Override
    public void run(){
        Scanner sc= new Scanner(System.in);
        if (Thread.currentThread().getName()=="add"){
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println("The addition is " + (a+b));
        }
        else if (Thread.currentThread().getName()=="sub"){
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println("The subtraction is " + (a-b));
        }
        else if (Thread.currentThread().getName()=="mul"){
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println("The multiplication is " + (a*b));
        }
        else if (Thread.currentThread().getName()=="div"){
            int a = sc.nextInt();
            int b = sc.nextInt();
            double c = (double) a/b;
            System.out.println("The division is " + c);
        }
        else if (Thread.currentThread().getName()=="oth")
            System.out.println("No Valid Operation");
        
    }    
}


public class Lab3T1 {
    public static void main(String[]args){
        MyThread add = new MyThread("add");
        MyThread sub = new MyThread("sub");
        MyThread mul = new MyThread("mul");
        MyThread div = new MyThread("div");
        MyThread oth = new MyThread("oth");

        add.start();
        sub.start();
        mul.start();
        div.start();
        oth.start();
    }
}


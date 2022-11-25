class MyThread1 extends Thread {
    public MyThread1(String name){
        super(name);
    }
    @Override
    public void run(){
        System.out.println("The house is : "+getName());
        if (getName().equals("House Stark") || getName().equals("House Targaryen")){
            try {
                sleep(1000);
            } 
            catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        else if (getName().equals("House Lannister") || getName().equals("House Bolton")){
            try {
                sleep(3000);
            } 
            catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        else{
            try {
                sleep(5000);
            } 
            catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

public class Lab3T2 {
    public static void main(String[]args){
        MyThread1 t1 = new MyThread1("House Stark");
        MyThread1 t2 = new MyThread1("House Targaryen");
        MyThread1 t3 = new MyThread1("House Lannister");
        MyThread1 t4 = new MyThread1("House Bolton");
        MyThread1 t5 = new MyThread1("House Tyrell");

        t1.setPriority(Thread.MAX_PRIORITY);
        t4.setPriority(Thread.MIN_PRIORITY);

        t1.run();
        t2.run();
        t3.run();
        t4.run();

        t1.start();
        t5.start();
        t3.start();
        t4.start();

        try {
            t1.join();
            t3.join();
            t4.join();
        } 
        catch (InterruptedException e) {
            e.printStackTrace();
        }

        if (t1.isAlive())
            System.out.println("Not Today!");
        if (!t4.isAlive())
            System.out.println("You know nothing!");
    }
}

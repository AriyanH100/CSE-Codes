class MyThread2 extends Thread {
    public MyThread2(String name){
        super(name);
    }
    public static long result = 0;
    @Override
    public void run(){
        if (Thread.currentThread().getName() == "Thread 1"){
            
            long n1 = 0 , n2 = 1 , n3 , n4 = 0 , result1 ,  c = 0 , i, count = 25;  //first half odd//     
           
            for (i = 0 ; i < count ; ++i){    
                if (i == 0){
                    n3 = 0;
                }
                else if (i == 1){
                    n3 = 1;
                }
                else{
                    n3=n1+n2;       
                    n1=n2;    
                    n2=n3;
                }
                if (n3 % 2 != 0){
                    n4 = n4 + n3;
                    c = c + 1;
                }
            }
            result1 = n4 / c ;
            System.out.println("Mean Odd for First Half " + result1);
            result = result + result1;
        }
        
        if (Thread.currentThread().getName() == "Thread 2"){
            
            long n1 = 0 , n2 = 1 , n3 , n4 = 0 , result2 , c = 0 , i, count = 25;  //first half even//        
           
            for (i = 0 ; i < count ; ++i){    
                if (i == 0){
                    n3 = 0;
                }
                else if (i == 1){
                    n3 = 1;
                }
                else{
                    n3=n1+n2;       
                    n1=n2;    
                    n2=n3;
                }
                if (n3 % 2 == 0){
                    n4 = n4 + n3;
                    c = c + 1;
                }
            }
            result2 = n4 / c ;
            System.out.println("Mean Even for First Half " +result2);
            result = result + result2;
        }
        
        if (Thread.currentThread().getName() == "Thread 3"){
            
            long n1 = 0 , n2 = 1 , n3 , n4 = 0 , result3 , c = 0 , i, count = 50;  //second half odd//         
           
            for (i = 0 ; i < count ; ++i){    
                if (i == 0){
                    n3 = 0;
                }
                else if (i == 1){
                    n3 = 1;
                }
                else{
                    n3=n1+n2;       
                    n1=n2;    
                    n2=n3;
                }
                if ( i > 24 && n3 % 2 != 0){
                    n4 = n4 + n3;
                    c = c + 1;
                }
            }
            result3 = n4 / c ;
            System.out.println("Mean Odd for Second Half " + result3);  //second half even// 
            result = result + result3;
        }
        if (Thread.currentThread().getName() == "Thread 4"){
            
            long n1 = 0 , n2 = 1 , n3 , n4 = 0 , result4 , c = 0 , i, count = 50;       
           
            for (i = 0 ; i < count ; ++i){    
                if (i == 0){
                    n3 = 0;
                }
                else if (i == 1){
                    n3 = 1;
                }
                else{
                    n3=n1+n2;       
                    n1=n2;    
                    n2=n3;
                }
                if ( i > 24 && n3 % 2 == 0){
                    n4 = n4 + n3;
                    c = c + 1;
                }
            }
            result4 = n4 / c ;
            System.out.println("Mean Even for Second Half " + result4);
            result = result + result4;
        }
        if (Thread.currentThread().getName() == "Thread 5"){
        
            System.out.println("Average of 4 Mean "+ (result/4));
            System.out.println("PIN: "+ (result/4));
        }
    }
}
    
   
public class Lab3T3 {
    public static void main(String[]args){
        MyThread2 t1 = new MyThread2("Thread 1");
        MyThread2 t2 = new MyThread2("Thread 2");
        MyThread2 t3 = new MyThread2("Thread 3");
        MyThread2 t4 = new MyThread2("Thread 4");
        MyThread2 t5 = new MyThread2("Thread 5"); 
        
        t1.start();
        t2.start();
        t3.start();
        t4.start();

        try {
            t1.join();
            t2.join();
            t3.join();
            t4.join();
        } 
        catch (InterruptedException e) {
            e.printStackTrace();
        }
        t5.start();
    }
}

    




 
              
        


    

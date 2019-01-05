import java.io.*;

public class pv_operate {
	public static void main(String args[]) {
		Synstack ss=new Synstack();
		Producer p=new Producer(ss);
		Consumer c=new Consumer(ss);
		Thread one=new Thread(p);
		Thread two=new Thread(c);
		one.start();
		two.start();
	}
}

class Producer implements Runnable{
	Synstack ss=new Synstack();
	Producer(Synstack ss){
		this.ss=ss;
	}
	
	public void run() {
		for(int i=1;i<=20;i++) {
			ss.push();
			System.out.println("Produce NO."+i+"  have index="+ss.index);
                        try{
                         Thread.sleep(1000);
                         }catch (InterruptedException e){
                              e.printStackTrace();
                          }
		}
	}
}

class Consumer implements Runnable{
    Synstack ss=new Synstack();
	Consumer(Synstack ss){
		this.ss=ss;
	}
	
	public void run() {
		for(int i=1;i<=20;i++) {
			ss.pull();
			System.out.println("Consume No."+i+"  have index="+ss.index);
                        try{
                         Thread.sleep(2000);
                         }catch (InterruptedException e){
                              e.printStackTrace();
                          }
		}
	}	
}

class Synstack{
	int max=10;
	int index=0;
	public synchronized void push() {
		if(index==max) {
			try {
				this.wait();
			}
			catch(Exception e) {System.out.println(e);}
		}
		this.notify();
        index++;
	}
	
	public synchronized void pull() {
		if(index==0) {
			try {
				this.wait();
			}
			catch(Exception e) {System.out.println(e);}
		}
		this.notify();
		index--;
	}
	
}
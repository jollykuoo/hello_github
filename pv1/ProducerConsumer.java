//客户端
public class ProducerConsumer{
    public static void main(String[] args){
        SyncStack ss =new SyncStack();
        Producer p =new Producer(ss);
        Customer c =new Customer(ss);
        new Thread(p).start();
        new Thread(c).start();

    }
}

//生产的产品
class Product{
    int id;
    //构造函数
    Product(int _id){
        this.id=_id;
    }

    public String toString(){
        return "产品："+id;
    }
}

//容器
class SyncStack{
    int index=0;
    Product[] Arrpro =new Product[10];  //容器最多可以放10个产品

    //容器中放产品的方法
    public synchronized void push(Product pro){
        //如果满了
        if(index ==Arrpro.length){
            try{
                this.wait();
            }catch(InterruptedException e){
                e.printStackTrace();
            }
        }
        this.notify(); //唤醒正在等待的线程

        Arrpro[index]=pro;
        index++;
    }
    //容器中取产品
    public  synchronized Product pull(){
        if(index ==0){
            try{
                this.wait();
            }catch(InterruptedException e){
                e.printStackTrace();
            }

        }
        this.notify(); //唤醒正在等待的线程
        index--;
        return Arrpro[index];

    }
}

//生产者--申请一个线程
class Producer implements Runnable{
    SyncStack ss =new SyncStack();
    Producer(SyncStack _ss){
        this.ss=_ss;
    }
    public void run(){
        //生产者能够造20个产品
        for(int i=0;i<20;i++){
            Product pro=new Product(i);
            ss.push(pro);
            System.out.println("生产了"+pro);
            try{
                Thread.sleep(1000);
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}

//消费者
class Customer  implements Runnable{
    SyncStack ss =new SyncStack();
    Customer(SyncStack _ss){
        this.ss=_ss;
    }

    public void run(){
        for(int i=0;i< 20;i++){
            Product pro =ss.pull();
            System.out.println("消费了"+pro);

            try{
                Thread.sleep(2000);
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        }       
    }
}

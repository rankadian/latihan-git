import java.util.Scanner;
/**
 * PurchasePrice10
 */
public class PurchasePrice10 {
    
    public static void main(String[] args) {
        Scanner input =new Scanner(System.in);
        int price, quality;
        double discount=0.1, totalPrice, purchasePrice, totalDiscount;
        System.out.println("Input price :");
        price = input.nextInt();
        System.out.println("Input quality :");
        quality = input.nextInt();  
        totalPrice = price*quality;
        totalDiscount = totalPrice*discount;
        purchasePrice = totalPrice-totalDiscount;
        System.out.println("Total discount: " + totalDiscount); 
        System.out.println("Final purchase price: " + purchasePrice);
    }
}
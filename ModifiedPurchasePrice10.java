import java.util.Scanner;
/**
 * ModifiedPurchasePrice10
 */
public class ModifiedPurchasePrice10 {
    
    public static void main(String[] args) {

        Scanner input =new Scanner(System.in);
        int price, quality, pageCount;
        double discount=0.1, totalPrice, purchasePrice, totalDiscount;
        String nameOfBook;
        System.out.println("Input name of book :");
        nameOfBook = input.next();
        System.out.println("Input page count :");
        pageCount = input.nextInt();
        System.out.println("Input price :");
        price = input.nextInt();
        System.out.println("Input quality :");
        quality = input.nextInt();  
        totalPrice = price*quality;
        totalDiscount = totalPrice*discount;
        purchasePrice = totalPrice-totalDiscount;
        System.out.println("Name of book: " + nameOfBook);
        System.out.println("Page count: " + pageCount);
        System.out.println("Total discount: " + totalDiscount); 
        System.out.println("Final purchase price: " + purchasePrice);

    }
}
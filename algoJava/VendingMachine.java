package VendingMachine;
// from https://www.youtube.com/watch?v=UaQm9YKPv0c
// prof. Weng
public class VendingMachine {
	int price;
	int balance;
	int total;
	
	void showPrompt()
	{
		System.out.println("welcome!");
	}
	
	void insertMoney(int amount)
	{
		balance = balance + amount;
	}
	
	void showBalance()
	{
		System.out.println(balance);
	}
	
	void getFood()
	{
		price = 10;
		if (balance >= price ) {
			System.out.println("here you are: ");
			balance = balance - price;
			total = total + price;
		}
	}
	
	public static void main(String[] args) {
		VendingMachine vm = new VendingMachine();
		vm.showPrompt();
		vm.showBalance();
		vm.insertMoney(100);
		vm.showBalance();
		vm.getFood();
		vm.showBalance();
	}

}

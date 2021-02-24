public class PalindromeNumber {

    public static void main(String[] args) {
        System.out.println("Hello World");
    }

    public boolean isPalindrome(int x) {

        String inputAsString = Integer.toString(x);
        String inputAsReverse = "";

        for (int i = inputAsString.length() - 1; i >= 0; i-- ) {
            inputAsReverse = inputAsReverse + inputAsString.charAt(i);
        }

        if (inputAsString.equals(inputAsReverse)) {
            return true;
        } else {
            return false;
        }

    }
}

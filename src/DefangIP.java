public class DefangIP {

    public static void main(String[] args) {
        System.out.println("Hello World");

        String addr = "1.1.1.1";
        System.out.println(defangIPaddr(addr));
    }

    /**
     * Input 1.1.1.1
     * Output 1[.]1[.] ...
     * @param address
     * @return
     */
    public static String defangIPaddr(String address) {

        StringBuilder stringBuilder = new StringBuilder();

        for (int i = 0; i < address.length(); i++) {

            if (address.charAt(i) != '.') {
                stringBuilder.append(address.charAt(i));
            }

            if (address.charAt(i) == '.') {
                stringBuilder.append("[.]");
            }

        }

        String returnValue = stringBuilder.toString();

        return returnValue;
    }
}

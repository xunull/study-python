
public class Java {

    // 10000
    // 94 millsecond

    // 100000
    // 9224 millsecond

    public static void main(String args[]) {
        int count = 10000;
        double z = 0;
        long start = System.currentTimeMillis();
        for (int x = 0; x < count; x++) {
            for (int y = 0; y < count; y++) {
                z += 1;
            }
        }
        long end = System.currentTimeMillis();
        System.out.println(z);
        System.out.println("cost: " + (end - start) + "ms");
    }
}
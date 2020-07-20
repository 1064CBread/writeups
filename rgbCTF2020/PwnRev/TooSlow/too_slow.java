public class TooSlow {
    public static void main(String[] args) throws Exception {
        long a = 0x12297E12426E6F53L;
        long b = 0x79242E48796E7141L;
        long c = 0x49334216426E2E4DL;
        long d = 0x473E425717696A7CL;
        long e = 0x42642A41;

        int key = 0x265D1D23;

        dec(a,key);
        dec(b,key);
        dec(c,key);
        dec(d,key);
        dec(e,key);
    }

    static void dec(long a, int key){
        for(int i=0;i<8;i++){
            int kByte = (int)((key >> (8*(i%4)))&0xFF);
            int aByte = (int)((a >> (8*i))&0xFF);
            int res = kByte ^ aByte;
            System.out.print((char)(res));
        }
    }
}
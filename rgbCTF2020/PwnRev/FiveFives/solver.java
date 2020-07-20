import java.util.*;
import java.io.*;
import java.nio.ByteBuffer;
import java.util.concurrent.ThreadLocalRandom;
import java.security.*;
import java.net.Socket;

public class Five_Trial {
    public static void main(String[] args) throws Exception {

        final boolean NET = true;
        BufferedReader in;
        PrintWriter out;

        //Big loop, connecting over and over
        while(true){

            if(NET){

                String hostName = "167.172.123.213";
                int portNumber = 7425;

                Socket echoSocket = new Socket(hostName, portNumber);
                out =
                        new PrintWriter(echoSocket.getOutputStream(), true){
						/*public void println(String s){
							System.out.print("[ECHO]"+s);
							super.println(s);
						}*/
                        };
                in =
                        new BufferedReader(
                                new InputStreamReader(echoSocket.getInputStream()));
            } else {
                out = new PrintWriter(System.out, true);
                in = new BufferedReader(new InputStreamReader(System.in));
            }

            System.out.println("Header:  "+in.readLine());
            System.out.println("Header2: "+in.readLine());
            System.out.println("Header3: "+in.readLine());

            int[] yesterday = new int[5];
            String yest_line = in.readLine();
            for(int i=0;i<5;i++){
                int a = Integer.parseInt(yest_line.split(" ")[i]);
                yesterday[i] = a;
            }
            System.out.println("Yesterday: "+Arrays.toString(yesterday));

            System.out.println("Header4: "+in.readLine());

            ArrayList<String> guesses = new ArrayList<>();
            for(int x=1;x<=5;x++)
                for(int y=1;y<=4;y++)
                    guesses.add("1 1 1 "+x+" "+y);

            out.println(guesses.size());

            boolean won = false;
            for(int i=0;i<guesses.size();i++){
                System.out.println("HeaderN1: "+in.readLine());
                System.out.println("Guessing "+guesses.get(i));
                out.println(guesses.get(i));
                String response = in.readLine();
                System.out.println("HeaderN2: "+response);
                if(response.startsWith("Congratulations")){
                    won = true;
                    break;
                }
            }

            if(!won)
                continue;
            break;
        }

        System.out.println("End1: "+in.readLine());
        System.out.println("End2: "+in.readLine());
    }
}
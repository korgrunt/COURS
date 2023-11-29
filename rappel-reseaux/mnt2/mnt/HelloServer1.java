import java.net.*;
import java.io.*;

class HelloServer1 {
    public static void main(String argv[]) throws Exception
    {
        //On installe le combine sur le numero de telephone
        ServerSocket serversocket = new ServerSocket(1111);
        //On attend les appels entrants
        Socket socket = serversocket.accept();
        //On ouvre un tube pour envoyer un message
        PrintStream out = new PrintStream( socket.getOutputStream() );
        InputStreamReader in = new InputStreamReader( socket.getInputStream() );
	int i=0;
	while( i != 5) 
        { //On ecrit et on envoie le message
        	out.println( "Hello World from server!" );
            char[] responseSpace = new char[20];
            in.read(responseSpace);
            System.out.println(responseSpace );

            i++;
	}
        //On raccroche
        socket.close();
    }
}

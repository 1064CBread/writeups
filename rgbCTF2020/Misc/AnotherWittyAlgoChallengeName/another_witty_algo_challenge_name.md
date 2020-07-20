# [another witty algo challenge name]
## Challenge Description
File: grid.txt

## Solution
The problem is literally to implement flood-fill: we're given a grid of 0's and 1's and are supposed to count how many "islands" of 1's there are, and that number is the flag. Only orthogonal connections matter.

Use https://en.wikipedia.org/wiki/Flood_fill : visit each square in the grid. If it's a 0, ignore. If it's 1 and it's been "marked", meaning we've already counted it, ignore. If it's a 1 we haven't marked, use flood-fill to "mark" every 1 it's connected to, and then increment the island count by 1.

Don't use a dumb stack-based implementation of Flood fill because you'll probably overflow; we use a queue.

Solver script:
```
import java.util.*;
import java.io.*;
import java.nio.ByteBuffer;
import java.util.concurrent.ThreadLocalRandom;
import java.security.*;
import java.net.Socket;

public class Grid {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new FileReader("./grid.txt"));
		boolean[][] map = new boolean[5000][5000];
		for(int x=0;x<5000;x++){
			String line = br.readLine();
			for(int y=0;y<5000;y++){
				map[x][y] = line.charAt(y) == '1';
			}
		}
		
		boolean[][] marked = new boolean[5000][5000];
		int islands = 0;
		
		LinkedList<Integer> toVisit = new LinkedList<>();
		LinkedList<Integer> toMark = new LinkedList<>();
		
		for(int x=0;x<5000;x++){
			for(int y=0;y<5000;y++){
				toVisit.add(x*5000 + y);
			}
		}
		
		while(toVisit.size() > 0){
			int vis = toVisit.pop();
			
			{
				int x = vis/5000;
				int y = vis%5000;
				if(!map[x][y])
					continue;
				if(marked[x][y])
					continue;
				islands++;
				System.out.println("Island at "+x+", "+y);
			}
					
			toMark.push(vis);
			
			while(toMark.size() > 0){
				int mark = toMark.pop();
				int x = mark/5000;
				int y = mark%5000;
				if(!map[x][y])
					continue;
				if(marked[x][y])
					continue;
				
				marked[x][y] = true;
				if(x>0)
					toMark.add((x-1)*5000 + (y-0));
				if(x<4999)
					toMark.add((x+1)*5000 + (y-0));
				if(y>0)
					toMark.add((x-0)*5000 + (y-1));
				if(y<4999)
					toMark.add((x-0)*5000 + (y+1));
			}
		}
		System.out.println("Total islands: "+islands);
    }
}
```

### Author
[timeroot](https://github.com/timeroot)

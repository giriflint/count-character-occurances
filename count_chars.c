#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printUsage() {
    printf("Usage:\n ");
    printf("\n./count_chars <filename>\n where filename is the absolute path to the file containing the characters\n");
    exit(0);
}

int main(int argc, char *argv[]) {
    if ((argc != 2) || (strcmp(argv[1],"-h") == 0)) {
	    printUsage();
    }
	
    int count[256] = { 0 }; /* 256 for ascii character set
			    chose this after looking at --print-chars*/
	
    FILE* f = fopen(argv[1], "r");
    if (f) {  
        int ch;
        
        while((ch=fgetc(f))) {
            if(ch == EOF) break;
            count[ch]+=1;
        }
        //print the occurence nos. of each character that is present in the file 
        for (int j=0;j<256;j++) {
		if (count[j]>0)
	                printf ("%c - %d\n", j, count[j]);
        }
    }
    else {
        printf("\nUnable to open the given file\n");
    }
    
    if(f) {
	fclose(f);
    }
    
    return 0;
}

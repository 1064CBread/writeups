#include "stdio.h"
#include "string.h"

#define HIDWORD(foo) ((foo >> 32) & 0xFFFFFFFF)

char* encryptFlag(char *result)
{
  unsigned char v1; // r3
  char *i; // r1
  int v3; // r3
  char v4; // zf
  unsigned int v5; // r3
  unsigned int v6; // r2
  unsigned long long v7; // r2

  v1 = (unsigned char)*result;
  if ( *result )
  {
    for ( i = result; ; v1 = (unsigned char)*i )
    {
      v6 = (unsigned char)(v1 - 10);
      if ( v1 <= 'O' )
      {
        v1 = v1 + 'F';
        if ( v6 <= 'P' )
          v1 = v6;
      }
      *i++ = (((unsigned char)(v1 - 7) ^ 0x43) << 6) | ((unsigned char)((v1 - 7) ^ 0x43) >> 2);
      v7 = i - result;
      if ( !*i )
        break;
      v3 = v7 - 5 * (((signed int)((unsigned long long)(0x66666667LL * (signed int)v7) >> 32) >> 1) - HIDWORD(v7));
      v4 = v3 == 2;
      v5 = (((unsigned char)*i << (-(char)v3 & 7)) | ((unsigned int)(unsigned char)*i >> v3)) & 0xFF;
      if ( v4 )
        v5 = v5 - 1;
      *i = v5;
    }
  }
  return result;
}

void main(int argc, char** argv){
	char* goal = "\x0A\xFB\xF4\x88\xDD\x9D\x7D\x5F\x9E\xA3\xC6\xBA\xF5\x95\x5D\x88\x3B\xE1\x31\x50\xC7\xFA\xF5\x81\x99\xC9\x7C\x23\xA1\x91\x87\xB5\xB1\x95\xE4";
	int len = strlen(goal);
	printf("Len %d\n", len);
	
	char trial[35+1];
	char check[35+1];
	
	for(int l=0;l<35;l++){
		trial[l+1] = 0;
		for(int c=1;c<200;c++){
			trial[l] = c;
			strcpy(check,trial);
			encryptFlag(check);
			if(!strncmp(check, goal, l+1))
				break;
		}
		printf("So far %s\n", trial);
	}
					
	puts(trial);
}

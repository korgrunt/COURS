#include <stdlib.h> 
#include <stdio.h> 
#include <glib.h> 

  typedef struct pcap_hdr_s {
          guint32 magic_number;   /* magic number */
          guint16 version_major;  /* major version number */
          guint16 version_minor;  /* minor version number */
          gint32  thiszone;       /* GMT to local correction */
          guint32 sigfigs;        /* accuracy of timestamps */
          guint32 snaplen;        /* max length of captured packets, in octets */
          guint32 network;        /* data link type */
  } pcap_hdr_t;



int main (){

	printf("\ntest\n");
	printf("%d", sizeof(guint32));
	return 0;
}

#include <stdint.h>
#include <stdio.h>
#include <sys/time.h>

#include "../includes/config.h"
#include "md4.h"
#include <emmintrin.h>

/*
 * The MD4 transformation for all three rounds.
 */
#define STEP(f, a, b, c, d, x, s) \
  (a) += _mm_add_epi32(f((b), (c), (d)),(x));  \
  (a) = (((_mm_slli_epi32((a), (s)))) | (_mm_srli_epi32(((a) & 0xffffffff),(32 - (s)))));

/*
 * The basic MD4 functions.
 *
 * F and G are optimized compared to their RFC 1320 definitions, with the
 * optimization for F borrowed from Colin Plumb's MD5 implementation.
 */
#define F(x, y, z) ((z) ^ ((x) & ((y) ^ (z))))
#define G(x, y, z) (((x) & ((y) | (z))) | ((y) & (z)))
#define H(x, y, z) (((x) ^ (y)) ^ (z))
#define H2(x, y, z) ((x) ^ ((y) ^ (z)))

/*
 * SET reads 4 input bytes in little-endian byte order and stores them
 * in a properly aligned word in host byte order.
 *
 * The check for little-endian architectures that tolerate unaligned
 * memory accesses is just an optimization.  Nothing will break if it
 * doesn't work.
 */
#if ARCH_ALLOWS_UNALIGNED == 1
#define SET(n) \
  (*(MD4_u32plus *)&ptr[(n) * 4])
#define GET(n) \
  SET(n)
#else
#define SET(n) (ptr[n])
#define GET(n) (ptr[n])
#endif

void my_body(unsigned char *candidate, __m128i *res, unsigned char *target)
{
  __m128i a, b, c, d;

  a = _mm_set1_epi32(0x67452301);
  b = _mm_set1_epi32(0xefcdab89);
  c = _mm_set1_epi32(0x98badcfe);
  d = _mm_set1_epi32(0x10325476);
  unsigned char * ptr = candidate;
  

  STEP(F, a, b, c, d, _mm_set1_epi32(ptr[0]), 3)
  STEP(F, d, a, b, c, _mm_set1_epi32(ptr[1]), 7)
  STEP(F, c, d, a, b, _mm_set1_epi32(ptr[2]), 11)
  STEP(F, b, c, d, a, _mm_set1_epi32(ptr[3]), 19)
  STEP(F, a, b, c, d, _mm_set1_epi32(ptr[4]), 3)
  STEP(F, d, a, b, c, _mm_set1_epi32(ptr[5]), 7)
  STEP(F, c, d, a, b, _mm_set1_epi32(ptr[6]), 11)
  STEP(F, b, c, d, a, _mm_set1_epi32(ptr[7]), 19)
  STEP(F, a, b, c, d, _mm_set1_epi32(ptr[8]), 3)
  STEP(F, d, a, b, c, _mm_set1_epi32(ptr[9]), 7)
  STEP(F, c, d, a, b, _mm_set1_epi32(ptr[10]), 11)
  STEP(F, b, c, d, a, _mm_set1_epi32(ptr[11]), 19)
  STEP(F, a, b, c, d, _mm_set1_epi32(ptr[12]), 3)
  STEP(F, d, a, b, c, _mm_set1_epi32(ptr[13]), 7)
  STEP(F, c, d, a, b, _mm_set1_epi32(ptr[14]), 11)
  STEP(F, b, c, d, a, _mm_set1_epi32(ptr[15]), 19)

  __m128i val = _mm_set1_epi32(0x5a827999);
  __m128i valSecond = _mm_set1_epi32(0x6ed9eba1);

  /* Round 2 */
  STEP(G, a, b, c, d, _mm_add_epi32(_mm_set1_epi32(ptr[0]) , val), 3)
  STEP(G, d, a, b, c, _mm_add_epi32(_mm_set1_epi32(ptr[4]) , val), 5)
  STEP(G, c, d, a, b, _mm_add_epi32(_mm_set1_epi32(ptr[8]) , val), 9)
  STEP(G, b, c, d, a, _mm_add_epi32(_mm_set1_epi32(ptr[12]) , val), 13)
  STEP(G, a, b, c, d, _mm_add_epi32(_mm_set1_epi32(ptr[1]) , val), 3)
  STEP(G, d, a, b, c, _mm_add_epi32(_mm_set1_epi32(ptr[5]) , val), 5)
  STEP(G, c, d, a, b, _mm_add_epi32(_mm_set1_epi32(ptr[9]) , val), 9)
  STEP(G, b, c, d, a, _mm_add_epi32(_mm_set1_epi32(ptr[13]) , val), 13)
  STEP(G, a, b, c, d, _mm_add_epi32(_mm_set1_epi32(ptr[2]) , val), 3)
  STEP(G, d, a, b, c, _mm_add_epi32(_mm_set1_epi32(ptr[6]) , val), 5)
  STEP(G, c, d, a, b, _mm_add_epi32(_mm_set1_epi32(ptr[10]) , val), 9)
  STEP(G, b, c, d, a, _mm_add_epi32(_mm_set1_epi32(ptr[14]) , val), 13)
  STEP(G, a, b, c, d, _mm_add_epi32(_mm_set1_epi32(ptr[3]) , val), 3)
  STEP(G, d, a, b, c, _mm_add_epi32(_mm_set1_epi32(ptr[7]) , val), 5)
  STEP(G, c, d, a, b, _mm_add_epi32(_mm_set1_epi32(ptr[11]) , val), 9)
  STEP(G, b, c, d, a, _mm_add_epi32(_mm_set1_epi32(ptr[15]) , val), 13)

  /* Round 3 */
  STEP(H, a, b, c, d, _mm_add_epi32(_mm_set1_epi32(ptr[0]) , valSecond), 3)
  STEP(H2, d, a, b, c, _mm_add_epi32(_mm_set1_epi32(ptr[8]) , valSecond), 9)
  STEP(H, c, d, a, b, _mm_add_epi32(_mm_set1_epi32(ptr[4]) , valSecond), 11)
  STEP(H2, b, c, d, a, _mm_add_epi32(_mm_set1_epi32(ptr[12]) , valSecond), 15)
  STEP(H, a, b, c, d, _mm_add_epi32(_mm_set1_epi32(ptr[2]) , valSecond), 3)
  STEP(H2, d, a, b, c, _mm_add_epi32(_mm_set1_epi32(ptr[10]) , valSecond), 9)
  STEP(H, c, d, a, b, _mm_add_epi32(_mm_set1_epi32(ptr[6]) , valSecond), 11)
  STEP(H2, b, c, d, a, _mm_add_epi32(_mm_set1_epi32(ptr[14]) , valSecond), 15)
  STEP(H, a, b, c, d, _mm_add_epi32(_mm_set1_epi32(ptr[1]) , valSecond), 3)
  STEP(H2, d, a, b, c, _mm_add_epi32(_mm_set1_epi32(ptr[9]) , valSecond), 9)
  STEP(H, c, d, a, b, _mm_add_epi32(_mm_set1_epi32(ptr[5]) , valSecond), 11)
  STEP(H2, b, c, d, a, _mm_add_epi32(_mm_set1_epi32(ptr[13]) , valSecond), 15)
  STEP(H, a, b, c, d, _mm_add_epi32(_mm_set1_epi32(ptr[3]) , valSecond), 3)
  STEP(H2, d, a, b, c, _mm_add_epi32(_mm_set1_epi32(ptr[11]) , valSecond), 9)
  STEP(H, c, d, a, b, _mm_add_epi32(_mm_set1_epi32(ptr[7]) , valSecond), 11)
  STEP(H2, b, c, d, a, _mm_add_epi32(_mm_set1_epi32(ptr[15]) , valSecond), 15)

  a += 0x67452301;
  b += 0xefcdab89;
  c += 0x98badcfe;
  d += 0x10325476;
  res[0] = a;
  res[1] = b;
  res[2] = c;
  res[3] = d;

  __m128i is_same = _mm_cmpeq_epi32(_mm_set1_epi32(ptr), _mm_set1_epi32(target));
  printf("V_mm_set1_epi32(alues): %d, %d, %d, %d\n", is_same[0], is_same[1], is_same[2], is_same[3]);


}

int main(int argc, char **argv)
{
  if (argc != 2)
  {
    fprintf(stderr, "Usage: %s HASH\n", argv[0]);
    return -1;
  }
  unsigned char *target = parse_hash(argv[1]);

  /*
    Candidate become buffer
  */
  unsigned char *candidates = (unsigned char *)malloc(sizeof(char) * 256); // max 7 char
                                       // only the char afer ! and char minuscule


  // init unitary candidate
  unsigned char *unitary_candidate_buffer = (unsigned char *)malloc(sizeof(char) * PWD_LEN + 1);
  memset(unitary_candidate_buffer, '!', PWD_LEN + 1);
  unitary_candidate_buffer[PWD_LEN + 1] = 0x80;
  
  // init big buffer without candidate
  memset(candidates, 0x00, 256);

  for(int i = 0; i < 4; i++){
    candidates[56*4 + i*4] = PWD_LEN;
  }


  //printf("\n\n%02x\n\n", candidate[0]);
  //candidate[PWD_LEN] = 0x80;
  //candidate[56] = PWD_LEN * 8;

  printf("___candidtate__\n");
  /*
  for (int i = 0; i < 64; i++)
  {
    printf("%x", candidate[i]);
  }
  */
  printf("_____\n");

  size_t tested = 0;
  struct timeval tval;
  double start;
  double now;

  gettimeofday(&tval, NULL);
  start = tval.tv_sec + tval.tv_usec / 1000000.0;

/*
  for(int i = 0; i < 256; i++){
    printf("%02x", candidates[i]);
    if((i+1)%16 == 0) {
      printf("\n");
    }
  }

*/
  
  do
  {

    // set candidates
    for(int i = 0; i < 4; i++){
      for(int idx = 0; idx < 4; idx++){
        candidates[(idx + (i*4))] = unitary_candidate_buffer[idx];
        candidates[(idx + (i*4)) + 16] = unitary_candidate_buffer[idx + 4];
      }

      incr_candidate(unitary_candidate_buffer);
    }




    // MD4_CTX ctx;
    //    return 1;
    unsigned char res[16];

    my_body(candidates, res, target);
    /*
       MD4_Init(&ctx); // init a context, in update, their is lo and hi,
       MD4_Update(&ctx, candidate, PWD_LEN);
       MD4_Final(res, &ctx); // should be simplified to one function call.

    */

    //   return 1;
    tested++;
    if (memcmp(res, target, 16) == 0)
    {
      printf("found: %s, after %ld tries\n", candidates, tested);
      return 0;
    }
    if (tested % (1024 * 1024 * 32) == 0)
    {
      gettimeofday(&tval, NULL);
      now = tval.tv_sec + tval.tv_usec / 1000000.0;
      double speed = tested / (now - start);
      fprintf(stderr, "%.3f M/s\n", speed / 1000000.0);
    }
  } while (incr_candidate(candidates));
  printf("not found after %ld tries\n", tested);
  return 1;
}
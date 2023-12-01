#define PWD_LEN 7

/*
 * The MD4 transformation for all three rounds.
 */
#define STEP(f, a, b, c, d, x, s)                                              \
  (a) += f((b), (c), (d)) + (x);                                               \
  (a) = (((a) << (s)) | (((a) & 0xffffffff) >> (32 - (s))));

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
#define SET(n) (*(MD4_u32plus *)&ptr[(n) * 4])
#define GET(n) SET(n)
#else
#define SET(n) (ptr[n])
#define GET(n) (ptr[n])
#endif

int get_32_combi(int c) {
  if (c < 26)
    return c + 'a';
  return c - 26 + '!';
}

void my_copy(char *candidate, char *solution) {
  for (int i = 0; i < PWD_LEN; i++) {
    solution[i] = candidate[i];
  }
  return;
}
int md4_comp(char *str1, char *str2) {
  for (int i = 0; i < 16; i++) {
    if (str1[i] != str2[i]) {
      return -1;
    }
  }
  return 0;
}

int incr_candidate(char *ptr) {
  int pos = PWD_LEN - 1;
  while (1) {
    if (pos < 3) {
      return 0;
    }
    char c = ++ptr[pos];
    if (c == '\'') {
      ptr[pos] = 'a';
      return 1;
    }
    if (c <= '&')
      return 1;
    if (c > 'z') {
      ptr[pos] = '!';
      pos--;
    } else {
      return 1;
    }
  }
}

void my_body(unsigned char *candidate, unsigned int *res) {
  int a, b, c, d;

  a = 0x67452301;
  b = 0xefcdab89;
  c = 0x98badcfe;
  d = 0x10325476;

  int *ptr = candidate;

  STEP(F, a, b, c, d, SET(0), 3)
  STEP(F, d, a, b, c, SET(1), 7)
  STEP(F, c, d, a, b, SET(2), 11)
  STEP(F, b, c, d, a, SET(3), 19)
  STEP(F, a, b, c, d, SET(4), 3)
  STEP(F, d, a, b, c, SET(5), 7)
  STEP(F, c, d, a, b, SET(6), 11)
  STEP(F, b, c, d, a, SET(7), 19)
  STEP(F, a, b, c, d, SET(8), 3)
  STEP(F, d, a, b, c, SET(9), 7)
  STEP(F, c, d, a, b, SET(10), 11)
  STEP(F, b, c, d, a, SET(11), 19)
  STEP(F, a, b, c, d, SET(12), 3)
  STEP(F, d, a, b, c, SET(13), 7)
  STEP(F, c, d, a, b, SET(14), 11)
  STEP(F, b, c, d, a, SET(15), 19)

  /* Round 2 */
  STEP(G, a, b, c, d, GET(0) + 0x5a827999, 3)
  STEP(G, d, a, b, c, GET(4) + 0x5a827999, 5)
  STEP(G, c, d, a, b, GET(8) + 0x5a827999, 9)
  STEP(G, b, c, d, a, GET(12) + 0x5a827999, 13)
  STEP(G, a, b, c, d, GET(1) + 0x5a827999, 3)
  STEP(G, d, a, b, c, GET(5) + 0x5a827999, 5)
  STEP(G, c, d, a, b, GET(9) + 0x5a827999, 9)
  STEP(G, b, c, d, a, GET(13) + 0x5a827999, 13)
  STEP(G, a, b, c, d, GET(2) + 0x5a827999, 3)
  STEP(G, d, a, b, c, GET(6) + 0x5a827999, 5)
  STEP(G, c, d, a, b, GET(10) + 0x5a827999, 9)
  STEP(G, b, c, d, a, GET(14) + 0x5a827999, 13)
  STEP(G, a, b, c, d, GET(3) + 0x5a827999, 3)
  STEP(G, d, a, b, c, GET(7) + 0x5a827999, 5)
  STEP(G, c, d, a, b, GET(11) + 0x5a827999, 9)
  STEP(G, b, c, d, a, GET(15) + 0x5a827999, 13)

  /* Round 3 */
  STEP(H, a, b, c, d, GET(0) + 0x6ed9eba1, 3)
  STEP(H2, d, a, b, c, GET(8) + 0x6ed9eba1, 9)
  STEP(H, c, d, a, b, GET(4) + 0x6ed9eba1, 11)
  STEP(H2, b, c, d, a, GET(12) + 0x6ed9eba1, 15)
  STEP(H, a, b, c, d, GET(2) + 0x6ed9eba1, 3)
  STEP(H2, d, a, b, c, GET(10) + 0x6ed9eba1, 9)
  STEP(H, c, d, a, b, GET(6) + 0x6ed9eba1, 11)
  STEP(H2, b, c, d, a, GET(14) + 0x6ed9eba1, 15)
  STEP(H, a, b, c, d, GET(1) + 0x6ed9eba1, 3)
  STEP(H2, d, a, b, c, GET(9) + 0x6ed9eba1, 9)
  STEP(H, c, d, a, b, GET(5) + 0x6ed9eba1, 11)
  STEP(H2, b, c, d, a, GET(13) + 0x6ed9eba1, 15)
  STEP(H, a, b, c, d, GET(3) + 0x6ed9eba1, 3)
  STEP(H2, d, a, b, c, GET(11) + 0x6ed9eba1, 9)
  STEP(H, c, d, a, b, GET(7) + 0x6ed9eba1, 11)
  STEP(H2, b, c, d, a, GET(15) + 0x6ed9eba1, 15)
  a += 0x67452301;
  b += 0xefcdab89;
  c += 0x98badcfe;
  d += 0x10325476;
  res[0] = a;
  res[1] = b;
  res[2] = c;
  res[3] = d;
}

__kernel void md4_crack(__global const unsigned int *target,
                        __global unsigned char *solution) {

  // Get the index of the current element to be processed
  int step_counter = 0;

  int id = get_global_id(0);

  // printf("\n START %d\n", step_counter);step_counter++;

  // prepare buffer
  unsigned char candidate[64];
  //      printf("\n START %d\n", step_counter);step_counter++;

  candidate[0] = id % 26 + 'a'; // get reste
  int tmp = id / 26;            // get quotient
  candidate[1] = tmp % 26 + 'a';
  tmp = tmp / 26;
  candidate[2] = get_32_combi(tmp % 32);
  //    printf("\n START %d\n", step_counter);step_counter++;

  // put unknow char of password
  for (int i = 3; i < PWD_LEN; i++) {
    candidate[i] = '!';
  }
  //  printf("\n START %d\n", step_counter);step_counter++;

  candidate[PWD_LEN] = 0x80;
  for (int i = 63; i > PWD_LEN; i--) {
    candidate[i] = 0x00;
  }
  candidate[56] = PWD_LEN * 8;
  // printf("\n START %d\n", step_counter);step_counter++;

  // printf("\n START %d\n", step_counter);step_counter++;

  //         printf("\n START %d\n", step_counter);step_counter++;

  // printf("\n");

  // printf("\ntest\n");

  // printf("\n%x\n", *target);

  // printf("\n%02x\n", solution[0]);
  do {

    // MD4_CTX ctx;
    //    return 1;
    unsigned char res[16];

    my_body(candidate, res);
    /*
      MD4_Init(&ctx); // init a context, in update, their is lo and hi,
      MD4_Update(&ctx, candidate, PWD_LEN);
      MD4_Final(res, &ctx); // should be simplified to one function call.

    */

    //   return 1;
    if (md4_comp(res, target) == 0) {
      my_copy(candidate, solution);
      printf("\nfound: %s tries\n", candidate);
      return;
    }

  } while (incr_candidate(candidate));

  return;
}


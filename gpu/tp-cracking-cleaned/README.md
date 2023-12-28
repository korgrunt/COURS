# GPU FOR PASS CRACKING

## for build you can use make commande.

```
$> make
```

## Report about the gpu exercices:

I've keep the programme in the version i've done on your gcp instance.
for gpu 

```
$> ./target/gpu ./gpu-opencl/vector_md4_kernel.cl 752f4adfe53d1da0241b5bc216d098fc
```
should find abcdefg

## Report about the simple exercices:

for mono thread cpu, i've try to remove some step, i've no found a way for remove step and keep a working program 

```
$> ./target/simple 83dc2dcea4070eeb926f218ea7ee1fa9
```
should find mamans

## Report about the simd exercices:

Simd doesn't work. I've understand the simd concept of use one register with multi data and process them for make paralléle opération on one thread,
i've not successful compared the hash generated in body with target.

```
/*
Not working, i've only made the candidates buffer as columns in 256 byte, process them in body with simd intel function, incrémente candidates, missed some time for made it work with comparaison. 
*/
// $> ./target/simd 83dc2dcea4070eeb926f218ea7ee1fa9
```

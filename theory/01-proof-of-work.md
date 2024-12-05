# Proof of Work

What is this? Why Bitcoin is safe?

Proof of work is what a *miner* does!

Anybody can send money by broadcasting a transaction to the network

Miners compete against each other for the privilege of *building* on the chain.

Nakamoto mined the first bitcoin. [First transaction](https://blockstream.info/block/000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f)

```echo $scriptSigHex | xxd -r -p```

After validating a block, the miner should generate a *valid hash*

This hash needs to satisfy the network *target*, that's  it,
the hash needs to be numerically less than the target

so the smaller the target the harder it gets!

Calculating a SHA256 is computationally expensive!

Brute force only


## Running proof-of-work.go:
- With target = 2^250:
  - ~276 µs
- With target = 2^245:
  - ~710 µs
- With target = 2^240:
  - ~94 ms
- With target = 2^235:
  - ~5 s
- With target = 2^230:
  - ???

# Proof of Work

What is this? Why Bitcoin is safe?

Proof of work is what a *miner* does!

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

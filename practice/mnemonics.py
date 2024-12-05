import bip32utils
from mnemonic import Mnemonic

# Step 1: Generate a mnemonic (seed phrase)
mnemo = Mnemonic("portuguese")
mnemonic_phrase = mnemo.generate(strength=256)  # You can use 128, 160, 192, 224, or 256 bits

print(f"Generated Mnemonic: {mnemonic_phrase}")

# Step 2: Convert the mnemonic to a seed
seed = mnemo.to_seed(mnemonic_phrase, passphrase="")  # Optional passphrase

# Step 3: Generate a BIP32 master key from the seed
master_key = bip32utils.BIP32Key.fromEntropy(seed)

# Step 4: Derive the private key (typically from m/44'/0'/0'/0 index 0 path)
private_key = master_key.ChildKey(0).ChildKey(0).PrivateKey()

# Print the private key in hex format
print(f"Private Key: {private_key.hex()}")

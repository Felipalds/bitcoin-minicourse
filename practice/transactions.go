package main

import (
	"crypto/ecdsa"
	"crypto/elliptic"
	"crypto/rand"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"log"
	"math/big"
)

type Transaction struct {
	Sender    string
	Receiver  string
	Amount    float64
	Signature []byte
}

func GenerateKeys() (*ecdsa.PrivateKey, *ecdsa.PublicKey) {
	privateKey, err := ecdsa.GenerateKey(elliptic.P256(), rand.Reader)
	if err != nil {
		log.Fatalf("Failed to generate keys: %v", err)
	}

	return privateKey, &privateKey.PublicKey
}

// this function will generate a hash sha256 for the transaction
// similar as we saw in proof-of-work.go
func (tx *Transaction) Hash() string {
	data := fmt.Sprintf("%s%s%f", tx.Sender, tx.Receiver, tx.Amount)
	hash := sha256.Sum256([]byte(data))
	return hex.EncodeToString(hash[:])
}

func (tx *Transaction) SignTransaction(privateKey *ecdsa.PrivateKey) {
	hash := tx.Hash()
	r, s, err := ecdsa.Sign(rand.Reader, privateKey, []byte(hash))
	if err != nil {
		log.Fatalf("Failed to sign transaction %v", err)
	}

	tx.Signature = append(r.Bytes(), s.Bytes()...)
}

func (tx *Transaction) VerifySignature(publicKey *ecdsa.PublicKey) bool {
	hash := tx.Hash()

	r := new(big.Int).SetBytes(tx.Signature[:len(tx.Signature)/2])
	s := new(big.Int).SetBytes(tx.Signature[len(tx.Signature)/2:])

	return ecdsa.Verify(publicKey, []byte(hash), r, s)
}

func main() {

	privateKey, publicKey := GenerateKeys()

	tx := &Transaction{
		Sender:   "Alice",
		Receiver: "Bob",
		Amount:   10.5,
	}

	// fmt.Println("Transaction Details:")
	// fmt.Printf("Sender: %s\nReceiver: %s\nAmount: %.2f\n", tx.Sender, tx.Receiver, tx.Amount)

	tx.SignTransaction(privateKey)

	// fmt.Printf("Transaction Hash: %s\n", tx.Hash())
	// fmt.Printf("Signature: %x\n", tx.Signature)

	// Verify the signature
	isValid := tx.VerifySignature(publicKey)

	if isValid {
		fmt.Println(tx.Hash())
	} else {
		fmt.Println("Signature verification failed.")
	}

}

package main

import (
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"strings"
	"time"
)

// this code will show you how Proof of Work... works LOL

type Block struct {
	Data      string
	Target    int
	Nonce     int
	Hash      string
	Timestamp time.Time
}

func calculateHash(data string, nonce int) string {
	input := fmt.Sprintf("%s%d", data, nonce)
	hash := sha256.Sum256([]byte(input))
	return hex.EncodeToString(hash[:])
}

// in golang, this is like a method
func (pow *Block) mine() {
	targetPrefix := strings.Repeat("0", pow.Target)
	for {
		pow.Hash = calculateHash(pow.Data, pow.Nonce)
		if strings.HasPrefix(pow.Hash, targetPrefix) { // we found!
			break
		}
		pow.Nonce++
	}
	pow.Timestamp = time.Now()
}

func main() {

	data := "Hello, Unioeste!"
	target := 8

	pow := Block{Data: data, Target: target}
	start := time.Now()

	pow.mine()

	duration := time.Since(start)

	fmt.Println("Completed mining")
	fmt.Printf("Data: %s\nNonce: %d\nHash: %s\nTime Taken: %s\n", pow.Data, pow.Nonce, pow.Hash, duration)

}

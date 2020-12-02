package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func main() {
	var balance []int
	target := 2020
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		// fmt.Println(scanner.Text())
		var tmp int
		tmp, err = strconv.Atoi(scanner.Text())
		balance = append(balance, tmp)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	twoNumbers(balance, target)
	threeNumbers(balance, target)
}

func twoNumbers(input []int, target int) {
	fmt.Printf("Searching for 2 numbers adding to %d\n\n", target)
	for count := 0; count < len(input); count++ {
		for second := count + 1; second < len(input); second++ {
			if input[count]+input[second] == target {
				fmt.Printf("First Index is %d, value is %d\n", count, input[count])
				fmt.Printf("Second Index is %d, value is %d\n", second, input[second])
				output := input[count] * input[second]
				fmt.Printf("Answer is %d\n", output)
				break
			}
		}
	}
}

func threeNumbers(input []int, target int) {
	fmt.Printf("\nSearching for 3 numbers adding up to %d\n\n", target)
	for count := 0; count < len(input); count++ {
		var output int
		var summation int
		for second := count + 1; second < len(input); second++ {
			for third := second + 1; third < len(input); third++ {
				summation = input[count] + input[second] + input[third]
				if summation == target {
					fmt.Printf("First index is %d, value is %d\n", count, input[count])
					fmt.Printf("Second index is %d, value is %d\n", second, input[second])
					fmt.Printf("Third index is %d, value is %d\n", third, input[third])
					output = input[count] * input[second] * input[third]
					fmt.Printf("Answer is %d\n", output)
					break
				}
			}
			if summation == target {
				break
			}
		}
		if summation == target {
			break
		}
	}
}

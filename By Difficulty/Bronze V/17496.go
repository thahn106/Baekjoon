package main
import "fmt"

func main() {
  var N,T,C,P int32
  fmt.Scan(&N, &T, &C, &P)
  fmt.Println(((N-1)/T)*C*P)
}

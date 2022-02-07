package main
import "fmt"

func main() {
  var N1,N2,N12 int32
  fmt.Scan(&N1,&N2,&N12)
  fmt.Println( (N1+1)*(N2+1)/(N12+1) - 1)
}

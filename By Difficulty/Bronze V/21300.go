package main
import "fmt"

func main() {
  s := 0
  i := 0
  for (i<6) {
    var input int
    fmt.Scanf("%d", &input)
    s+=input
    i+=1
  }
  fmt.Println(5*s)
}

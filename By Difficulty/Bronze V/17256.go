package main
import "fmt"

func main() {
  var ax, ay, az, cx, cy, cz int32
  fmt.Scan(&ax, &ay, &az)
  fmt.Scan(&cx, &cy, &cz)
  fmt.Println(cx-az, cy/ay, cz-ax)
}

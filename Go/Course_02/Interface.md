## Polymorphism
* ability for an object to have different "forms" depending on the context
```
rectangle, area = base * height
triangle, area = 0.5 * base * height
```
## Defining an interface type
```go 
type Shape2D interface{
    Area() float64
    Perimeter() float64
}
type Triangle {...}
func (t Triangle) Area() float64 {...}
func (t Triangle) Perimeter() float64 {...}
```
* Triangle type satisfies the Shape2D interface
* No need to state it explicitly

## Interface Values
1. Can be treated like other values
* Assigned to variables
* Passed, returned
2. Interface values have two components
* dynamic type
* dynamic value
```go
type Speaker interface {Speak()}
type Dog struct {name string}
func (d Dog) Speak() {
    fmt.Println(d.name)
}
func main(){
    var s1 Speaker
    var d1 Dog("Biran")
    s1=d1
    s1.Speak()
}
// Dynamic type is Dog, Dynamic value is d1
```

## Interface with Nil Dynamic Value
```go
var s1 Speaker
var d1 *Dog
s1=d1
s1.Speak()
// s1.Speak() is still legal because s1 know its dynamic type it can call Dog Speak mechod. But Speak need do some changes
func (d *Dog) Speak(){
    if d == nil{
        fmt.Println("noise")
    }else{
        fmt.Println(d.name)
    }
}
```

## Using interfaces as parameter
```go
type Shape2D interface{
    Area() float64
    Perimeter() float()
}

type Triangle{...}
func (t Triangle) Area() float64{...}
func (t Triangle) Perimeter() float64{...}

type Rectangle{...}
func (t Rectangle) Area() float64{...}
func (t Rectangle) Perimeter() float64{...}
// Rectangle and Triangle satisfy the Shape2D interface

func FitInYard(s Shape2D) bool{
    if (s.Area() > 100 && s.perimeter() > 100){
        return true
    }
    return false
}
// Parameter is any type that satisfies the interface
```

## Empty Interface
* Empty interface psecifies no methods
* All types satisfy the empty interface
* Use it to have a function accept any type as a prameter
```go
func Printme(val interface{}){
	fmt.Print(val)
}
func main() {
    x:=X{Name:"wo",Age:123,Gender:"cao"}
	Printme(x)
    // {wo 123 cao}
    Printme(1)
    //1
    Printme("ri")
    //ri
}
```

## Type Assertions for Disambiguation
```go
func DrawShape(s Shape2D) bool{
    rect, ok := s.(Rectangle)
    if ok {
        DrawRect(rect)
    }
    tri, ok: = s.(Triagnle)
    if ok{
        DrawRect(tri)
    }
}
```

## Type Switch
```go
func DrawShape(s Shape2D) bool{
    switch sh := s.(type) {
        case Rectangle:
            DrawRect(sh)
        case Triangle:
            DrawTriangle(sh)
        default:
            fmt.Println("unknown")
        }
}
```

## Reflection
```go
import reflect
var x interface{} = []int{1,2,3}
xType := reflect.TypeOf(x)
xValue:= reflect.ValueOf(x)
fmt.Println(xType, xValue)
```
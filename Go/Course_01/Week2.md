Pointer<br>
1. & returns the address of a variable/function
2. \* returns data at an address
```go
var x int=1
var y
var ip *int

ip = &x
y = *ip
```

New<br>
new() function creates a variable and returns a pointer to the variable
```go
ptr := new(int)
*ptr = 3
```

Comments
```go
//
/* */
```

Boolean Operator
```go
a && b
a || b
!a
```

Type Conversions
```go
var x int32 = 1
var y int16 = 2

x = int32(y)
```

Floating Point
```go
float32 // ~6 digits of precision
float64 // ~15 digits of precision

var x float64 = 1.2345e2
var y float64 = 1.2345
```

Unicode<br>
1. Unicode is a 32-bit character code
2. UTF-8 is variable length, could be 8bit, 16bit or 32 bit
3. Code points - Unicode characters A:0x41
4. Rune - a code point in go

Strings
```go
x := "Hi There" // double quotes
// Each byte is a rune (UTF-8 code point)
```

Unicode Package
```go
IsDigit(r rune)
IsSpace(r rune)
IsLetter(r rune)
IsLower(r rune)
IsPunct(r rune)

ToUpper(r rune)
ToLower(r rune)
```

Strings Package
```go
Compare(a, b) // returns 0 if a==b, -1 a<b ,1 a>b
Contains(s, substr) // returns true or false
HasPrefix(s, prefix) // returns true or false
Index(s, substr) // returns the index of the first instance of substr in s
```

String Manipulation
```go 
Replace(s, old, new, n) // returns a copy of the string s with the first
// n instances of old replaceed by new
ToLower(s)
ToUpper(s)
TrimSpace(s) // returns a new string with all leading and trailing white space removed
```

Strconv Package
```go
Atoi(s) // converts string s to int
Itoa(i) // converts int(base10) to string

FormatFloat(f, fmt, prec, bitSize) // converts floating point number to a string
// f: floating number, fmt: format(b,e,E,f,g,G), prec: 精度, bitSize: 32-float32 64-float64
ParseFloat(s, bitsize) //string-> floating number
```

Constants
```go
const x=1.3
const (
    y=4
    z="Hi"
)
```

iota similar with enumerate
* It is constants that must be different but actual value is not important
```go
type Grades int
const (
    A Grades = iota
    B
    C
    D
    E
    F
)
// each constans is assigned to a unique integer
// Starts at 1 and increaments
```

Switch/Case
```go
switch x {
    case 1:
        fmt.Printf("case1")
    case 2:
        fmt.Printf("case2")
    default: 
        fmt.Printf("case default")
}
```
Tagless Switch
```go
swithc {
    case x > 1:
        fmt.Printf("case1")
    case x < 1:
        fmt.Printf("case2")
    defalut:
        fmt.Printf("case default")
}
```

Scan
```go
var appleNum int

fmt.Printf("number fo apples?")
num, err:= fmt.Scan(&appleNum)
// Scan takes a pointer as an argument, returns number of scanned items and error
fmt.Printf(appleNum)
```
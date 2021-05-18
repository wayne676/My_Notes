python interpreter 用来管理内存 和 garbage collection 
interpreted language like python, 每次跑程序都要把python代码翻译成机器码 因为是一边跑
一边翻译 所以 可以不用声明变量类型 而是在跑的时候自己推断 

compiled language translate once saves time but 内存管理不能 那么为啥java可以用garbage collection
因为java的garbage collection 发生在 jvm 类似于 interpretor

go在编译时候直接把 garbage collection compile到你的代码中 所以 this is a compiled language that actually has
garbage collection (typically only done by interpretor)

Go Tool Command
```go
go build
go doc // prints documentation for a package
go fmt // formats scource code files
go get // download pakcages and install them
go list // list all installed pakcages
go run
```

Variable </br>
```go
var x int
// keyword name type
```
Type Declarations
```go
// type alias
type Celsius float64
var temp Celsius

type IDnum int
var pid IDnum
```
Uninitialized Variables have a zero value
```go
var x int // x=0
var x string //x=""
```
Short Variable Declarations
```go
x := 100
// Can only do this inside a function
// you can't do a short variable declaration outside a function, that's not legal
```
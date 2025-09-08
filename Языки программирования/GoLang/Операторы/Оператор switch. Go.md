#Go 
### Описание
- Описание _switch_ используется для удобной проверки нескольких условий
	 Альтернатива для множества блоков _if...else if_
- Операторы switch выполняются сверху вниз
- Возможно наличие действия по умолчанию _(default)_, необязательно

### Базовый пример
```go
var x int = 3
switch x {
case 1:
	fmt.Println("1")
case 2:
	fmt.Println("2")
case 3:
	fmt.Println("3")
default:
	fmt.Println("other", x)
}

url := "example.com"
switch url {
case "example.com"
	fmt.Println("test")
case "google.com"
	fmt.Println("live")
default:
	fmt.Println("dev")
}
```

### Условные варианты
```go
switch rezsult := calculate(5); {
case result > 10:
	fmt.Println(result, ">10")
case result == 6:
	fmt.Println(result, "=6")
case result < 10:
	fmt.Println(result, "<10")
}
```

### Список вариантов
```go
switch x {
case 1, 2, 3:
	//...
case 10, 20, 30:
	//...
}
//благодаря этому, мы можем проверять сразу несколько вариантов. В примере можем увидеть, что если х равен какому-то из значений первого кейса, то выполнится именно это часть
```

### Падение (fallthrough)
- Ключевое слово _fallthrough_ позволяет продолжать проверку следующего варианта оператора _switch_ 
```go
package main

import "fmt"

func main() {
    num := 0
    switch num {
        case 0:
            fmt.Println("Case: 0")
        fallthrough 
		//В этом примере ключевое слово fallthrough передаёт             управление на первую строку блока case 1, поэтому              этот блок также выполняется
        case 1:
            fmt.Println("Case: 1")
        case 2:
            fmt.Println("Case: 2")
        default:
            fmt.Println("default")
    }
}


package main

import "fmt"

func main() {
    day := "Tue"
    switch {
        case day == "Mon":
            fmt.Println("Monday")
        fallthrough
        case day == "Tue":
            fmt.Println("Tuesday")
        fallthrough
        case day == "Wed":
            fmt.Println("Wednesday")
    }
}
//В этом примере ключевое слово fallthrough указывает на то, что следующий оператор case будет выполнен независимо от истинности своего условия
```

### Вывод 
- Оператор _switch_ может быть использован для удобной проверки переменной на различные значения
	 Используйте запятые, чтобы проверить несколько значений в одном варианте 
- Выражения допускается в качестве варианта
	 Вы можете использовать вызовы фкц, математические операции и логику внутри вариантов оператора _switch_
- Ключевое слово _fallthrough_ выполнит следующий вариант оператора _switch_
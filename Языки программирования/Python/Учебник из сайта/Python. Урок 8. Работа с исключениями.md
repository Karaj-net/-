Данный урок посвящен исключениям и работе с ними. Основное внимание уделено понятию исключения в языках программирования, обработке исключений в Python, их генерации и созданию пользовательских исключений.
#Уроки_Python 
# Исключения в языках программирования

Исключениями (_exceptions_) в языках программирования называют проблемы, возникающие в ходе выполнения программы, которые допускают возможность дальнейшей ее работы в рамках основного алгоритма. Типичным примером исключения является деление на ноль, невозможность считать данные из файла (устройства), отсутствие доступной памяти, доступ к закрытой области памяти и т.п. Для обработки таких ситуаций в языках программирования, как правило, предусматривается специальный механизм, который называется обработка исключений (_exception handling_).

Исключения разделяют на **синхронные** и **асинхронные**. **Синхронные** исключения могут возникнуть только в определенных местах программы. Например, если у вас есть код, который открывает файл и считывает из него данные, то исключение типа “ошибка чтения данных” может произойти только в указанном куске кода. **Асинхронные** исключения могут возникнуть в любой момент работы программы, они, как правило, связаны с какими-либо аппаратными проблемами, либо приходом данных. В качестве примера можно привести сигнал отключения питания.

В языках программирования чаще всего предусматривается специальный механизм обработки исключений. **Обработка** может быть **с** **возвратом**, когда после обработки исключения выполнение программы продолжается с того места, где оно возникло. И **обработка без возврата**, в этом случае, при возникновении исключения, осуществляется переход в специальный, заранее подготовленный, блок кода.

Различают **структурную** и **неструктурную** обработку исключений. **Неструктурная** обработка предполагает регистрацию функции обработчика для каждого исключения, соответственно данная функция будет вызвана при возникновении конкретного исключения. Для **структурной** обработки язык программирования должен поддерживать специальные синтаксические конструкции, которые позволяют выделить код, который необходимо контролировать и код, который нужно выполнить при возникновении исключительной ситуации.

# Ошибки и исключения в Python

В _Python_ выделяют два различных вида ошибок: синтаксические ошибки и исключения.

## Синтаксические ошибки в Python

Синтаксические ошибки возникают в случае если программа написана с нарушениями требований _Python_ к синтаксису. Определяются они в процессе парсинга программы. Ниже представлен пример с ошибочным написанием функции _print_.
```Python
for i in range(10):
    prin("hello!")

Traceback (most recent call last):
  File "<pyshell#2>", line 2, in <module>
    prin("hello!")
NameError: name 'prin' is not defined
```


## Исключения в Python

Второй вид ошибок – это исключения. Они возникают в случае если синтаксически программа корректна, но в процессе выполнения возникает ошибка (деление на ноль и т.п.). Более подробно про понятие исключения написано выше, в разделе “исключения в языках программирования”.

Пример исключения _ZeroDivisionError_, которое возникает при делении на 0.
```Python
a = 10
b = 0
c = a / b
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    c = a / b
ZeroDivisionError: division by zero
```


В _Python_ исключения являются определенным типом данных, через который пользователь (программист) получает информацию об ошибке. Если в коде программы исключение не обрабатывается, то приложение останавливается и в консоли печатается подробное описание произошедшей ошибки с указанием места в программе, где она произошла и тип этой ошибки.

# Иерархия исключений в Python

Существует довольно большое количество встроенных типов исключений в языке _Python_, все они составляют определенную иерархию, которая выглядит так, как показано ниже.
```
BaseException  
+– SystemExit  
+– KeyboardInterrupt  
+– GeneratorExit  
+– Exception  
     +– StopIteration  
     +– StopAsyncIteration  
     +– ArithmeticError  
     |    +– FloatingPointError  
     |    +– OverflowError  
     |    +– ZeroDivisionError  
     +– AssertionError  
     +– AttributeError  
     +– BufferError  
     +– EOFError  
     +– ImportError  
          +– ModuleNotFoundError  
     +– LookupError  
     |    +– IndexError  
     |    +– KeyError  
     +– MemoryError  
     +– NameError  
     |    +– UnboundLocalError  
     +– OSError  
     |    +– BlockingIOError  
     |    +– ChildProcessError  
     |    +– ConnectionError  
     |    |    +– BrokenPipeError  
     |    |    +– ConnectionAbortedError  
     |    |    +– ConnectionRefusedError  
     |    |    +– ConnectionResetError  
     |    +– FileExistsError  
     |    +– FileNotFoundError  
     |    +– InterruptedError  
     |    +– IsADirectoryError  
     |    +– NotADirectoryError  
     |    +– PermissionError  
     |    +– ProcessLookupError  
     |    +– TimeoutError  
     +– ReferenceError  
     +– RuntimeError  
     |    +– NotImplementedError  
     |    +– RecursionError  
     +– SyntaxError  
     |    +– IndentationError  
     |         +– TabError  
     +– SystemError  
     +– TypeError  
     +– ValueError  
     |    +– UnicodeError  
     |         +– UnicodeDecodeError  
     |         +– UnicodeEncodeError  
     |         +– UnicodeTranslateError  
     +– Warning  
          +– DeprecationWarning  
          +– PendingDeprecationWarning  
          +– RuntimeWarning  
          +– SyntaxWarning  
          +– UserWarning  
          +– FutureWarning  
          +– ImportWarning  
          +– UnicodeWarning  
          +– BytesWarning  
          +– ResourceWarning

```

Как видно из приведенной выше схемы, все исключения являются подклассом исключения _BaseException_. Более подробно об иерархии исключений и их описании можете прочитать [здесь](https://docs.python.org/3/library/exceptions.html#bltin-exceptions).
# Обработка исключений в Python

Обработка исключений нужна для того, чтобы приложение не завершалось аварийно каждый раз, когда возникает исключение. Для этого блок кода, в котором возможно появление исключительной ситуации необходимо поместить во внутрь синтаксической конструкции _try…except_.
```Python
print("start")
try:
   val = int(input("input number: "))
   tmp = 10 / val
   print(tmp)
except Exception as e:
   print("Error! " + str(e))
print("stop")
```


В приведенной выше программе возможных два вида исключений – это _ValueError_, возникающее в случае, если на запрос программы “введите число”, вы введете строку, и _ZeroDivisionError_ – если вы введете в качестве числа 0.

Вывод программы при вводе нулевого числа будет таким.

**start input number: 0 Error! stop**

Если бы инструкций _try…except_ не было, то при выбросе любого из исключений программа аварийно завершится.
```Python
print("start")
val = int(input(“input number: “))
tmp = 10 / val
print(tmp)
print("stop")
```


Если ввести 0 на запрос приведенной выше программы, произойдет ее остановка с распечаткой сообщения об исключении.

> [!NOTE] Title
> **start**
> **input number: 0**
> **Traceback (most recent call last):**
> **File “F:/work/programming/python/devpractice/tmp.py”, line 3, in `<module>`**
>    **tmp = 10 / val**
>    **ZeroDivisionError: division by zero**


Обратите внимание, надпись _stop_ уже не печатается в конце вывода программы.

Согласно документу по языку _Python_, описывающему ошибки и исключения, оператор _try_ работает [следующим образом](https://docs.python.org/3/tutorial/errors.html):

- Вначале выполняется код, находящийся между операторами _try_ и _except._
- Если в ходе его выполнения исключения не произошло, то код в блоке _except_ пропускается, а код в блоке _try_ выполняется весь до конца.
- Если исключение происходит, то выполнение в рамках блока _try_ прерывается и выполняется код в блоке _except_. При этом для оператора _except_ можно указать, какие исключения можно обрабатывать в нем. При возникновении исключения, ищется именно тот блок _except_, который может обработать данное исключение.
- Если среди _except_ блоков нет подходящего для обработки исключения, то оно передается наружу из блока _try_. В случае, если обработчик исключения так и не будет найден, то исключение будет необработанным (_unhandled exception_) и программа аварийно остановится.

Для указания набора исключений, который должен обрабатывать данный блок _except_ их необходимо перечислить в скобках (круглых) через запятую после оператора _except_.

Если бы мы в нашей программе хотели обрабатывать только _ValueError_ и _ZeroDivisionError_, то программа выглядела бы так.
```Python
print("start")
try:
   val = int(input("input number: "))
   tmp = 10 / val
   print(tmp)
except(ValueError, ZeroDivisionError):
   print("Error!")
print("stop")
```


Или так, если хотим обрабатывать _ValueError_, _ZeroDivisionError_ по отдельность, и, при этом, сохранить работоспособность при возникновении исключений отличных от вышеперечисленных.
```Python
print("start")
try:
   val = int(input("input number: "))
   tmp = 10 / val
   print(tmp)
except ValueError:
   print("ValueError!")
except ZeroDivisionError:
   print("ZeroDivisionError!")
except:
   print("Error!")
print("stop")
```


Существует возможность передать подробную информацию о произошедшем исключении в код внутри блока _except_.
```Python
rint("start")
try:
   val = int(input("input number: "))
   tmp = 10 / val
   print(tmp)
except ValueError as ve:
   print("ValueError! {0}".format(ve))
except ZeroDivisionError as zde:
   print("ZeroDivisionError! {0}".format(zde))
except Exception as ex:
   print("Error! {0}".format(ex))
print("stop")
```


# Использование finally в обработке исключений

Для выполнения определенного программного кода при выходе из блока _try/except_, используйте оператор _finally_.
```Python
try:
   val = int(input("input number: "))
   tmp = 10 / val
   print(tmp)
except:
   print("Exception")
finally:
  print("Finally code")
```


Не зависимо от того, возникнет или нет во время выполнения кода в блоке _try_ исключение, код в блоке _finally_ все равно будет выполнен.

Если необходимо выполнить какой-то программный код, в случае если в процессе выполнения блока _try_ не возникло исключений, то можно использовать оператор _else_.
```Python
try:
   f = open("tmp.txt", "r")
   for line in f:
       print(line)
   f.close()
except Exception as e:
   print(e)
else:
   print("File was readed")
```


# Генерация исключений в Python

Для принудительной генерации исключения используется инструкция _raise_.

Самый простой пример работы с _raise_ может выглядеть так.
```Python
try:
   raise Exception("Some exception")
except Exception as e:
   print("Exception exception " + str(e))
```


Таким образом, можно “вручную” вызывать исключения при необходимости.

# Пользовательские исключения (User-defined Exceptions) в Python

В _Python_ можно создавать собственные исключения. Такая практика позволяет увеличить гибкость процесса обработки ошибок в рамках той предметной области, для которой написана ваша программа.

Для реализации собственного типа исключения необходимо создать класс, являющийся наследником от одного из классов исключений.
```Python
class NegValException(Exception):
   pass

try:
   val = int(input("input positive number: "))
   if val < 0:
       raise NegValException("Neg val: " + str(val))
   print(val + 10)
except NegValException as e:
  print(e)

[^1]: zdbfzdfb
	
```


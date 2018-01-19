# tilde-ath 

[![build status](https://api.travis-ci.org/PaulkaToast/tilde-ath.svg?branch=master)](https://travis-ci.org/PaulkaToast/tilde-ath)
[![Coverage Status](https://coveralls.io/repos/github/PaulkaToast/tilde-ath/badge.svg?branch=master)](https://coveralls.io/github/PaulkaToast/tilde-ath?branch=master)


Interpreter for the ~ATH programming language from homestuck 

# Installation Instructions
```
pip install -r requirements.txt
```

# Testing Instructions
```
python -m pytest

// with coverage
python -m pytest -v --cov ath --cov-report term-missing
```

# Examples

## Printing
C
```c
printf("hello, world!\n");
```

~ATH
```
> hello, world!\n ==> ;
```

## Variable Declaration
C
```c
int var = 5;
string var = "hello";
```

~ATH
```
var = 5;
var = >hello=;
```

## Function Declaration
C
```c
int func() {
	return 0;
}
```

~ATH
```
ACT func() {
	APPEARIFY 0;
}
```

## Arithmetic Operators
C
```c
x = a + b;
x = a - b;
x = a * b;
x = a / b;
x = a % b;
```

~ATH
```
x = ADDIFY(a,b);
x = SUBIFY(a,b);
x = REPLICATE(a,b);
x = DIMINISH(a,b);
x = RESIDUE(a,b);
```

## Relational Operators
C
```c
x = a == b;
x = a != b;
x = a > b;
x = a < b;
x = a >= b;
x = a <= b;
```

~ATH
```
x = a == b;
x = a != b;
x = a > b;
x = a < b;
x = a >= b;
x = a <= b;
```
## Logical Operators
C 
```c
x = a && b;
x = a || b;
x = !x; 
```

~ATH
```
x = a && b;
x = a || b;
x = !x;
```

## Loops
C
```c
for( ; ; ) {
      printf("This loop will run forever.\n");
}
```

~ATH
```
u1 = ALIVE;
u1.lifespan = HE_IS_ALREADY_HERE;

~ATH(u1) {
	> This loop will run forever.\n ==> ;
}EXECUTE(NULL);
```

python
```python
for x in range(0, 3):
	print("counter is:" + str(x))
```

~ATH
```
u1 = ALIVE;
u1.lifespan = 3;
u1.age = 0;

~ATH(u1) {
	>counter is:$(u1.age) ==> ;
}EXECUTE(NULL);
THIS.DIE();
```

## If Statements
python
```python
if x < 50:
	//code
```

~ATH
```
u1 = ALIVE;
u1.DIE_UNLESS(x < 50);

~ATH(u1) {
       	//code
	U1.DIE();
}EXECUTE(NULL);
THIS.DIE();
```

python
```python
u1 = true

if u1:
	//code
else:
	//code2
```

~ATH
```
u1 = ALIVE;
u1.lifespan = HE_IS_ALREADY_HERE;
u1.age = 0;

~ATH(u1) {
	//code
	u1.DIE();
}EXECUTE(u1.REVIVE());
~ATH(!u1) {
	//code2
	u1.REVIVE());
}EXECUTE(u1.DIE());
THIS.DIE();
```

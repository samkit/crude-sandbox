// Source: http://aperiodic.net/phil/scala/s-99/
//
// Some of the answers are copied from the original source
// questions but nevertheless i learned in the process

object Problem_1 extends App {
	// println(p3(3, List(1, 2, 3, 4, 5)))
    def p3[T](n : Int, list : List[T]) : T = (n, list) match {
	    case (0, h :: rest) => h
	    case (x, _ :: rest) => p3(x - 1, rest)
	    case _ => throw new NoSuchElementException
	}
    
    // println(p4(List(1, 2, 3, 4, 5)))
    def p4[T](list : List[T]) : Int = {
        def calculateLength(length : Int, list : List[T]) : Int = list match {
            case Nil => length
            case _ :: rest => calculateLength(length + 1, rest)
        }
        calculateLength(0, list)
    }
    
    // println(p5(List(1, 2, 3, 4, 5, 6)))
    def p5[T](list : List[T]) : List[T] = {
        def reverse(result : List[T], more : List[T]) : List[T] = more match {
            case Nil => result
            case h :: rest => reverse(h :: result, rest)
        }
        reverse(List(), list)
    }
    
    // TODO 
    // println(p6(List(1, 2, 3, 2, 1)))
    def p6[T](list : List[T]) : Unit = {
        def isPalindrom(left : List[T], right : List[T]) : Unit = (left, right) match {
            case (first :: rest, right) if rest.length != right.length => {
                println("Check1", first, rest, right)
                isPalindrom(rest, first :: right)
            }
            case (fl :: left, fr :: right) =>
            case _ => println("nothing")
        }
        isPalindrom(list, List())
    }
    
    def p7[T](list : List[T]) : List[T] = {
        list
    }

	override def main(args : Array[String]) = {
//	    println(p7(List(List(1, 1), 2, List(3, List(5, 8)))))
        println("helo")
        println("hello world")
	}
}
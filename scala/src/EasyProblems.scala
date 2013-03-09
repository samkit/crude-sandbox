// Source: http://aperiodic.net/phil/scala/s-99/
//
// Some of the answers are copied from the original source
// questions but nevertheless i learned in the process

object EasyProblems extends App {
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
    
    // println(p6(List(1, 2, 3, 2, 1)))
    def p6[T](list : List[T]) : Boolean = {
        def reverse(list : List[T]): List[T] = list match {
            case head :: rest => reverse(rest) ::: List(head)
            case Nil => list
        }
        // can isPalindrome() itself be a tail recursive function?
        list == reverse(list)
    }
    
    // println(p7(List(List(1, 1), 2, List(3, List(5, 8)))))
    def p7[T](list: List[Any]): List[Any] = list flatMap {
        case ms: List[_] => p7(ms) 
        case e => List(e)
    }
    
    // println(p7a(List(List(1, 1), 2, List(3, List(5, List(List(List(8))))))))
    // PRAISE: I did this myself!!!!
    def p7a(list: List[Any]): List[Any] = list match {
        case (head: List[_]) :: rest => p7a(head) ++ p7a(rest)
        case head :: rest => List(head) ++ p7a(rest)
        case Nil => Nil
    }
    
    // println(p8(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)))
    def p8[T](list: List[T]): List[T] = list match {
        case h1 :: h2 :: rest if h1 == h2 => p8(h1 :: rest)
        case head :: rest => head :: p8(rest)
        case e => println(e); e
    }
    
    // println(p9a(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)))
    // PRAISE: I did this in an overly complex manner, but functional!
    def p9[T](list: List[T]): List[List[T]] = {
        def collate(duplicates: List[T], list: List[T]): List[List[T]] = (list, duplicates) match {
            case (h1 :: r1, h2 :: r2) if h1 == h2 => collate(h1 :: duplicates, r1)
            case (head :: rest, Nil) => collate(List(head), rest)
            case (head :: rest, _) => duplicates :: collate(List(head), rest)
            case (Nil, e) => List(e)
        }
        collate(List(), list)
    }
    
    // println(p9a(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)))
    def p9a[T](list: List[T]): List[List[T]] = {
        // PRAISE: original author had a bug of returning List(List())
        // here which prints a redundant List() at the end
        if (list.isEmpty) Nil
        else {
            val (packed, rest) = list.span {_ == list.head}
            if (rest == Nil) List(packed)
            packed :: p9a(rest)
        }
    }
    
    // println(p10(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)))
    def p10[T](list: List[T]): List[(Int, T)] = {
        for (one <- p9(list))
            yield (one.length, one.head)
    }

    override def main(args: Array[String]) = {
        println(p10(List('a, 'a, 'a, 'a, 'b, 'c, 'c, 'a, 'a, 'd, 'e, 'e, 'e, 'e)))
    }
}

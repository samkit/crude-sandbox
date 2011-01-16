// Refer "http://en.wikipedia.org/wiki/Variadic_templates"
// for more information on variadic templates.

#include <iostream>
#include <string>
#include <typeinfo>

using namespace std;

template <typename... LIST>
class RecurseHierarchy;

// Partial specialization of template class RecurseHierarchy.
// This is done by creating a specialization which is itself
// templated.
// Read "Modern C++ Design" for more on such template
// facilities.
template <typename FIRST, typename... LIST>
class RecurseHierarchy<FIRST, LIST...> : public RecurseHierarchy<LIST...>
{
    class NotImplementedClass;

    typedef FIRST data_type;
public:
    RecurseHierarchy()
    {
        cout << "RecurseHierarchy [" << this << "]: " << typeid(data_type*).name() << endl;
    }

    virtual ~RecurseHierarchy()
    {
        cout << "~RecurseHierarchy [" << this << "]: " << typeid(data_type*).name() << endl;
    }
};

template<>
class RecurseHierarchy<>
{
};

template <typename FunctionType, typename... Args>
void dispatcher(FunctionType f, Args... args)
{
    f(args...);
}

void function_1(int i)
{
    cout << "function_1::" << i << endl;
}

void function_2(string const& value, string const& recepient)
{
    cout << "function_2::" << value << ", " << recepient << endl;
}

int main()
{
    {
        RecurseHierarchy<int, double, char, string> recurse;
    }

    cout << "Another test" << endl;

    dispatcher(function_1, 10);
    dispatcher(function_2, "Hello", "Samkit");

    return 0;
}

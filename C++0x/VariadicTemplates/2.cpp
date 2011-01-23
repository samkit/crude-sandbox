#include <iostream>

using namespace std;

class MyClass
{
public:
    void function_1()
    {
        cout << "function_1" << endl;
    }

    int function_2(int value)
    {
        cout << "function_2 [" << value << "]" << endl;
        return value;
    }
};

template <typename return_type, typename... function_arguments>
class functor
{
public:
    virtual return_type operator ()(function_arguments...) = 0;
};

class square_filter : public functor<int, int>
{
public:
    int operator ()(int value)
    {
        return value * value;
    }
};

template <typename return_type, typename... function_arguments>
class filter_all_arguments : public functor<return_type, function_arguments...>
{
public:
    filter_all_arguments(functor<return_type, function_arguments...> const& f)
        :m_functor(f)
    {
    }

    return_type operator ()(function_arguments... args)
    {
        return m_functor(args...);
    }

private:
    functor<return_type, function_arguments...>& m_functor;
};

template <typename class_type, typename return_type, typename... function_arguments>
class function
{
    typedef return_type (class_type::*pointer) (function_arguments...);
public:
    function(functor<return_type, function_arguments...>& f, pointer function)
        :m_filter(f),
         m_function(function)
    {
    }

    return_type operator ()(class_type& instance, function_arguments... args)
    {
        (instance.*m_function)(m_filter(args...));
    }

private:
    functor<return_type, function_arguments...>& m_filter;
    pointer m_function;
};

template <typename class_type>
class composed
{
public:
    template <typename return_type, typename... function_arguments>
    composed(class_type& instance, function<class_type, return_type, function_arguments...>& member_function)
    {
        member_function(instance, 9);
    }
};

int main()
{
    square_filter f;
    function<MyClass, int, int> function_2(f, &MyClass::function_2);

    MyClass myClass;
    composed<MyClass> myComposite(myClass, function_2);

    return 0;
}

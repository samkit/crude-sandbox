#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/xml_parser.hpp>
#include <iostream>
#include <string>

using namespace std;
using namespace boost::property_tree;

template <typename KeyType, typename DataType>
void print(KeyType const& key, DataType const& data)
{
}

template <>
void print<string, string>(string const& key, string const& data)
{
    cout << key << ": " << data << endl;
}

template <typename Iterator>
void iterate_ptree(Iterator start, Iterator finish, int max_recursion_level)
{
    if (max_recursion_level == 0)
    {
        return;
    }
    for (; start != finish; ++start)
    {
        print(start->first, start->second.data());
        iterate_ptree(start->second.begin(), start->second.end(), max_recursion_level - 1);
    }
}

int main(int argc, char* argv[])
{
    string fileName("test.xml");
    ptree pt;
    try
    {
        read_xml(fileName, pt);
    }
    catch(xml_parser_error const& e)
    {
        cout << "Exception caught: " << e.what() << endl;
        return -1;
    }

    int max_recursion_level(::atoi(argv[1]));
    iterate_ptree(pt.begin(), pt.end(), max_recursion_level);

    return 0;
}

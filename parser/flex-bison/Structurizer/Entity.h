#include <map>
#include <vector>

namespace Structurizer {

using namespace std;

class Dimensions {
 public:
	vector<long> data;
	void insert(long);
};

class SingleElement {
 public:
	Dimensions *dimensions;
	string data_type;
	string name;

	SingleElement() { }
	SingleElement(const string &, const string &, const Dimensions &);
	~SingleElement() { }
	void insert(string&, string&, Dimensions&);
};

class Elements {
 public:
	vector<SingleElement> data;
	void insert(const SingleElement&);
};

class Entity {
 public:
	map<string, Elements&> data;
	void insert(const string&, Elements&);
};

}	// namespace Structurizer ends

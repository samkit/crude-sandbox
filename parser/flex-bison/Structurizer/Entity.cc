#include <iostream>
#include "Entity.h"

using namespace Structurizer;

inline void Dimensions::insert(long i) {
	data.push_back(i);
}

inline SingleElement::SingleElement(const string &data_type, const string &name, const Dimensions &dimensions) {
	this->data_type = data_type;
	this->name = name;
	this->dimensions = dimensions;
}

inline void Elements::insert(const SingleElement &element) {
	data.push_back(element);
}

inline void Entity::insert(const string &name, Elements &element) {
	data[name] = element;
}

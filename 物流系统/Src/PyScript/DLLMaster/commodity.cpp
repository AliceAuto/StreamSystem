#include "head.h"


class Commodity {
public:
	// 属性
	int id;
	int stock; // 库存
	double price; // 价格
	string name; // 名称
	string description; // 商品描述
	// 带参数的构造函数
	Commodity(int Id, int Stock, double Price, string Name, string Description) {
		this->id = Id, this->stock = Stock, this->price = Price;
		this->name = name, this->description = Description;
	}
	// 打印当前对象的信息
	void print() {
		printf("id = %d, stock = %d, price = %llf, name = %s, description = %s\n", id, stock, price, name.c_str(), description.c_str());
	}
	// 返回某个属性的get方法
	int const get_id() { return this->id; }
	int const get_stock() { return this->stock; }
	double const get_price() { return this->price; }
	string const get_name() { return this->name; }
	string const get_desciption() { return this->description; }

};
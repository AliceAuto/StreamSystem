#include "head.h"


class Commodity {
public:
	// ����
	int id;
	int stock; // ���
	double price; // �۸�
	string name; // ����
	string description; // ��Ʒ����
	// �������Ĺ��캯��
	Commodity(int Id, int Stock, double Price, string Name, string Description) {
		this->id = Id, this->stock = Stock, this->price = Price;
		this->name = name, this->description = Description;
	}
	// ��ӡ��ǰ�������Ϣ
	void print() {
		printf("id = %d, stock = %d, price = %llf, name = %s, description = %s\n", id, stock, price, name.c_str(), description.c_str());
	}
	// ����ĳ�����Ե�get����
	int const get_id() { return this->id; }
	int const get_stock() { return this->stock; }
	double const get_price() { return this->price; }
	string const get_name() { return this->name; }
	string const get_desciption() { return this->description; }

};
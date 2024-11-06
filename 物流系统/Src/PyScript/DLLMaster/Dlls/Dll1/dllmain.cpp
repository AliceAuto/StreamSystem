// Dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "dllmain.h" // 包含头文件
// Dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "pch.h"  // 如果你的项目中使用了预编译头，否则可以删除这一行。
#include <cstdio> // 用于 printf
#include <json/json.h>
#include <string>
#include <sstream>
// Dllmain.cpp : 定义 DLL 应用程序的入口点。
#include "pch.h"  // 如果你的项目中使用了预编译头，否则可以删除这一行。
#include <cstdio> // 用于 printf
#include <json/json.h>
#include <string>
#include <sstream>

#ifdef _WIN32
#define DLL_EXPORT __declspec(dllexport)
#else
#define DLL_EXPORT
#endif

class JsonHandler {
public:
    // 创建 JSON 字符串
    std::string CreateJson(const std::string& name, int age, bool isStudent, const std::string& city, const std::string& zip) {
        Json::Value root;
        root["name"] = name;
        root["age"] = age;
        root["isStudent"] = isStudent;

        Json::Value address;
        address["city"] = city;
        address["zip"] = zip;
        root["address"] = address;

        Json::FastWriter writer;
        return writer.write(root);
    }

    // 解析 JSON 字符串并返回字段信息
    std::string ParseJson(const std::string& jsonString) {
        Json::Value root;
        Json::Reader reader;
        bool parsingSuccessful = reader.parse(jsonString, root);

        if (!parsingSuccessful) {
            return "Error parsing JSON: Unrecognized format or invalid JSON syntax.";
        }

        std::ostringstream result;
        result << "Name: " << root["name"].asString() << "\n";
        result << "Age: " << root["age"].asInt() << "\n";
        result << "IsStudent: " << root["isStudent"].asBool() << "\n";
        result << "City: " << root["address"]["city"].asString() << "\n";
        result << "Zip: " << root["address"]["zip"].asString() << "\n";

        return result.str();
    }
};

// 实例化 JsonHandler 对象
static JsonHandler jsonHandler;

// 导出函数：创建 JSON 字符串
extern "C" DLL_EXPORT const char* CreateJson(const char* name, int age, bool isStudent, const char* city, const char* zip) {
    static std::string jsonResult = jsonHandler.CreateJson(name, age, isStudent, city, zip);
    return jsonResult.c_str();
}

// 导出函数：解析 JSON 字符串
extern "C" DLL_EXPORT const char* ParseJson(const char* jsonString) {
    static std::string parseResult = jsonHandler.ParseJson(jsonString);
    return parseResult.c_str();
}

// DLL 中的函数实现
extern "C" __declspec(dllexport) int add(int a, int b) {
    // 返回两个整数的和
    return a + b;
}

#include <bits/stdc++.h>


class String {
    char *data;
    size_t str_len = 0;
    size_t max_len = 1;
public:
    String(); // constructor
    String(char* val);
    String(const String& source); // copy constructor
    String(String&& source); // move constructor
    ~String() { delete[] data; }
    void push_back(char c);
    char pop_back();
    size_t size() { return str_len; }
    friend std::ostream &operator<<(std::ostream &os, const String &s) {
        os << std::string(s.data);
        return os;
    }
    friend bool operator==(const String& a, const String& b) {
        return strcmp(a.data, b.data);
    }
    String& operator+=(const String& b) {
        size_t na = strlen(data), nb = strlen(b.data);
        char *new_data = new char[na + nb + 1];
        for (int i = 0; i < na; i++)
            new_data[i] = data[i];
        for (int i = 0; i < nb; i++)
            new_data[i + na] = b.data[i];
        new_data[na + nb] = '\0';
        delete[] data;
        data = new_data;
        str_len = na + nb;
        max_len = na + nb + 1;
        return *this;
    }
    friend String operator+(const String& a, const String& b) {
        return String(a) += b;
    }
};

String::String() : max_len(1), str_len(0) {
    data = new char[max_len];
    data[0] = '\0';
}

String::String(char* val) {
    if (val == nullptr) {
        data = new char[max_len];
        data[0] = '\0';
    }
    str_len = strlen(val);
    max_len = str_len + 1;
    data = new char[max_len];
    for (int i = 0; i < str_len; i++)
        data[i] = val[i];
    data[str_len] = '\0';
}

String::String(const String& source) : max_len(strlen(source.data)+1), str_len(strlen(source.data)) {
    data = new char[max_len];
    for (int i = 0; i < str_len; i++)
        data[i] = source.data[i];
    data[str_len] = '\0';
}

String::String(String&& source) {
    data = source.data;
    source.data = nullptr;
}

void String::push_back(char c) {
    if (str_len + 1 < max_len) {
        data[str_len] = c;
        str_len++;
    } else {
        max_len = max_len << 1;
        char *temp = data;
        data = new char[max_len];
        for (int i = 0; i < str_len; i++)
            data[i] = temp[i];
        data[str_len] = c;
        str_len++;
        delete[] temp;
    }
    data[str_len] = '\0';
}

char String::pop_back() {
    if (str_len == 0) {
        throw std::runtime_error("Pop zero length");
    }
    str_len--;
    char ret_val = data[str_len];
    data[str_len] = '\0';
    return ret_val;
}

int main() {
    String s;
    s.push_back('1');
    s.push_back('2');
    s.push_back('3');
    std::cout << s << "\n";
    s.pop_back();
    s.push_back('4');
    std::cout << s << "\n";
    String b;
    b.push_back('1');
    std::cout << (s == b) << "\n";
    std::cout << (s + b) << "\n";
}

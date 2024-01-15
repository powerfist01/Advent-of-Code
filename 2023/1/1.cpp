#include <bits/stdc++.h>

using namespace std;

int first_integer_character(string str, bool from_start=true){
	
	if(from_start == false){
		reverse(str.begin(), str.end());
	}

	for(int i = 0; i < str.length(); i++) {
		char c = str[i];
		if(c >= '0' && c <= '9')
			return c-'0';
	}
	return 0;
}

int main(){
	
	freopen("input", "r", stdin);
	
	string s;
	int answer = 0;
    	while(cin >> s){
			int first_integer = first_integer_character(s);
			int last_integer = first_integer_character(s, false);

			answer += first_integer*10 + last_integer;
    	}
	
	cout<<answer<<endl;
	
	return 0;
}


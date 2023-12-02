#include <bits/stdc++.h>

using namespace std;

int first_integer_character(string str, bool from_start=true){
	
	if(from_start == false){
		reverse(str.begin(), str.end());
	}

	string temp_str = "";
	for(int i = 0; i < str.length(); i++) {
		char c = str[i];
		if(c >= '0' && c <= '9'){
			return c-'0';
		} else{
			string arr[] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
			
			if(from_start == false){
				temp_str = c + temp_str;
			} else {
				temp_str += c;
			}

			for(int j = 0; j < 9; j++){
				if(temp_str.find(arr[j]) != string::npos){
					return j+1;
				}
			}
		}
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
		cout <<first_integer << " "<<last_integer<<endl;
		answer += first_integer*10 + last_integer;
	}
	
	cout<<answer<<endl;
	
	return 0;
}


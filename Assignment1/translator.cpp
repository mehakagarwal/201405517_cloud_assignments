#include<iostream>
#include<stdio.h>
#include<map>
#include<string>
#include<fstream>

using namespace std;
int main(){
	map<string,string> myMap;
	myMap["pushl	%ebp"]="pushq	%rbp";
	myMap[".cfi_def_cfa_offset 8"]=".cfi_def_cfa_offset 16";
	myMap[".cfi_offset 5, -8"]=".cfi_offset 6, -16";
	myMap["movl	%esp, %ebp"]="movq	%rsp, %rbp";
	myMap[".cfi_def_cfa_register 5"]=".cfi_def_cfa_register 6";
	myMap["andl	$-16, %esp"]="";
	myMap["subl	$16, %esp"]="";
	myMap["movl	$.LC0, (%esp)"]="movl	$.LC0, %edi";
	myMap["leave"]="popq	%rbp";
	myMap[".cfi_restore 5"]="";
	myMap[".cfi_def_cfa 4, 4"]=".cfi_def_cfa 7, 8";
	ifstream myfile("pgm1_32.s");
	string line;
	long size = myfile.tellg();
 	if(myfile.is_open())
	{
		while(getline(myfile,line))
		{
			int i;
			for(i=0;i<line.length();i++)
			{
				if(!isspace(line[i]))
				{
					break;
				}
			}
			line=line.substr(i,line.length()-i);
			if((myMap.find(line)!=myMap.end()))
			{
				if(myMap[line]!="")
					cout<<myMap[line]<<endl;
			}
			else
				cout<<line<<endl;			
		}
	}
	myfile.close();
	
	
	return 0;
}

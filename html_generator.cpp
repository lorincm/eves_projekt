#include <iostream>
#include <fstream>
#include <Windows.h>
#include <string>
#include <vector>
#include <atlstr.h>
#include <sstream>

using namespace std;

void input(string *array, vector<string> &szakirodalom, string &tmp);

int main(int argc, const char * argv[])
{
	setlocale(LC_ALL, "hun");

	vector<string>	szakirodalom, v;
	string			tmp, currentDate, currentline, array[4];
	SYSTEMTIME		time;
	ifstream		file("C:\\Users\\louvre\\Documents\\GitHub\\lorincm.github.io\\munka.html");

	GetLocalTime(&time);
	CString cstrMessage;
	cstrMessage.Format("%d-%02d-%02d",
		time.wYear,
		time.wMonth,
		time.wDay
	);
	currentDate = cstrMessage;
	
	input(array, szakirodalom, tmp);

	while (!file.eof())
	{
		getline(file, currentline);

		if (currentline == "<!---->")
		{
			v.push_back(u8"<br></br><table><tr><th>Dátum</th><th>A részfeladat megnevezése</th><th>Elvégzett munka rövid leírása</th><th>Tapasztalatok</th><th>Igénybe vett szakirodalom</th></tr><tr><td>");
			v.push_back(currentDate);
			v.push_back("</td><td>");
			v.push_back(array[0]);
			v.push_back("</td><td>");
			v.push_back(array[1]);
			v.push_back("</td><td>");
			v.push_back(array[2]);
			v.push_back("</td><td> ");
			v.push_back(array[3]);
			v.push_back("</td></table>");
			v.push_back("<!---->");
			break;
		}
		else
		{
			v.push_back(currentline);
		}
	}
	file.close();
	ofstream file2("C:\\Users\\louvre\\Documents\\GitHub\\lorincm.github.io\\munka.html");
	file.clear();

	for (int i = 0; i < v.size(); i++)
	{
		if (v[i] == "<!---->")
		{

			file2 << endl;
			file2 << v[i] << endl;
			file2 << u8"<a href=\"#top\">[ugrás az oldal tetejére]</a></center><div id = \"bot\"></div>\n</center></body></html>";
		}
		else
		{
			file2 << v[i];
		}
	}
	return 0;
}

void input(string *array, vector<string> &szakirodalom, string &tmp) 
{
	cout << "Részfeladat megnevezése: ";
	getline(cin, array[0]);
	cout << endl;
	cout << "Elvégzett munka rövid leírása: ";
	getline(cin, array[1]);
	cout << endl;
	cout << "Tapasztalatok: ";
	getline(cin, array[2]);
	cout << endl;
	do {
		tmp = "";
		cout << "Felhasznált irodalom: ";
		getline(cin, tmp);
		if (tmp != "")
		{
			szakirodalom.push_back("<a target=\"_blank\" href=\"");
			szakirodalom.push_back(tmp);
			szakirodalom.push_back("\">");
			szakirodalom.push_back(tmp);
			szakirodalom.push_back("</a> ");
		}
		cout << endl;
	} while (tmp != "");
	tmp = "";
	for (int i = 0; i < szakirodalom.size(); i++)
	{
		tmp += szakirodalom[i];
	}

	array[3] = tmp;
}

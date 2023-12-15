#include <bits/stdc++.h>
#include <fstream>
using namespace std;

map<char, int> order
    = { { 'A', 13 }, { 'K', 12 }, { 'Q', 11 }, { 'J', 10 }, { 'T', 9 } };
map<string, int> type;

vector<string>
split (const string &s, char separator = ' ')
{
  istringstream ss (s);
  string token;
  vector<string> tokens;
  while (getline (ss, token, separator))
    {
      if (!token.empty ())
        {
          tokens.push_back (token);
        }
    }
  return tokens;
}

int
getType (const string &s)
{
  map<char, int> count;
  for (char c : s)
    {
      count[c]++;
    }

  vector<int> num_occurrences;
  for (auto &[key, val] : count)
    {
      num_occurrences.push_back (val);
    }

  sort (num_occurrences.rbegin (), num_occurrences.rend ());

  if (num_occurrences[0] == 5 || num_occurrences[0] == 4)
    {
      return num_occurrences[0]; // 5 or 4 of a kind
    }
  else if (num_occurrences[0] == 3 && num_occurrences[1] == 2)
    {
      return 3; // Full house
    }
  else if (num_occurrences[0] == 3)
    {
      return 2; // 3 of a kind
    }
  else if (num_occurrences[0] == 2 && num_occurrences[1] == 2)
    {
      return 1; // 2 pairs
    }
  else if (num_occurrences[0] == 2)
    {
      return 0;
    }
  return -1;
}

bool
cmp (const string &lhs, const string &rhs)
{
  if (type[lhs] != type[rhs])
    {
      return type[lhs] < type[rhs];
    }

  for (int i = 0; i < lhs.size (); ++i)
    {
      if (order[lhs[i]] != order[rhs[i]])
        {
          return order[lhs[i]] < order[rhs[i]];
        }
    }
  return order[lhs[0]] < order[rhs[0]];
}

int
main ()
{
  ifstream fin ("fin.txt"); 
  cin.rdbuf (fin.rdbuf ());

  for (int i = 9; i >= 2; --i)
    {
      order['0' + i] = i - 1;
    }

  string line;
  vector<string> hands;
  map<string, int> bid_map;

  while (getline (cin, line))
    {
      vector<string> input = split (line, ' ');
      string hand = input[0];
      int bid = stoi (input[1]);
      bid_map[hand] = bid;
      hands.push_back (hand);
      type[hand] = getType (hand);
    }

  sort (hands.begin (), hands.end (), cmp);
  int res = 0;

  for (int i = 0; i < hands.size (); ++i)
    {
      res += (i + 1) * bid_map[hands[i]];
    }

  cout << res << endl;

  fin.close ();
  return 0;
}

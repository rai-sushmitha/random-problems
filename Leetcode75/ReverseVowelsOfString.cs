public class Solution {
    public string ReverseVowels(string s) {
       char[] sa = s.ToCharArray();
       char[] vowels = new char[]{'a', 'e', 'i', 'o', 'u'};
       int i = 0, j = s.Length - 1;

       while(i<j){
        while(i<j && !vowels.Contains(char.ToLower(sa[i]))){
            i=i+1;
        }
        while(i<j && !vowels.Contains(char.ToLower(sa[j]))){
            j = j-1;
        }
        if(i<j){
            char temp = sa[i];
            sa[i] = sa[j];
            sa[j] = temp;
        }
        i=i+1;
        j=j-1;
       }

       return new string(sa);
    }
}

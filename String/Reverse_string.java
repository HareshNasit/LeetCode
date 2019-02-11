public void reverseString(char[] s) {
	    //https://leetcode.com/problems/reverse-string/
            int i=0;
            int j=s.length-1;
            while (i < j) {
                char temp = s[i];
                s[i]= s[j];
                s[j] =temp;
                i++; j--;
            }
     }
}

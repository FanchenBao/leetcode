class Solution {
    public String sortVowels(String s) {
        /*
        LeetCode 2785
        
        Pick out the vowels, sort them, and put them back in.
        
        O(NlogN) 48 ms, faster than 64.06%
        */
        char[] sarr = s.toCharArray();
        List<Character> vs = new ArrayList<>();
        List<Integer> indices = new ArrayList<>();
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        for (int i = 0; i < sarr.length; i++) {
            if (vowels.contains(sarr[i])) {
                vs.add(sarr[i]);
                indices.add(i);
            }
        }
        Collections.sort(vs);
        for (int i = 0; i < vs.size(); i++)
            sarr[indices.get(i)] = vs.get(i);
        return String.valueOf(sarr);
    }
}


class Solution {
    public String sortVowels(String s) {
        /*
        This the counting sort solution, which takes O(N)
         */
        char[] sarr = s.toCharArray();
        Set<Character> vowels = new HashSet<>(Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'));
        int[] counts = new int[1000]; // for counting sort
        for (char c : sarr) {
            if (vowels.contains(c)) counts[c - 'A']++;
        }
        String sortedVowels = "AEIOUaeiou";
        int j = 0;
        for (int i = 0; i < sarr.length; i++) {
            if (vowels.contains(sarr[i])) {
                // skip the sorted vowels that do not appear in s
                while (j < sortedVowels.length() && counts[sortedVowels.charAt(j) - 'A'] == 0) j++;
                sarr[i] = sortedVowels.charAt(j);
                counts[sortedVowels.charAt(j) - 'A']--;
            }
        }
        return String.valueOf(sarr);
    }
}

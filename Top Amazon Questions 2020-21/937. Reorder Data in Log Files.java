public String[] reorderLogFiles(String[] logs) {
        // Runtime: O(N.M.LogN)
        // Space: O(M.logN)
        Comparator<String> comp = new Comparator<String> () {
            public int compare(String log1, String log2) {
                String[] split1 = log1.split(" ", 2);
                String[] split2 = log2.split(" ", 2);

                boolean isDigit1 = Character.isDigit(split1[1].charAt(0));
                boolean isDigit2 = Character.isDigit(split2[1].charAt(0));

                 // Case 1: Both are letter-logs
                if (!isDigit1 && !isDigit2) {
                    // Compare log content
                    int cmp = split1[1].compareTo(split2[1]);
                    if (cmp != 0) {
                        return cmp;
                    }

                    return split1[0].compareTo(split2[0]);
                }

                // Case 2: log1 is letter-log and log2 is digit-log
                if (!isDigit1 && isDigit2) {
                    return -1;
                }

                // Case 3: log2 is letter-log and log1 is digit-log
                else if (isDigit1 && !isDigit2) {
                    return 1;
                }
                // Case 4: log1 and log2 are digit-logs
                else {
                    return 0;
                }
            }
        };
        Arrays.sort(logs, comp);
        return logs;
    }

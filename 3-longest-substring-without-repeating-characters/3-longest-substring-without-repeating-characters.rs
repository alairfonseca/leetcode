use std::collections::HashMap;
use std::cmp;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut result: i32 = 1;
        let mut subs_start: i32 = 0;
        let mut subs_end: i32 = 0;
        let mut visited = HashMap::new();
        
        if s.len() == 0 {
            return 0;
        }
        
        for (i, ch) in s.chars().enumerate() {
            if !visited.contains_key(&ch) || visited[&ch] < subs_start {
                subs_end = (i as i32) + 1;
                result = cmp::max(result, subs_end - subs_start);
            } else {
                subs_start = visited[&ch] + 1;
            }
            
            visited.insert(ch, i as i32);
        }
        
        result
    }
}
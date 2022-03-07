impl Solution {
    pub fn palindrome(s: &[u8], l: usize, r: usize) -> (usize, usize) {
        let mut a = l;
        let mut b = r;

        let mut start = 0;
        let mut end = 0;
        
        while b < s.len() && s[a] == s[b] {
            start = a;
            end = b;

            if a == 0 {
                break;
            }

            a -= 1;
            b += 1;
        }

        (start, end)
    }

    
    pub fn longest_palindrome(s: String) -> String {
        let mut result = (0, 0);
        let mut current_longest = 0;
        let byte_string = s.as_bytes();
        
        for i in 0..byte_string.len() {
            let (odd_l, odd_r) = Solution::palindrome(byte_string, i, i);
            let (even_l, even_r) = Solution::palindrome(byte_string, i, i + 1);
            
            let odd_size = odd_r - odd_l + 1;
            let even_size = even_r - even_l + 1;
            
            if odd_size > even_size && odd_size > current_longest {
                current_longest = odd_size;
                result.0 = odd_l;
                result.1 = odd_r;
            } else if even_size > odd_size && even_size > current_longest {
                current_longest = even_size;
                result.0 = even_l;
                result.1 = even_r;
            }
        }
        
        s[result.0..=result.1].to_string()
    }
}
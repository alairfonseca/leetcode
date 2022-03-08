impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1 || num_rows >= s.len() as i32 {
            return s;
        }
        
        let mut rows = vec![String::new(); num_rows as usize];
        let mut row_index: i32 = 0;
        let mut step: i32 = 1;
        
        for ch in s.chars() {
            rows[row_index as usize].push(ch);
            
            if row_index == 0 {
                step = 1;
            }
            
            if row_index == (num_rows - 1) {
                step = -1;
            }
            
            row_index += step;
        }
        
        rows.concat()
    }
}
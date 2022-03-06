use std::collections::HashMap;

impl Solution {
    fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut known = HashMap::new();
        let mut result = vec![];

        for (i, v) in nums.iter().enumerate() {
            let comp = target - v;

            if known.contains_key(&nums[i]) {
                result.push(known[v]);
                result.push(i as i32);
            } else {
                known.insert(comp, i as i32);
            }
        }

        result
    }
}